import matplotlib.pyplot as plt
import contour_fft
import numpy as np


image_path1 = 'images/leaf1.jpg'
image_path2 = 'images/leaf4.jpg'
show_image = True
show_values = True

fft1 = contour_fft.get_contour_fft(image_path1, show_image, show_values)

fft2 = contour_fft.get_contour_fft(image_path2, show_image, show_values)

print 'Correlation coeff: ', np.correlate(fft1, fft2)

plt.figure(1)
plt.subplot(211)
plt.plot(fft1)

plt.subplot(212)
plt.plot(fft2)
plt.show()
