# That's a program that process a batch of image pairs.

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

import openpyxl           # Contains spreadsheet reading-writing packages
import matplotlib.pyplot as plt
import os
import sys
import func
import vel_profile


# MAIN()

# N is the number of image pairs
path = '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images'
N = (len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])-1)/2
print N

# num = 2 # number of averaging points

for i in range(1, N+1):
    A = '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images/B%03d_1.bmp' % i
    B = '/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Images/B%03d_2.bmp' % i
    print i
    # Calling the function that processes the image pairs
    func.pair_process(A, B, i)
    # openpiv.tools.display_vector_field('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/pair_%03d.txt' % i, scale=50, width=0.002)
    DATA = numpy.loadtxt('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/pair_%03d.txt' % i)
    vel_profile.velocity_profile(DATA, i)
    # print DATA
