import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('C:/Users/Mazedur Rahman/Downloads/person.jpg')

plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('James Bond')
plt.show()

