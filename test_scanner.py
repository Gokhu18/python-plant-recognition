# This program takes no arguments, creates a connection to a Scanner,
# takes an image and stores it on the test folder.
# Usage: python2 test_scanner.py

import subprocess
import os

scanners = subprocess.check_output(['scanimage', '-L'])

for element in scanners.split('\n'):
    if 'libusb' in element:
        scanner = element[element.find('`')+1:element.find("'")]

# Changed coordinates to avoid black corner, resolution is 150 DPI
ins = 'scanimage --device "' + scanner +'" --format=jpeg -l 5 -x 180 -y 180 > test/test.jpg'

os.system(ins)
