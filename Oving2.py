import numpy as np
import matplotlib.pyplot as plt

#Oppgave 1
x_1 = np.linspace(-5,1,101)
y_1 = np.linspace(-0.5,2,101)
x_1, y_1 = np.meshgrid(x_1, y_1)
theta_1 = np.arctan2(y_1,x_1)
r_1 = np.sqrt(x_1**2+y_1**2)

psi_1 = y_1 - ((1.2/np.pi) * theta_1)

#field liner
_,f = plt.subplots()
f.contour(x_1,y_1,psi_1,levels=20, colors ='k')
f.set_xlabel('x-aksen')
f.set_ylabel('y-aksen')

f.axhline(y=0, color='r', linewidth=3)
f.plot(1.2/np.pi, 0, 'bo', markersize=8)

plt.show()