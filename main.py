# That's a program that process a batch of image pairs.
# TEST
# Import necessary modules
import cython
import numpy as np        # Necessary for the correct performance of the script
import openpiv.pyprocess    # Contains functions for field scaling
import openpiv.scaling    # Contains advanced algorithms for PIV analysis
import openpiv.tools      # Contains tools
import openpiv.validation
import openpiv.process
import openpiv.filters
import numpy
from skimage import io
import openpyxl           # Contains spreadsheet reading-writing packages
import matplotlib.pyplot as plt
import os
import sys
import func
import vel_profile
from PIL import Image



#MAIN()

# this lines of code renames the images to a correct name

# path01 = '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Test images'
# N = (len([f for f in os.listdir(path01) if os.path.isfile(os.path.join(path01, f))]))
# print N
# for i in range(1, N):
#     A = io.imread('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Test images/spe1461227550_f%03d-page1.bmp' % (2*i-1))
#     if (int(i % 2) == 0) and i != 1:
#         io.imsave('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images/B%03d_2.bmp' % int(i / 2 + .5), A)
#     else:
#         io.imsave('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images/B%03d_1.bmp' % (int(i / 2) + 1), A)
#
path01 = '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Test images'
N = (len([f for f in os.listdir(path01) if os.path.isfile(os.path.join(path01, f))]))
print N
for i in range(1, N):
    A = Image.open('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Test images/spe1461230341_f%03d.tif' % (2*i-1))
    A.seek(0)
    A.save('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images/B%03d_1.tif' % i)
    A.seek(1)
    A.save('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images/B%03d_2.tif' % i)

# FOLDERS = os.listdir('/Users/sergirosell/Documents/Master thesis/PIV/Images/')
# print FOLDERS


# N is the number of image pairs
path = '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images'
N = (len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])-1)/2
print N

# num = 2 # number of averaging points

for i in range(1, N+1):
    A = '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images/B%03d_1.tif' % i
    B = '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images/B%03d_2.tif' % i
    print i
    # Calling the function that processes the image pairs
    func.pair_process(A, B, i)
    # openpiv.tools.display_vector_field('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/pair_%03d.txt' % i, scale=50, width=0.002)
    # DATA = numpy.loadtxt('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/pair_%03d.txt' % i)
    # vel_profile.velocity_profile(DATA, i)
    # print DATA
