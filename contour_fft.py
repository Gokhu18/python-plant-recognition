import numpy as np
import time
import cv2

def get_contour_fft(image_path, show_image=False, show_values=False):
    # Loads the image from image_path
    img = cv2.imread(image_path)[:,:,0]

    # Applies Otsu threshold
    ret2,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Closing operation (wich would be opening if object were white) to
    # eliminate noise due to small particles as dust
    kernel = np.ones((3,3), np.uint8)
    image = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    # Shows the black and white image with grayed contour
    if show_image:
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 480,480)
        cv2.imshow('image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Finds a point to start the algorithm
    flag = 0
    for i in xrange(len(image)):
        for j in xrange(len(image[0])):
            if image[i, j] == 0:
                x_i = i
                y_i = j
                flag = 1
                break
        if flag:
            break

    next = 3
    # [x, y] is the starting point
    x = x_i
    y = y_i
    image[x, y] = 128
    values = list()

    # Find the vector of directions around the leaf's contour
    while x != x_i or y != y_i or len(values) == 0:
        # Creates a list with the neighbour pixels
        neighbours = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y+1], [x+1, y+1],
            [x+1, y], [x+1, y-1], [x, y-1]]
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

    # Prints amount of values and how many times each one has been repeated
    if show_values:
        print 'Values: {}, 0s: {}, 1s: {}, 2s: {}, 3s: {}, 4s: {}, 5s: {}, '\
            '6s: {}, 7s: {}'.format(len(values), values.count(0),
            values.count(1), values.count(2), values.count(3), values.count(4),
            values.count(5), values.count(6), values.count(7))

    # Zero padding to get a 4096 length vector
    while (len(values) < 2**12):
        values.append(0)

    # Computes FFT, eliminates the second half of the spectrum and computes
    # absoulte values
    fft = np.fft.fft(values)[1:2**11+1]
    fft = np.absolute(fft)

    # Normalizes the vector to an amplitude of 100
    m = max(fft) / 100.0
    for i in xrange(len(fft)):
        fft[i] /= m

    return fft
