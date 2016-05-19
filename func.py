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

window_size = 64
overlap = 32
dt = 0.002
search_area_size = 64
threshold = 1.3


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
    u, v, sig2noise = openpiv.process.extended_search_area_piv( frame_a, frame_b, window_size=window_size, overlap=overlap, dt=dt, search_area_size=search_area_size, sig2noise_method='peak2mean' )

    # Calculates the centers of the interrogation windows
    x, y = openpiv.pyprocess.get_coordinates(image_size=frame_a.shape, window_size=window_size, overlap=overlap)

    plt.figure()
    plt.quiver(x, y, u, v)
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/RAW_%03d.png' % counter)

    # Filtering outlier vectors
    u, v, mask = openpiv.validation.sig2noise_val(u, v, sig2noise, threshold=threshold)

    plt.figure()
    plt.quiver(x, y, u, v)
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/AFTER_FILTER_1_%03d.png' % counter)

    u, v, mask = openpiv.validation.local_median_val(u, v, u_threshold=0.5, v_threshold = 20, size = 1)

    # Replacement of the outlier vectors for an interpolation between neighbours
    u, v = openpiv.filters.replace_outliers(u, v, method='localmean', max_iter=10, kernel_size=2)

    plt.figure()
    plt.quiver(x, y, u, v)
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/AFTER_OUTLIERS_%03d.png' % counter)

    # Gaussian
    u, v = openpiv.filters.gaussian(u, v, size=2)

    plt.figure()
    plt.quiver(x, y, u, v)
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/AFTER_GAUSSIAN_%03d.png' % counter)

    # Scaling in order to get dimensional units. Provide pixels / meter.
    x, y, u, v = openpiv.scaling.uniform(x, y, u, v, scaling_factor=100)

    # Saves, in a .txt file, the data
    openpiv.tools.save(x, y, u, v, mask, '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/pair_%03d.txt' % counter, delimiter='\t')

    # plots and saves image
    # plt.matshow(frame_a, fignum=100, cmap=plt.cm.gray)
    # plt.savefig('test.png')

    # openpiv.tools.display_vector_field('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/pair_%03d.txt' % counter, scale = 100, width = 0.0025)

    # plots arrow graph
    plt.figure()
    plt.quiver(x, y, u, v)
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/FINAL_%03d.png' % counter)

    plt.figure()
    plt.plot(x, v, 'ro')
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/XVpair_%03d.png' % counter)

    plt.figure()
    plt.plot(y, u, 'ro')
    plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/YUpair_%03d.png' % counter)
    return