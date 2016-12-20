import subprocess
import os

scanners = subprocess.check_output(['scanimage', '-L'])

for element in scanners.split('\n'):
    if 'libusb' in element:
        scanner = element[element.find('`')+1:element.find("'")]

# Changed coordinates to avoid black corner, resolution is 150 DPI
ins = 'scanimage --device "' + scanner +'" --format=jpeg -l 5 -x 180 -y 180 > test/test.jpg'

os.system(ins)
