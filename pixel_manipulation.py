import cv2 as cv

img = cv.imread("C:/Users/Mazedur Rahman/Desktop/OpenCV/data/corporate.jpg")
cv.imshow('James Bond',img)

pixel = img[120,120]
print("Color Indensities are Red : {}, Green : {}, Blue : {}".format(pixel[0],pixel[1],pixel[2]))

red_pixel = img[120,120]
print("Red Color Indensiy is Red : {}".format(red_pixel[0]))

img[120,120]= (0,50,0)
pixel = img[120,120]
print("Color Indensities are Red : {}, Green : {}, Blue : {}".format(pixel[0],pixel[1],pixel[2]))

cv.waitKey(0)




