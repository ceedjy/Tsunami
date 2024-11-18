import numpy as np

def deletePositiveZ(dataFrame):
    for index, row in dataFrame.iterrows():
        if row['z'] > 0.0:
            dataFrame = dataFrame.drop(index)
    return dataFrame


def createMatrix2(dataFrame):
    matrix = np.array([])
    sizeDataSet = len(dataFrame)
    index = 1

    while index < sizeDataSet:
        height = dataFrame['z'][index]
        # Add the first height data to the matrix
        row = np.array([height])
        current_lat = dataFrame['latitude'][index]
        studied_lat = current_lat

        while studied_lat == current_lat and index < sizeDataSet:
            index += 1
            height = dataFrame['z'][index]
            row=np.append(row, height)
            studied_lat = dataFrame['latitude'][index]
        matrix=np.append(matrix, row)
    return matrix

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

def correctMatrix(matrix):
    normalLen = len(matrix[0])
    for i in range(1, len(matrix)):
        if len(matrix[i]) < normalLen:
            print(len(matrix[i]))
            print(normalLen)
            for j in range(len(matrix[i]), normalLen):
                blur = (matrix[i][j-1] + matrix[i-1][j-1] + matrix[i-1][j])/3
                #print(blur)
                matrix[i].append(blur)
    #print(matrix[32][34])
    return matrix

def findDeepMax(matrix):
    mini = min(matrix[0])
    for i in range(len(matrix)):
        if mini > min(matrix[i]):
            mini = min(matrix[i])
    return mini
            
