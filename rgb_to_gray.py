import cv2

img_path = 'database/rabano.1.jpg'

img_rgb = cv2.imread(img_path)

cv2.namedWindow('image')
cv2.imshow('image', img_rgb)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', img_gray)
cv2.waitKey(0)

img_gray2 = img_rgb[:,:,0]
cv2.imshow('image', img_gray2)
cv2.waitKey(0)

cv2.destroyAllWindows()
