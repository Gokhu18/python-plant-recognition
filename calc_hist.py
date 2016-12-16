# Recives one argument which is the route to an image then
# calculates its histogram and plots it

import cv2
import sys
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread(sys.argv[1]), (640,480)) [:,:,0]

hist = cv2.calcHist([img], [0], None, [256], [0,256])

plt.plot(hist)

plt.show()
