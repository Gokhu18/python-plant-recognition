import numpy as np
import time
import cv2
import getpass

if getpass.getuser() == 'pi':
    from picamera.array import PiRGBArray
    from picamera import PiCamera

def get_contour_fft(image_path=False, show_image=False, show_values=False):
    # Loads the image, resizes it to 640x480 and converts it to gray scale
    # if image_path=False the image is to be taken by the camera
    if image_path:
        # Once the images are taken from the camera, resize won't be neccesary
        img = cv2.resize(cv2.imread(image_path), (640,480))[:,:,0]
    else:
        camera = PiCamera(resolution = (640, 480))
        rawCapture = PiRGBArray(camera)
        time.sleep(0.2)
        camera.capture(rawCapture, format="bgr")
        img = rawCapture.array[:,:,0]

    # Applies Otsu threshold
    ret2,image = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print (ret2)

    # Shows the black and white image with grayed contour
    if show_image:
        cv2.imshow('image2', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Finds a point to start the algorithm
    flag = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
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

    # The vector of directions around the contour of the leaf is found in this loop
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
