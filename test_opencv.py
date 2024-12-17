from PIL import Image
import numpy as np
import cv2

# Create a Numpy array
# len(array) = 100
# len(array[0]) = 200
# len(array[0][0]) = 3
array = np.zeros([100, 200, 3], dtype=np.uint8)
array[:,:1] = [255, 0, 0]  # Red left side
array[:,1:] = [0, 0, 255]   # Blue right side

cv2.imwrite('color_img.jpg', array)
cv2.imshow("image", array)
cv2.waitKey()

"""
# Convert array to image
img = Image.fromarray(array)
img.save('output.png')



import numpy, cv2
img = numpy.zeros([30,30,3])

img[:,:,0] = numpy.ones([30,30])*64/255.0
img[:,:,1] = numpy.ones([30,30])*128/255.0
img[:,:,2] = numpy.ones([30,30])*192/255.0

cv2.imwrite('color_img.jpg', img)
cv2.imshow("image", img)
cv2.waitKey()
"""