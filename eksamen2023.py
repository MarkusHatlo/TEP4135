import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def derivering():
    x,y,q,u = sp.symbols('x y q u')
    return sp.diff(q/(2*sp.pi)*sp.atan(y/x), y)

#print(derivering())

def interering(yn):
    b = 4
    n = 0.012
    So = 0.05
    return  b*yn*1/n*((b*yn)/(b+2*yn))**(2/3)*So**(1/2)

#print(interering(0.345))


x = np.linspace(-0.3,0.3,101)
y = np.linspace(-0.3,0.3,101)

x, y = np.meshgrid(x, y)

u = 1
q = np.pi/10*u

phi = u*y + q/(2*np.pi)*np.arctan2(y,x)

_,f1 = plt.subplots()
print(x)
f1.contour(x,y,phi,levels = 20, colors ='blue')
f1.contour(x,y,phi,levels = [-0.1,0.1], colors ='black')
plt.show()