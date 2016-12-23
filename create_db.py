# This program takes as argument the species of the leaf to scan and
# saves and saves an image to the database folder

import subprocess
import sys, os

if len(sys.argv) != 2:
    print 'Error: This program should receive the species of the leaf!'
    print 'Example: python2 create_db.py pepino\n'
    sys.exit()

species = sys.argv[1]

scanners = subprocess.check_output(['scanimage', '-L'])

# Get the name of the scanner and avoid cameras
for element in scanners.split('\n'):
    if 'libusb' in element:
        scanner = element[element.find('`')+1:element.find("'")]

# Finds a correct name to save the next image
images = os.listdir('database')
i = 1

while species+'_'+str(i)+'.jpg' in images:
    i += 1

name = species+'_'+str(i)+'.jpg'

# Changed coordinates to avoid black corner, resolution is 150 DPI
command = 'scanimage --device "'+ scanner +'" --format=jpeg -l 5 -x 180 -y 180 > database/'
command += name

os.system(command)
