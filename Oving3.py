import numpy as np
import matplotlib.pyplot as plt

x_1 = np.linspace(-4,4,101)
y_1 = np.linspace(-4,4,101)
x_1, y_1 = np.meshgrid(x_1, y_1)
theta_1 = (np.arctan2(y_1,x_1) + 2*np.pi) % (2*np.pi)
r_1 = np.sqrt(x_1**2+y_1**2)

A = 1
alpha_values = np.array([3, 2, 3/2, 2/3, 1/2])

fig, axs = plt.subplots(2, 3, figsize=(12, 8))

for i, alpha in enumerate(alpha_values):
    psi_1 = A * r_1**alpha * np.sin(alpha * theta_1)
    ax = axs[i // 3, i % 3]
    ax.contour(x_1, y_1, psi_1, levels=20, colors='k')
    ax.set_title(f'alpha = {alpha}')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')

# Hide the empty subplot (6th subplot)
fig.delaxes(axs[1, 2])

plt.tight_layout()
plt.show()