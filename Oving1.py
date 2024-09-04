import numpy as np
import matplotlib.pyplot as plt

# T = np.array([1,2,3,4,5])

# f = plt.figure(1)
# plt.plot(T,T**2)
# plt.xlabel('T')
# plt.ylabel('T**2')
# plt.show()

# x, y = np.meshgrid(np.arange(2, 7.5, 0.5),
#                    np.arange(2,7.5,0.5))

# u = x**2+y**3
# v = x**3+y**2

# f = plt.figure(2)
# Q = plt.quiver(x, y, u, v)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

A = 1
x = np.linspace(-10,10,101)
y = np.linspace(-10,10,101)
X, Y = np.meshgrid(x, y)

psi = X*Y
phi = 1/2*(X**2-Y**2)

u = A*X
v = -Y*A
u_magnitude = np.sqrt(u**2 + v**2)

plt.rcParams.update({'font.size': 14})
figsize = (7, 6)

#field liner
_,f = plt.subplots(figsize=figsize)
f.contour(X,Y,psi,levels=30, colors ='k')
f.contour(X,Y,phi,levels=10, colors ='r')
f.set_xlabel('x-aksen')
f.set_ylabel('y-aksen')
plt.show()

# #gradient
fig2,ax2 = plt.subplots(figsize=figsize)
cbar = ax2.contourf(X,Y,u_magnitude, levels=10)
fig2.colorbar(cbar, ax=ax2, label='U m/s')
ax2.set_title('Plot of velocity magnitude')
ax2.set_aspect('equal') # Ensures figure is not stretched
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()


# #vektorfelt
__, ax3 = plt.subplots(figsize=figsize)
skip = 5 # Number of vector grid points to skip during plotting
ax3.quiver(X[::skip, ::skip], Y[::skip, ::skip],
           u[::skip, ::skip], v[::skip, ::skip]
)
ax3.set_title('Plot of velocity vectors')
ax3.set_aspect('equal') # Ensures figure is not stretched
ax3.set_xlabel('x')
ax3.set_ylabel('y')
plt.show()

