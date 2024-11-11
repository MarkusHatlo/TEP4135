import numpy as np
import matplotlib.pyplot as plt

normal_p = np.loadtxt('C:/Users/marha/Documents/Skole/TEP4135/viskose/normal_p.xy')
normal_p_1 = np.loadtxt('C:/Users/marha/Documents/Skole/TEP4135/viskose/normal_p_1.xy')
normal_to_wedge_p = np.loadtxt('C:/Users/marha/Documents/Skole/TEP4135/viskose/normal_to_wedge_p.xy')
normal_to_wedge_p_1 = np.loadtxt('C:/Users/marha/Documents/Skole/TEP4135/viskose/normal_to_wedge_p_1.xy')
normal_to_wedge_U = np.loadtxt('C:/Users/marha/Documents/Skole/TEP4135/viskose/normal_to_wedge_U.xy')
normal_to_wedge_U_1 = np.loadtxt('C:/Users/marha/Documents/Skole/TEP4135/viskose/normal_to_wedge_U_1.xy')
normal_U = np.loadtxt('C:/Users/marha/Documents/Skole/TEP4135/viskose/normal_U.xy')
normal_U_1 = np.loadtxt('C:/Users/marha/Documents/Skole/TEP4135/viskose/normal_U_1.xy')




x_values = []
y_values = []
u_values = []
v_values = []

def dele(importListe):

    x_values = []
    y_values = []
    u_values = []
    v_values = []

    for list in importListe:
        for i_no, i in enumerate(list):
            if i_no == 0:
                x_values.append(float(i))
            elif i_no == 1:
                y_values.append(float(i))
            elif i_no == 3:
                u_values.append(float(i))
            elif i_no == 4:
                v_values.append(float(i))
    return x_values, y_values, u_values, v_values

x_u, y_u, u, v = dele(normal_to_wedge_U)
x_p, y_p, p, k = dele(normal_to_wedge_p)

#U, V = np.meshgrid(u,v)
#x, y = np.meshgrid(x,y)

plt.plot(x_p,p)
plt.xlabel('u')
plt.ylabel('y')
plt.grid()
plt.show()