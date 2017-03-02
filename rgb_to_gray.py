import cv2

img_path = 'database/fresa.23.jpg'

imgrgb = cv2.imread(img_path)

cv2.namedWindow('image')
cv2.imshow('image', imgrgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
