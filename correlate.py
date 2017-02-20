# This file takes as argument the path to the test image, calculates its
# contour fft and compares it using correlation with all the descriptors in
# descriptors.txt
# Usage: python2 correlate.py test/fresa.jpg

import contour_fft
import numpy as np
import json
import sys

# Verify correct number of command line arguments
if len(sys.argv) != 2:
    print 'Error: This program should receive the path to the image'
    print 'Example: python2 correlate.py test/fresa.jpg\n'
    sys.exit()

input_file = 'descriptors.txt'
image_path = sys.argv[1]
show_image = True
show_values = False

fft = contour_fft.get_contour_fft(image_path, show_image, show_values)

descriptors = json.load(file(input_file))

for name, descriptor in descriptors.items():
    print(name, np.correlate(fft, descriptor)[0])
