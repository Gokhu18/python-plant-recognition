import matplotlib.pyplot as plt
import contour_fft
import numpy as np

image_path = 'images/leaf4.jpg'
show_image = True
show_values = False
fft = contour_fft.get_contour_fft(image_path, show_image, show_values)

#freq = np.fft.fftfreq(len(valores))
#plt.plot(freq, fft.real, freq, fft.imag)
#plt.plot(valores)
#print np.absolute(fft)[:10]
#plt.plot(np.absolute(fft)[:2**11])
#plt.show()
