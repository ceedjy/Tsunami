import pandas as pd
from data_functions import *
import time
import cv2
import numpy as np


# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params): 
  
    # Left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
        # displaying X on image
        sizeX = cv2.getTextSize('X', 0, 1.0, 1)
        # displaying the coordinates 
        # on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(array, 'X', (x-(sizeX[0][0]//2),y+(sizeX[0][1]//2)), font, 
                    1, (0, 0, 255), 2) 
        cv2.imshow('image', array) 
  
  
    
  
# driver function 
if __name__=="__main__": 
  
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

    for i in range(len(matrixH)) :
        for j in range(len(matrixH[i])):
            # Not water
            if matrixH[i][j]>=0.0 :
                array[i,j]=[0,255,0]
            else:
                array[i,j] = [(abs(deepMax)-abs(matrixH[i][j]))%255, 0, 0]

    cv2.imwrite('bat_img.jpg', array)
    cv2.imshow("image", array)          
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    print(f"Programme exécuté en : {execution_time: .5f} secondes")
  
    # setting mouse handler for the image 
    # and calling the click_event() function 
    cv2.setMouseCallback('image', click_event) 
  
    # wait for a key to be pressed to exit 
    cv2.waitKey(0) 
  
    # close the window 
    cv2.destroyAllWindows() 


