# This program takes no input and generates the average descriptors of each
# of the species on the database folder
# Usage: python2 generate_descriptors.py

import matplotlib.pyplot as plt
import contour_fft
import numpy as np
import json
import os

folder = 'database'
output_file = 'descriptors.txt'

print('Reading files...\n')
images = sorted(os.listdir(folder))

name = ''
descriptors = {}

print('Calculating FFTs...\n')
for image in images:
    name = image[:image.index('_')]
    if name not in descriptors:
        print(name)
        descriptors[name] = list()

    fft = contour_fft.get_contour_fft(folder+'/'+image)
    descriptors[name].append(fft)

print('\nCalculating FFT average of each species...\n')
for specie,descriptor in descriptors.items():
    descriptors[specie] = list(np.mean(descriptor, axis=0))

with open(output_file, 'w') as f:
    f.write(json.dumps(descriptors))
