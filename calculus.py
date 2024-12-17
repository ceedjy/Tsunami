"""
Authors : 
    Morgane Farez 
    Cassiopée Gossin 
"""

from math import sqrt

# Global variable :
g = 9.806 # aproximately 9,81 m/s2 | N/kg (a more exact value is taken to be more precise)


# functions for basic physic :

""" 
A function which calculate the speed of a propagation of a point disturbance in the ocean (also called tsunami) : 𝑣 = 𝑔ℎ**(1/2)
Parameters :
    g : acceleration of gravity at the Earth's surface, float 
    h : the height of the water column, float 
Return the speed, float 
"""
def speed(g, h):
    return sqrt(g*h)

"""
A function which calculate the distance from point A to point B : √(x2−x1)**2+(y2−y1)**2
Parameters : 
    A : start point, tuple (x,y)
    B : end point , tuple (x,y)
Return the distance, float
"""
def distance(A, B):
    xa = A[0]
    ya = A[1]
    xb = B[0]
    yb = B[1]
    distance = sqrt(((xb-xa)**2) + ((yb-ya)**2))
    return distance 


# functions for matrix :

"""
Find the minimum value in a matrix 
Parameters : 
    matrix : the matrix where we are searching
Return the minimum value, it's made for float but it can also be an int 
"""
def findMinMatrix(matrix):
    mini = min(matrix[0])
    for i in range(len(matrix)):
        if mini > min(matrix[i]):
            mini = min(matrix[i])
    return mini

"""
Find the maximum value in a matrix 
Parameters : 
    matrix : the matrix where we are searching
Return the maximum value, it's made for float but it can also be an int 
"""
def findMaxMatrix(matrix):
    maxi = max(matrix[0])
    for i in range(len(matrix)):
        if maxi < max(matrix[i]):
            maxi = max(matrix[i])
    return maxi
