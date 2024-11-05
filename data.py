import pandas as pd
from data_functions import *
import time
import cv2
import numpy as np

# x = longitude (vertical)
# y = latitude (horizontal)
start_time = time.perf_counter()
path = "data/bathymetry_zoom_in_japan_sea.csv"

# Read csv file into a dataframe
dataFrame = pd.read_csv(path)

# Delete first row (in case it's no data)
if isinstance(dataFrame['latitude'][0], str):
    dataFrame = dataFrame.drop([0])

matrixH = createMatrix(dataFrame)
array = np.zeros([len(matrixH), len(matrixH[0]), 3], dtype=np.uint8)

deepMax = findDeepMax(matrixH)
print(deepMax)

for i in range(len(matrixH)) :
    for j in range(len(matrixH[i])):
        # Not water
        if matrixH[i][j]>=0.0 :
            array[i,j]=[0,255,0]
        else:
            array[i,j] = [(abs(deepMax)-abs(matrixH[i][j]))%255, 0, 0]
        
cv2.imwrite('bat_img.jpg', array)
cv2.imshow("image", array)
cv2.waitKey()


end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Programme exécuté en : {execution_time: .5f} secondes")


