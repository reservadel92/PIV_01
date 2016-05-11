import numpy
import matplotlib.pyplot as plt
import openpiv


def velocity_profile(DATA, counter):

    DATA2 = sorted(DATA, key=lambda a_entry: a_entry[0])
    print DATA2
    # plt.figure()
    # plt.plot(x, v, 'ro')
    # plt.savefig('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/Vxvpair_%03d.png' % counter)
    numpy.savetxt('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/pair_SORTED_%03d.txt' % counter, DATA2)

    a = [row[0] for row in DATA2]
    a = numpy.unique(a)
    profile = numpy.zeros((len(a), 2), dtype=numpy.int)
    profile[1][0] = 1
    # print DATA2[1180][0]
    # for j in range(0, len(a)):
    #    profile[j][0] = DATA2[j][0] + profile[j][0]
    #    profile[j][1] = DATA2[j][1] + profile[j][1]
    # b = [row[1] for row in DATA2]
    # b = numpy.unique(b)
    # print len(b)
    # for m in range(0, len(a)):
    #    profile[m][0] = profile[m][0] / len(b)
    #    profile[m][1] = profile[m][1] / len(b)
    print profile
    # numpy.savetxt('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/X_%03d.txt' % counter, a)
    # numpy.savetxt('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/Y_%03d.txt' % counter, b)
    numpy.savetxt('/Users/sergirosell/Documents/Master thesis/PIV/PIV Multi/Results/XV_average_%03d.txt' % counter, profile)
    return

