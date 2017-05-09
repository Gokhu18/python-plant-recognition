# This program takes as arguments the folder to save the
# image and the species of the leaf
# Example: python2 create_db.py database pepino

import subprocess
import sys, os

# Verify correct number of command line arguments
if len(sys.argv) != 3:
    print('Error: This program should receive two arguments!')
    print('The folder to save the image and the species of the leaf')
    print('Example: python2 create_db.py database pepino\n')
    sys.exit()

folder = sys.argv[1]
species = sys.argv[2]

# Configuration of the command to scan the image
device = 'genesys:libusb:001:005'
mode = 'color'
Format = 'jpeg'
resolution = '150'
l = '5' # left ignored area to avoid black line
t = '5' # top ignored area to avoid black line
x = '200' # Horizontal width of the image
y = '200' # Vertical length of the image


# Finds a correct name to save the next image
images = os.listdir(folder)
i = 1

while species+'.'+str(i)+'.'+Format in images:
    i += 1

name = species+'.'+str(i)+'.'+Format

# create command to scan image and save it to folder
command = 'scanimage '
command += '--device ' + device
command += ' --mode=' + mode
command += ' --format=' + Format
command += ' --resolution=' + resolution
command += ' -l ' + l
command += ' -t ' + t
command += ' -x ' + x
command += ' -y ' + y
command += ' > '
command += folder + '/' + name

# Issue command to the operating system to scan the image
os.system(command)
