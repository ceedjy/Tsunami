import pandas as pd
from data_functions import *
import time


# x = longitude (vertical)
# y = latitude (horizontal)
start_time = time.perf_counter()
path = "data/bathymetry_small_area_japan_sea.csv"

# Read csv file into a dataframe
dataFrame = pd.read_csv(path)

# Delete first row (in case it's no data)
if isinstance(dataFrame['latitude'][0], str):
    dataFrame = dataFrame.drop([0])

matrixH = createMatrix(dataFrame)
print(matrixH)

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Programme exécuté en : {execution_time: .5f} secondes")


