# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:19:02 2020

@author: Stefan Weichert
"""

import numpy as np
import matplotlib.pyplot as plt

# Set parameters
a = 0.6;
b = 0.5;
c = 0.2;

# define functions
def u(x,y):
    return a**2-(b-c*x)**2
def v(x,y):
    return -2*c*b*y+c*c*x*y*2

# create data (grid)
xmin = -2
xmax = +8
ymin = -2
ymax = +2    
x = np.linspace(xmin,xmax,14)
y = np.linspace(ymin,ymax,15)

[X,Y] = np.meshgrid(x,y)

#calculate velocity field
U = u(X,Y)
V = v(X,Y)

plt.figure(1)
plt.clf()
plt.quiver(X,Y,U,V,       angles='xy', scale_units='xy')

# Contour plot (f some arbitrary scalar function)
def total_speed(u,v):
    return np.sqrt(u**2+v**2)

Total = total_speed(U,V)

plt.figure(2)
plt.clf()
plt.contourf(X,Y,Total,20)# 20 is the number of countours
   #contour  without the "f" does not fill between contours 

# 3D plot
from mpl_toolkits.mplot3d  import Axes3D

# fig3 = plt.figure(3)
# plt.clf()
# ax3_1 = fig3.gca(projection = "3d") #prepare for 3D
# ax3_1.plot_surface(X,Y,Total)       #3D surface plot 
# ax3_1.view_init(90, -10)            #set view-angles
plt.show()
