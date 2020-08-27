import cv2

img = cv2.imread('../data/corporate.jpg')
px = img[100, 90]
print(px)  

px_blue = img[100, 90, 0]
print(px_blue) 


img[100, 90] = [255, 255, 255]
print(img[100, 90])  



print(img.shape) 
height, width, channels = img.shape
print(img.size)  
print(img.dtype)  

face = img[100:200, 115:188]
cv2.imshow('face', face)
cv2.waitKey(0)



