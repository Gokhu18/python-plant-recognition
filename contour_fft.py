import matplotlib.pyplot as plt
import numpy as np
import Image

def get_contour_fft(image_path, show_image, show_values):
    # Loads the image, resizes it to 640x480 and converts it to gray scale
    image = Image.open(image_path).resize((640,480)).convert('L')
    threshold = 220
    # Loads the image into pix as a numpy array
    pix = image.load()
    # Converts the image to black and white
    for i in range(480):
        for j in range(640):
            if pix[j,i] < threshold:
                pix[j,i] = 0
            else:
                pix[j,i] = 255

    flag = 0
    # Finds a point to start the algorithm
    for i in range(480):
        for j in range(640):
            if pix[j,i] == 0 and flag == 0:
                x_i = j
                y_i = i
                flag = 1

    next = 3
    # [x, y] is the starting point
    x = x_i
    y = y_i
    pix[x,y] = 128
    values = list()

    while x != x_i or y != y_i or len(values) == 0:
        # Creates a list with the neighbour pixels
        neighbours = [[x-1, y-1], [x, y-1], [x+1, y-1], [x+1, y], [x+1, y+1], [x, y+1], [x-1, y+1], [x-1, y]]
        # Finds the direction of the next pixel clockwise
        for i in range(8):
            pixel = pix[neighbours[next][0], neighbours[next][1]]
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
        pix[x,y] = 128

        # Little trick to make the algorithm work
        if next < 2:
            next = 5 + next
        else:
            next = next - 2

    # Shows the black and white image with grayed contour
    if show_image:
        image.show()
    
    # Prints amount of values in the contour and how many times wach one has been repeated
    if show_values:
        print 'values:',len(values),'0s:',values.count(0),'1s:',values.count(1),'2s:',values.count(2),'3s:',values.count(3),'4s:',values.count(4),'5s:',values.count(5),'6s:',values.count(6),'7s:',values.count(7)

    while (len(values) < 2**12):
        values.append(0)

    fft = np.fft.fft(values)

    return fft

