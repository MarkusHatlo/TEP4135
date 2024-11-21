import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,6,50)
y = np.linspace(0,3,50)
(x,y) = np.meshgrid(x,y)

k_0 = 2
q = 1
d = 1


k = 1.1*k_0
phi = q/(2*np.pi)*(np.arctan2(y,(x-d)) - k*np.arctan2(y,x) + np.arctan2(y,(x+d)))

levels = np.logspace(-4,0,20)
levels = np.insert(levels,0,[0.0])

_,f1 = plt.subplots()
f1.contour(x,y,phi,levels, color="black")
plt.show()
