import subprocess
import os

scanners = subprocess.check_output(['scanimage', '-L'])

for element in scanners.split('\n'):
    if 'libusb' in element:
        scanner = element[element.find('`')+1:element.find("'")]

ins = 'scanimage --device "' + scanner +'" --format=tiff --resolution 75 > /home/seven/test.tiff'

os.system(ins)
