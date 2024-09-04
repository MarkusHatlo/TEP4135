# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:32:45 2020

@author: Stefan Weichert
"""

#import libraries
import numpy as np                  # math functionality
import matplotlib.pyplot  as plt    # plotting

# create vector of x values
x = np.linspace(-3,4,40)
# calculate y-values (two sets)
y = x**2 - 5
y2 =(x-1)**2 - 1
# do the plotting
plt.figure(1)                               # make figure
plt.clf()                                   # clear figure
plt.plot(x,y,label='plot number 1')         # plot one (regular)
plt.scatter(x,y2,label = 'plot number 2')   # plot the other (scatter)
plt.xlabel('position x [m]')
plt.legend()  # display the legend
plt.show() # show the figure window (not always necessary)
