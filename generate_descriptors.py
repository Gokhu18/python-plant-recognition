# This program takes no input and generates the descriptors of each image
# on the database folder, saving them as a dictionary on descriptors.txt
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

descriptors = {}

print('Calculating FFTs...')
for image in images:
    name = image[:image.index('.')]
    print(name)
    fft = contour_fft.get_contour_fft(folder+'/'+image)
    descriptors[name] = list(fft)

print('Saving to file...\n')
with open(output_file, 'w') as f:
    f.write(json.dumps(descriptors))
