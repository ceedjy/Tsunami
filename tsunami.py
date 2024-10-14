# -*- coding: utf-8 -*-
"""
Authors : 
    Morgane Farez 
    Cassiopée Gossin 
Subject : Tsunami representation
"""

from math import sqrt

# should be taken from data 
Matrix = [[1, 2, 3, 1],
          [2, 3, 1, 2],
          [3, 1, 2, 3],
          [1, 2, 3, 1]]

# Global variable :
g = 9.806 # aproximately 9,81 m/s2 | N/kg (a more exact value is taken to be more precise)

""" 
A function which calculate the speed of a propagation of a point disturbance in the ocean (also called tsunami) : 𝑣 = 𝑔ℎ**(1/2)
Parameters :
    g : acceleration of gravity at the Earth's surface, float 
    h : the height of the water column, float 
"""
def speed(g, h):
    return sqrt(g*h)

"""
A function which calculate the distance from point A to point B : √(x2−x1)**2+(y2−y1)**2
Parameters : 
    A : start point, tuple (x,y)
    B : end point , tuple (x,y)
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
"""
def time(h, A, B):
    dist = distance(A, B)
    sp = speed(g, h)
    time = dist/sp
    print(dist)
    print(sp)
    return time


# il faudra decouper ca pour avoir le temps total mais en fct des différentes valeurs de h


### TEST ###
pointA = (3, 1)
pointB = (0, 3)
t = time(2.1, pointA, pointB)
print(t)


