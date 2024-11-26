"""
Authors : 
    Morgane Farez 
    Cassiopée Gossin 
"""

import pandas as pd
from data_functions import *
import cv2
import numpy as np
from calculus import * 
from math import fabs
import glob
from PIL import Image

# global variables 
NB_CLICS = 2
TAB_CLICS = []
VERSION = 0 # version for the gif, 1 is for the coefficient and 0 is for the time in seconds 

# functions to create a gif : 

""" 
Calculate the time between two point using Bresenham march 
Parameters :
    stratPoint : the start point, a tuple (x, y)
    endPoint : the endpoint, a tuple (x, y)
Return the time, float
"""
def time(startPoint, endPoint):
    points_line = bresenham_march(array, startPoint, endPoint)
    speed_sum = 0
    for point in points_line :
        speed_sum += speed(g, abs(matrixH[point[1]][point[0]]))
    speed_final = speed_sum / len(points_line)
    time = distance(startPoint, endPoint)/speed_final
    return time

""" 
Creating the matrix for the time image
Parameters :
    startPoint : the start point, a tuple (x, y)
Return the matrix were all times are calculated 
"""
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

""" 
Creating the image with the matrix of the time 
Parameters :
    startPoint : the start point, a tuple (x, y)
Return nothing, but upload images and call the gif function 
"""
def createImageTime(startPoint):
    matrix = createMatrixTime(startPoint)
    array = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array1 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array2 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array3 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array4 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)
    array5 = np.zeros([len(matrix), len(matrix[0]), 3], dtype=np.uint8)

    timeMax = findMaxMatrix(matrix)

    global VERSION
    version = VERSION
    
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
            else: # with time in second (1-2-3-4-rest) # why not more images ? too much calculus, it takes too long to process
                if (matrix[i][j] >= 1.0 and matrix[i][j] < 1.05) or (matrix[i][j] >= 2.0 and matrix[i][j] < 2.05) or (matrix[i][j] >= 3.0 and matrix[i][j] < 3.05) or (matrix[i][j] >= 4.0 and matrix[i][j] < 4.05):
                    array[i,j] = [0, 0, 0]
                else:
                    array[i,j] = color
                
            # movie image 
            array5[i,j] = color
            if (version == 1 and coeff >= 0.8) or (version == 0 and matrix[i][j] <= 1.0):
                array1[i,j] = color
                array2[i,j] = color
                array3[i,j] = color
                array4[i,j] = color
            if (version == 1 and coeff >= 0.6 and coeff < 0.8) or (version == 0 and matrix[i][j] <= 2.0 and matrix[i][j] > 1.0) :
                array1[i,j] = [0, 0, 0]
                array2[i,j] = color
                array3[i,j] = color
                array4[i,j] = color
            if (version == 1 and coeff >= 0.4 and coeff < 0.6) or (version == 0 and matrix[i][j] <= 3.0 and matrix[i][j] > 2.0):
                array1[i,j] = [0, 0, 0]
                array2[i,j] = [0, 0, 0]
                array3[i,j] = color
                array4[i,j] = color
            if (version == 1 and coeff >= 0.2 and coeff < 0.4) or (version == 0 and matrix[i][j] <= 4.0 and matrix[i][j] > 3.0):
                array1[i,j] = [0, 0, 0]
                array2[i,j] = [0, 0, 0]
                array3[i,j] = [0, 0, 0]
                array4[i,j] = color
            if (version == 1 and coeff >= 0.0 and coeff < 0.2) or (version == 0 and matrix[i][j] > 4.0):
                array1[i,j] = [0, 0, 0]
                array2[i,j] = [0, 0, 0]
                array3[i,j] = [0, 0, 0]
                array4[i,j] = [0, 0, 0]

    # Show image
    cv2.imwrite('time_ready.jpg', array)
    # Show movie images
    cv2.imwrite('time_movie1.jpg', array1)
    cv2.imwrite('time_movie2.jpg', array2)
    cv2.imwrite('time_movie3.jpg', array3)
    cv2.imwrite('time_movie4.jpg', array4)
    cv2.imwrite('time_movie5.jpg', array5)
    createMovie(array1, array2, array3, array4, array5, array)
    
""" 
Creating the gif in another openCV window 
Parameters :
    arr1 - arr6 : all arrays wich represent all matrix used for each images of the gif 
Return nothing but open a new window with the gift 
"""
def createMovie(arr1, arr2, arr3, arr4, arr5, arr6): 
    tab = [arr1, arr2, arr3, arr4, arr5, arr6]
    indice = 0
    download_gif()
    for i in range(0, 24):
        array = tab[indice]
        cv2.imshow("movie", array) # Show image
        indice = (indice+ 1)%6
        cv2.waitKey(1000)

""" 
Downnload the gif in the current directory with images in the current directory
"""
def download_gif():
    frames = [Image.open(image) for image in glob.glob("./time_*.JPG")]
    frame_one = frames[0]
    frame_one.save("tsunami.gif", format="GIF", append_images=frames,
               save_all=True, duration=1000, loop=0)
    print("Fin du téléchargement du gif")

    
# functions to create the visual and calculate the time and the speed in consequence 

""" 
Apply the bresenham march to the image to know by wich cases of the matrix the tsunami go in straight line between two points 
Parameters :
    img : an image 
    p1 : a point, a tuple (x, y)
    p2 : a point, a tuple (x, y)
Return a table with all the point we are looking for 
"""
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
 
""" 
Display the coordinates of the points clicked on the image, create a gif and  images of the advancement of the tsunami 
Parameters :
    event : 
    x : the x value of the clicked point
    y : the y value of the clicked point
    flags : 
    param : 
Return a table with all the point we are looking for 
"""
def click_event(event, x, y, flags, params): 
    global NB_CLICS
    global TAB_CLICS
    
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

""" 
Driver function / main function
"""
if __name__=="__main__": 
    
    path = "data/bathymetry_small_area_japan_sea.csv"

    # Read csv file into a dataframe
    dataFrame = pd.read_csv(path)

    # Delete first row (in case it's no data)
    if isinstance(dataFrame['latitude'][0], str):
        dataFrame = dataFrame.drop([0])

    matrixH = correctMatrix(createMatrix(dataFrame))
    array = np.zeros([len(matrixH), len(matrixH[0]), 3], dtype=np.uint8)

    deepMax = findMinMatrix(matrixH)

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
    
    while(cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) > 0):
        
        cv2.imshow('image',array)
        
        if nb_clics > 0:
            cv2.setMouseCallback('image', click_event) 
            nb_clics -= 1
            
        k = cv2.waitKey(33)
        if k==27:    # Esc key to close window
            break
        elif k==114:  # r pressed to reset window
            array = base_map.copy()
            cv2.imshow("image", array) 
            NB_CLICS = 2
            TAB_CLICS = []  
        elif k==118:
            if VERSION == 1:
                VERSION = 0
                print("Change version to time in second")
            else : 
                VERSION = 1
                print("Change version to percent of advancement")
    
    # close the window 
    cv2.destroyAllWindows() 
    
