import pandas as pd
from data_functions import *
import cv2
import numpy as np
from tsunami import * 
from math import fabs
#import time as tm
#import os
#import moviepy.video.io.ImageSequenceClip
import imageio

NB_CLICS = 2
TAB_CLICS = []

# function to display the coordinates of 
# of the points clicked on the image  
def click_event(event, x, y, flags, params): 
    global NB_CLICS
    global TAB_CLICS
    
    #print(f'x: {x}, y: {y}', )
    
    # Left mouse clicks 
    if NB_CLICS > 0:
        if event == cv2.EVENT_LBUTTONDOWN: 
            # displaying X on image
            sizeX = cv2.getTextSize('X', 0, 1.0, 1)
            # displaying the coordinates 
            print(f'x : {x} y : {y}')
            # on the image window 
            font = cv2.FONT_HERSHEY_SIMPLEX 
            cv2.putText(array, 'X', (x-(sizeX[0][0]//2),y+(sizeX[0][1]//2)), font, 1, (0, 0, 255), 2) 
            cv2.imshow('image', array)
            TAB_CLICS.append((x,y))
            # creation time image
            if NB_CLICS == 2:
                NB_CLICS -= 1
                createImageTime((x,y))
            else: NB_CLICS -= 1
            
            if NB_CLICS == 0 :
                # Draw line
                points_line = bresenham_march(array, TAB_CLICS[0], TAB_CLICS[1])
                speed_sum = 0
                for point in points_line :
                    speed_sum += speed(g, abs(matrixH[point[1]][point[0]]))
                speed_final = speed_sum / len(points_line)
                print(f'Speed : {speed_final} m/s')
                print(f'Time : {distance(TAB_CLICS[0], TAB_CLICS[1])/speed_final} s')
                
                cv2.line(array, TAB_CLICS[0], TAB_CLICS[1], (0,0,255), 1)
                cv2.imshow('image', array) # Show line on 2nd click
                
                # Re-init
                TAB_CLICS = []
                NB_CLICS = 2
                

def time(startPoint, endPoint): # calculate the time 
    points_line = bresenham_march(array, startPoint, endPoint)
    speed_sum = 0
    for point in points_line :
        speed_sum += speed(g, abs(matrixH[point[1]][point[0]]))
    #if len(points_line) == 0: 
        #print(startPoint, endPoint)
    speed_final = speed_sum / len(points_line)
    time = distance(startPoint, endPoint)/speed_final
    return time

def createMatrixTime(startPoint):
    matrix = []
    for i in range(0, len(matrixH)):
        matrix.append([])
        for j in range(0, len(matrixH[0])):
            if startPoint == (j, i):
                matrix[i].append(0)
            else:
                timeChr = time(startPoint, (j, i))
                matrix[i].append(timeChr)
    return matrix

def findTimeMax(matrix):
    maxi = max(matrix[0])
    for i in range(len(matrix)):
        if maxi < max(matrix[i]):
            maxi = max(matrix[i])
    return maxi

def createImageTime(startPoint):
    matrix = createMatrixTime(startPoint)
    array = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array1 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array2 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array3 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array4 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array5 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)

    timeMax = findTimeMax(matrix)

    version = 1 # 1: coeff, 2: time in secondes
    
    for i in range(len(matrix)) :
        for j in range(len(matrix[i])):
            coeff = 1-(abs(matrix[i][j])/(abs(timeMax)))
            color = [1-coeff*255, 0, coeff*255]
            # full image 
            if version == 1: # with percent of advancement (20-40-60-80-100)
                if (coeff >= 0.8 and coeff < 0.805) or (coeff >= 0.6 and coeff < 0.605) or (coeff >= 0.4 and coeff < 0.405) or (coeff >= 0.2 and coeff < 0.205):
                    array[i,j] = [0, 0, 0]
                else:
                    array[i,j] = color
            else: # with time in second (1-2-3-4-rest) # why note more ? too much calculus, it takes too long to process
                if (matrix[i][j] >= 1.0 and matrix[i][j] < 1.05) or (matrix[i][j] >= 2.0 and matrix[i][j] < 2.05) or (matrix[i][j] >= 3.0 and matrix[i][j] < 3.05) or (matrix[i][j] >= 4.0 and matrix[i][j] < 4.05):
                    array[i,j] = [0, 0, 0]
                else:
                    array[i,j] = color
                
            # movie image 
            array5[i,j] = color
            if (version == 1 and coeff >= 0.) or (version == 2 and matrix[i][j] <= 1.0):
                array1[i,j] = color
                array2[i,j] = color
                array3[i,j] = color
                array4[i,j] = color
            if (version == 1 and coeff >= 0.6 and coeff < 0.8) or (version == 2 and matrix[i][j] <= 2.0 and matrix[i][j] > 1.0) :
                array1[i,j] = [0, 0, 0]
                array2[i,j] = color
                array3[i,j] = color
                array4[i,j] = color
            if (version == 1 and coeff >= 0.4 and coeff < 0.6) or (version == 2 and matrix[i][j] <= 3.0 and matrix[i][j] > 2.0):
                array1[i,j] = [0, 0, 0]
                array2[i,j] = [0, 0, 0]
                array3[i,j] = color
                array4[i,j] = color
            if (version == 1 and coeff >= 0.2 and coeff < 0.4) or (version == 2 and matrix[i][j] <= 4.0 and matrix[i][j] > 3.0):
                array1[i,j] = [0, 0, 0]
                array2[i,j] = [0, 0, 0]
                array3[i,j] = [0, 0, 0]
                array4[i,j] = color
            if (version == 1 and coeff >= 0.0 and coeff < 0.2) or (version == 2 and matrix[i][j] > 4.0):
                array1[i,j] = [0, 0, 0]
                array2[i,j] = [0, 0, 0]
                array3[i,j] = [0, 0, 0]
                array4[i,j] = [0, 0, 0]

    # Show image
    cv2.imwrite('time_img.jpg', array)
    # Show movie images
    cv2.imwrite('time_movie1.jpg', array1)
    cv2.imwrite('time_movie2.jpg', array2)
    cv2.imwrite('time_movie3.jpg', array3)
    cv2.imwrite('time_movie4.jpg', array4)
    cv2.imwrite('time_movie5.jpg', array5)
    createMovie(array1, array2, array3, array4, array5, array)
    
def createMovie(arr1, arr2, arr3, arr4, arr5, arr6): # a appeler en mode (createMovieTime(mov1, mov2, mov3, mov4, mov5, time_img))
    # faire une boucle infini dans une autre page openCV pour afficher en boucle les images de temps 
    tab = [arr1, arr2, arr3, arr4, arr5, arr6]
    indice = 0
    for i in range(0, 24):
        array = tab[indice]
        cv2.imshow("movie", array) # Show image
        indice = (indice+ 1)%6
        #tm.sleep(3)
        cv2.waitKey(1000)
    return 

def bresenham_march(img, p1, p2):
     x1 = p1[0]
     y1 = p1[1]
     x2 = p2[0]
     y2 = p2[1]
     
     if ( 
         x1 >= img.shape[1]
         or x2 >= img.shape[1]
         or y1 >= img.shape[0]
         or y2 >= img.shape[0]
     ): 
         #tests if line is in image, necessary because some part of the line must be inside, it respects the case that the two points are outside

         if not cv2.clipLine((0, 0, *img.shape), p1, p2):
             print("not in region")
             return

     steep = fabs(y2 - y1) > fabs(x2 - x1)
     if steep:
         x1, y1 = y1, x1
         x2, y2 = y2, x2

     # takes left to right
     also_steep = x1 > x2
     if also_steep:
         x1, x2 = x2, x1
         y1, y2 = y2, y1

     dx = x2 - x1
     # fabs return the absolute value of a number (abs() = absolute value but transform to float)
     dy = fabs(y2 - y1)
     error = 0.0
     delta_error = 0.0
     # Default if dx is zero
     if dx != 0:
         delta_error = fabs(dy / dx)

     y_step = 1 if y1 < y2 else -1

     y = y1
     ret = []
     for x in range(x1, x2):
         p = (y, x) if steep else (x, y)
         if p[0] < img.shape[1] and p[1] < img.shape[0]:
             ret.append(p)
         error += delta_error
         if error >= 0.5:
             y += y_step
             error -= 1
     if also_steep:  # because we took the left to right instead
         ret.reverse()
     return ret  
  
    
def restart_window():
    pass
    
  
# driver function 
if __name__=="__main__": 
  
    path = "data/bathymetry_golfe_gascogne.csv" #bathymetry_small_area_japan_sea

    # Read csv file into a dataframe
    dataFrame = pd.read_csv(path)

    # Delete first row (in case it's no data)
    if isinstance(dataFrame['latitude'][0], str):
        dataFrame = dataFrame.drop([0])

    matrixH = correctMatrix(createMatrix(dataFrame))
    array = np.zeros([len(matrixH), len(matrixH[0]), 3], dtype=np.uint8)

    deepMax = findDeepMax(matrixH)

    for i in range(len(matrixH)) :
        for j in range(len(matrixH[i])):
            # Not water
            if matrixH[i][j] >= 0.0:
                array[i, j] = [0, 100, 0]
            else:
                coeff = 255-(abs(matrixH[i][j])*255/(abs(deepMax)))
                array[i,j] = [int(coeff), 0, 0]
    
    # Copy do not touch
    base_map = array.copy()
    
    nb_clics = 2
    
    # Show image
    cv2.imwrite('bat_img.jpg', array)
    cv2.imshow("image", array) 
    
    if nb_clics > 0:
        cv2.setMouseCallback('image', click_event) 
        nb_clics -= 1

    # wait for a key to be pressed to exit 
    cv2.waitKey(0) 
    
    # close the window 
    cv2.destroyAllWindows()
    


