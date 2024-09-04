# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:24:44 2020

@author: Stefan Weichert
"""
# import the usual libraries
import numpy as np
import matplotlib.pyplot as plt

# set some parameters
a = 0.6;
b = 0.5;
c = 0.2;

# define functions that calculate u and v (velocity components) as a function of the position
def u(x,y):
    return a**2-(b-c*x)**2
def v(x,y):
    return -2*c*b*y+c*c*x*y*2

# set the range in which we want to calculate and plot everything
xmin = -2
xmax = +8
ymin = -2
ymax = +2

# create x and y position vectors
x = np.linspace(xmin,xmax,21)
y = np.linspace(ymin,ymax,18)

# make the meshgrid we need for evaluating the functions u and v at each position
[X,Y] = np.meshgrid(x,y)

# calculate velocity (vector) components
U = u(X,Y)
V = v(X,Y)

# Do the vector plot (without correct scaling)
plt.figure(1)
plt.clf()
plt.quiver(X,Y,U,V)
plt.title("Wrong scaling of arrows")
# Do the vector plot (with correct scaling)
plt.figure(2)
plt.clf()
plt.quiver(X,Y,U,V, angles='xy', scale_units='xy')
plt.title("correct (spatial) scaling of arrows")
# Play around with this!  pull the figure windows into weird shapes and see that
# the one WITH scaling adjusts the vector directions to the new aspect ratio
# while the one WITHOUT simply keeps the arrows' angles.
plt.show()