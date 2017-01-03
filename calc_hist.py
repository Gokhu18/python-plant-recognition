# Recives one argument which is the route to an image then
# calculates its histogram and plots it

import cv2
import sys
import matplotlib.pyplot as plt

# Verify correct number of command line arguments
if len(sys.argv) != 2:
    print 'Error: This program should receive the path to the image!'
    print 'Example: python2 calc_hist.py database/fresa_1.jpg\n'
    sys.exit()

# Loads image to img
img = cv2.imread(sys.argv[1])

# Calculates histogram of img channel 2 "blue", 256 bins
hist = cv2.calcHist([img], [2], None, [256], [0,256])

plt.plot(hist)

plt.show()
