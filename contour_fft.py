import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_contour_fft(image_path, show_image, show_values):
    # Loads the image, resizes it to 640x480 and converts it to gray scale
    #image = Image.open(image_path).resize((640,480)).convert('L')
    threshold = 220
    image = cv2.resize(cv2.imread(image_path, 0), (640,480))

    # Loads the image into pix as a numpy array
    # Converts the image to black and white
    for i in range(480):
        for j in range(640):
            if image[i, j] < threshold:
                image[i, j] = 0
            else:
                image[i, j] = 255

    flag = 0
    # Finds a point to start the algorithm
    for i in range(480):
        for j in range(640):
            if image[i, j] == 0 and flag == 0:
                x_i = i
                y_i = j
                flag = 1

    next = 3
    # [x, y] is the starting point
    x = x_i
    y = y_i
    image[x, y] = 128
    values = list()

    while x != x_i or y != y_i or len(values) == 0:
        # Creates a list with the neighbour pixels
        neighbours = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y+1], [x+1, y+1], [x+1, y], [x+1, y-1], [x, y-1]]
        # Finds the direction of the next pixel clockwise
        for i in range(8):
            pixel = image[neighbours[next][0], neighbours[next][1]]
            if pixel == 0 or pixel == 128:
                break
            next = next + 1
            if next == 8:
                next = 0

        values.append(next)

        # Updates the actual pixel value
        x = neighbours[next][0]
        y = neighbours[next][1]

        # Changes the pixel color to gray to make it visible on the image
        image[x,y] = 128

        # Little trick to make the algorithm work
        if next < 2:
            next = 5 + next
        else:
            next = next - 2

    # Shows the black and white image with grayed contour
    if show_image:
        cv2.imshow('image2', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    # Prints amount of values in the contour and how many times wach one has been repeated
    if show_values:
        print 'values:',len(values),'0s:',values.count(0),'1s:',values.count(1),'2s:',values.count(2),'3s:',values.count(3),'4s:',values.count(4),'5s:',values.count(5),'6s:',values.count(6),'7s:',values.count(7)

    # Zero padding to get a 4096 length vector
    while (len(values) < 2**12):
        values.append(0)

    # Computes FFT, eliminates the second half of the spectrum and computes absoulte values
    fft = np.fft.fft(values)[1:2**11+1]
    fft = np.absolute(fft)

    # Normalizes the vector to an amplitude of 100
    m = max(fft) / 100.0
    for i in xrange(len(fft)):
        fft[i] /= m

    return fft
    #return values[1:2**11+1]

