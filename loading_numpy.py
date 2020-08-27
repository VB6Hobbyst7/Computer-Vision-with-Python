import numpy as np
import matplotlib.pyplot as plt
import cv2

#Image for Numpy
img = plt.imread('C:/Users/Mazedur Rahman/Downloads/person.jpg')

print(type(img))
print(img.shape)
print(img.ndim)
print(img.size)
print(img.dtype)
print(img.nbytes)

print(img[10, 10, 0])
print(img[10, 10, 1])
print(img[10, 10, 2])

print(img[10,10,:])
print(img[10,10])





