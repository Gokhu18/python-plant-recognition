# Recives one argument which is the route to an image then
# calculates its histogram and plots it

import cv2
import sys
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print 'Error: This program should receive the path to the image!'
    print 'Example: python2 calc_hist.py images/leaf1.jpg\n'
    sys.exit()

img = cv2.resize(cv2.imread(sys.argv[1]), (640,480)) [:,:,0]

hist = cv2.calcHist([img], [0], None, [256], [0,256])

plt.plot(hist)

plt.show()
