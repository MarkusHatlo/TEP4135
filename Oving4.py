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
a_0 = 0

# Calculate U/U1 values
U_U1_values = U_U1(y, a_0)

# Create the plot (note: U/U1 is now on the x-axis, y is on the y-axis)
plt.figure(figsize=(8, 6))
plt.plot(U_U1_values, y, label=r'$U/U_1 = a_0 y + (\frac{3 a_0}{2} - 2) y^2 + \left(1 - \frac{a_0}{2}\right) y^4$')

# Add labels and title
plt.xlabel(r'$U/U_1$')
plt.ylabel('y')
plt.title('Plot of $y$ as a function of $U/U_1$')
plt.legend()

# Show the grid and the plot
plt.grid(True)
plt.show()
