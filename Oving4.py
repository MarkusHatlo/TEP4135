# import numpy as np
# import matplotlib.pyplot as plt

# #Oppgave 1
# x = np.linspace(-2,2,101)
# y = np.linspace(-2,2,101)
# x, y = np.meshgrid(x, y)

# a_0 = 1

# U_U1 = a_0*y+(3/2*a_0)*y**2+(1-a_0/2)*y**4

# _,f = plt.subplots()
# f.plot(x,y,U_U1)
# f.set_xlabel('x-aksen')
# f.set_ylabel('y-aksen')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the equation
def U_U1(y, a_0):
    return a_0 * y - ((3 * a_0/2) - 2) * y**2 - (1 - a_0 / 2) * y**4

# Set up y values for plotting
y = np.linspace(0, 1, 100)

# Set a_0 constant (you can modify this value as needed)
a_0_values = np.array([0,1,2,2.67])

fig, axs = plt.subplots(2, 2, figsize=(5, 8))
plt.grid(True)

for i, a_0 in enumerate(a_0_values):

    # Calculate U/U1 values
    U_U1_values = U_U1(y, a_0)
    ax = axs[i // 2, i % 2]
    ax.plot(U_U1_values,y)
    ax.set_title(f'a_0 = {a_0}')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.grid(True)
    ax.set_xticks(np.arange(min(U_U1_values), max(U_U1_values), 0.35))  # Adjust interval size as needed

    # Create the plot (note: U/U1 is now on the x-axis, y is on the y-axis)
    #, label=r'$U/U_1 = a_0 y + (\frac{3 a_0}{2} - 2) y^2 + \left(1 - \frac{a_0}{2}\right) y^4$'

plt.tight_layout()
plt.show()
