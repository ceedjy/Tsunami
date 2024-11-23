"""
Authors : 
    Morgane Farez 
    Cassiopée Gossin 
"""

import numpy as np

""" 
Create a matrix with all the data in the data frame 
Parameters :
    dataFrame : the dataframe we are using
Return the matrix with all the values inside 
"""
def createMatrix(dataFrame):
    matrix = []
    sizeDataSet = len(dataFrame)
    index = 1

    while index < sizeDataSet:
        height = dataFrame['z'][index]
        # Add the first height data to the matrix
        row = [height]
        current_lat = dataFrame['latitude'][index]
        studied_lat = current_lat
        while studied_lat == current_lat and index < sizeDataSet:
            index += 1
            height = dataFrame['z'][index]
            row.append(height)
            studied_lat = dataFrame['latitude'][index]
        matrix.append(row)
    return matrix

""" 
Correct the matrix to have a matrix where all lines have the same length 
If there is not enought value, a blur is ally on the missing value to create new ones 
Parameters :
    matrix : the matrix we want to correct
Return the corrected matrix  
"""
def correctMatrix(matrix):
    normalLen = len(matrix[0])
    for i in range(1, len(matrix)):
        if len(matrix[i]) < normalLen:
            for j in range(len(matrix[i]), normalLen):
                blur = (matrix[i][j-1] + matrix[i-1][j-1] + matrix[i-1][j])/3
                matrix[i].append(blur)
    return matrix
