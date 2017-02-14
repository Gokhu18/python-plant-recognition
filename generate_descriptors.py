# This program takes no input and generates the average descriptors of each
# of the species on the database folder
# Usage: python2 generate_descriptors.py

import matplotlib.pyplot as plt
import contour_fft
import numpy as np
import os
import re

print('Reading files...\n')

folder = 'database'

images = sorted(os.listdir(folder))

name = ''
ffts = []
descriptors = {}

print('Calculating FFTs...\n')

for image in images:
    name = image[:image.index('_')]
    number = re.findall(r'\d+', image)[0]
    fft = contour_fft.get_contour_fft(folder+'/'+image)
    if name not in descriptors:
        print(name)
        descriptors[name] = list()
    descriptors[name].append(fft[:10])

print descriptors
