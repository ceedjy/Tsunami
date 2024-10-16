def deletePositiveZ(dataFrame):
    for index, row in dataFrame.iterrows():
        if row['z'] > 0.0:
            dataFrame = dataFrame.drop(index)
    return dataFrame


def createMatrix(dataFrame):
    matrix = []
    sizeDataSet = len(dataFrame)
    index = 1

    while index < sizeDataSet:
        height = dataFrame['z'][index]
        # Add the first height data to the matrix
        matrix.append([height])
        current_lat = dataFrame['latitude'][index]
        studied_lat = current_lat

        while studied_lat == current_lat and index < sizeDataSet:
            index += 1
            height = dataFrame['z'][index]
            matrix[len(matrix)-1].append(height)
            studied_lat = dataFrame['latitude'][index]

    return matrix

