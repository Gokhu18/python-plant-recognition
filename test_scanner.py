import subprocess
import os

scanners = subprocess.check_output(['scanimage', '-L'])

for element in scanners.split('\n'):
    if 'libusb' in element:
        scanner = element[element.find('`')+1:element.find("'")]

ins = 'scanimage --device "' + scanner +'" --format=jpeg -x 150 -y 150 > test/test.jpg'

os.system(ins)
