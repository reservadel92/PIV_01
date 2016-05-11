import numpy as np        # Necessary for the correct performance of the script
import openpiv.pyprocess    # Contains functions for field scaling
import openpiv.scaling    # Contains advanced algorithms for PIV analysis
import openpiv.tools      # Contains tools
import openpiv.validation
import openpiv.process
import openpiv.filters
# import openpyxl           # Contains spreadsheet reading-writing packages
import matplotlib.pyplot as plt
import os
import sys

# Functions


def pair_process(file_a, file_b, counter):

    # That's the function that process each image pair.
    # Load the images and convert them to 32 bits. At this moment images are situated at same folder as main.

    frame_a = openpiv.tools.imread(file_a).astype(np.int32)
    frame_b = openpiv.tools.imread(file_b).astype(np.int32)

    # Processes the image pair: zero order displacement predictor cross-correlation algorithm.
    # window_size: size of the interrogation window for frame_a
    # overlap in pixels between adjacent windows
    # dt: time in seconds between the two image frames
    # search_area_size: size in pixels of the search area on frame b.
    # sig2noise_method: method used for the evaluation of the signal/noise ratio
    u, v, sig2noise = openpiv.process.extended_search_area_piv(frame_a, frame_b, window_size=24, overlap=12, dt=0.02, search_area_size=64, sig2noise_method='peak2peak')

    # Calculates the centers of the interrogation windows
    x, y = openpiv.pyprocess.get_coordinates(image_size=frame_a.shape, window_size=24, overlap=12)

    # Filtering outlier vectors
    u, v, mask = openpiv.validation.sig2noise_val(u, v, sig2noise, threshold=1.4)

    # Replacement of the outlier vectors for an interpolation between neighbours
    u, v = openpiv.filters.replace_outliers(u, v, method='localmean', max_iter=10, kernel_size=2)

    # Scaling in order to get dimensional units. Provide pixels / meter.
    x, y, u, v = openpiv.scaling.uniform(x, y, u, v, scaling_factor=96.52)

    # Saves, in a .txt file, the data
    openpiv.tools.save(x, y, u, v, mask, '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/pair_%03d.txt' % counter, delimiter='\t')

    # plots and saves image
    # plt.matshow(frame_a, fignum=100, cmap=plt.cm.gray)
    # plt.savefig('test.png')

    # plots arrow graph
    plt.figure()
    plt.quiver(x, y, u, v)
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/Arrow_%03d.png' % counter)

    plt.figure()
    plt.plot(x, v, 'ro')
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/XVpair_%03d.png' % counter)

    plt.figure()
    plt.plot(y, u, 'ro')
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/YUpair_%03d.png' % counter)
    return