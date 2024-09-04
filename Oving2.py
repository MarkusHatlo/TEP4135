import numpy as np
import matplotlib.pyplot as plt

#Oppgave 1
x_1 = np.linspace(-5,1,101)
y_1 = np.linspace(0,2,101)
x_1, y_1 = np.meshgrid(x_1, y_1)
theta_1 = np.arctan2(y_1,x_1)

psi_1 = y_1 - ((1.2/np.pi) * theta_1)

# plt.rcParams.update({'font.size': 14})
# figsize = (7, 6)

#field liner
_,f = plt.subplots()
f.contour(x_1,y_1,psi_1,levels=20, colors ='k')
f.set_xlabel('x-aksen')
f.set_ylabel('y-aksen')
plt.show()