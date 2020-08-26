import cv2

img = cv2.imread('C:/Users/Mazedur Rahman/Downloads/person.jpg')

cv2.imshow('John Smith',img)
k = cv2.waitKey(0)&0xFF
if k == ord('e'):
    cv2.destroyAllWindows()

elif k == ord('s'):
    cv2.imwrite('C:/Users/Mazedur Rahman/Desktop/Computer-Vision-with-Python/corporate.jpg',img)
    cv2.destroyAllWindows()
    


