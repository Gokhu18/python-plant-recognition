import matplotlib.pyplot as plt
import contour_fft
import numpy as np
import sys

if len(sys.argv) < 2 or len(sys.argv) > 4:
    print 'Error: This program should receive one to three arguments'
    print 'Usage: python2 test_thres.py "Path_to_image" "show_image" "show_values"'
    print 'Example: python2 test_thres.py images/leaf1.jpg True False'
    print 'Example: python2 test_thres.py images/leaf1.jpg True'
    print 'Example: python2 test_thres.py images/leaf1.jpg\n'
    sys.exit()

image_path = sys.argv[1]
show_image = False if len(sys.argv) < 3 else bool(sys.argv[2])
show_values = False if len(sys.argv) < 4 else bool(sys.argv[3])
fft = contour_fft.get_contour_fft(image_path, show_image, show_values)

#freq = np.fft.fftfreq(len(valores))
#plt.plot(freq, fft.real, freq, fft.imag)
#plt.plot(valores)
#print np.absolute(fft)[:10]
#plt.plot(np.absolute(fft)[:2**11])
#plt.show()
