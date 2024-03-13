from enum import ENUM
import numpy as np
import matplotlib.pyplot as plt

#space type ENUM
class SPACE_TYPE(num):
    BOX = 0
    OCTAHEDRON = 1
    SPHERE = 2
    #Add hypersphere and implement hyperbolic geometry for fun once you get the rest working !!!!


class space():
    
    SPACING_THRESHOLD = 0.01 #default in meters - particle intersection with bound modeling
    #
    bounds = np.array([]) #list of verticies of space - appended by constructors below
    
    #used to calculate wave propogation characteristics
    temperature = 0
    humidity = 0
    #TODO: and appends verticies to bounds for 
    def create_box(length, width, height):
    
    #returns if a specified point lies within a specified plane
    #param x, y z: p1 coordinate
    #param A, B, C: unit vector defining plane
    #x0, y0, z0: plane defining point (effectively shifts in unit vector direction of this point)
    def is_on_plane(x, y, z, A, B, C, x0, y0, z0):
        D = -A * x0 - B * y0 - C * z0 # calculate D using a point on the plane
        #check if point lies on the plane
        return abs(A * x + B * y + C * z + D) < SPACING_THRESHOLD
    
    #TODO:reads bounds field and creates a surface object
    def create_surface(bounds, type):
