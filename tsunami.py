# -*- coding: utf-8 -*-
"""
Authors : 
    Morgane Farez 
    Cassiopée Gossin 
Subject : Tsunami representation
"""

from math import sqrt

#  here we consider that the points and the map are in an orthonormal reference 

# should be taken from data 
Matrix = [[1, 2, 3, 1],
          [2, 3, 1, 2],
          [3, 1, 2, 3],
          [1, 2, 3, 1]]

hTest = 3.1
hTest2 = 4

Matrix2 = [[hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest],
           [hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest, hTest]]

# Global variable :
g = 9.806 # aproximately 9,81 m/s2 | N/kg (a more exact value is taken to be more precise)

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

"""
A function which calculate the time a tsunami goes from point A to point B
Parameters : 
    h : the height of the water column, float 
    A : start point, tuple (x,y)
    B : end point , tuple (x,y)
Return the time, float  
""""""
def time(h, A, B):
    dist = distance(A, B)
    sp = speed(g, h)
    time = dist/sp
    return time


A function which calulate in which case the point is on the matrix 
Parameters : 
    A : the point, tuple (x,y)
    width : the width of the entire map 
    height : the height of the entire map 
    widthOneCell : The width of only one cell in the map (we consider that one cell is a square)
Return the corresponding h from the matrix where the point is on the map, float 
"""
def pt_to_H(A, matrix, width, height, widthOneCell):
    xa = A[0]
    ya = A[1]
    # the x axis 
    i = 0
    while ((widthOneCell * i) < xa):
        i+=1
    xM = (i-2)
    # the y axis 
    j = 0
    while ((widthOneCell * j) < ya):
        j+=1
    yM = (j-2)
    h = matrix[yM][xM]
    print(xa, ya, xM, yM)
    return h

# il faudra decouper ca pour avoir le temps total mais en fct des différentes valeurs de h
# il faudrait appliquer time sur chaque partie de du vecteur jusqu a que ca touche les bords
# il faudra se mettre d'accord sur les unités de tout 

### TESTS ###

# for the time 
"""
pointA = (3, 1)
pointB = (0, 3)
t = time(2.1, pointA, pointB)
print(t)
"""

# for the pt_to_H
"""
ptA = (69.2, 36.4)
width = 100
height = 100
widthOneCell = 10
print(pt_to_H(ptA, Matrix2, width, height, widthOneCell))
"""

# for testing if the time is good, see for a constant h and a constant distance if the time is the same
"""
pA = (30, 30)
pB1 = (10, 10)
pB2 = (50, 50)
pB3 = (50, 10)
pB4 = (10, 50)

pB5 = (30, 10)
pB6 = (10, 30)
pB7 = (50, 30)
pB8 = (30, 50)

print(time(2, pA, pB1))
print(time(2, pA, pB2))
print(time(2, pA, pB3))
print(time(2, pA, pB4))

print(time(2, pA, pB5))
print(time(2, pA, pB6))
print(time(2, pA, pB7))
print(time(2, pA, pB8))
"""


