import numpy as np
import matplotlib.pyplot as plt

beta_test = 10*2*np.pi/60
beta = np.linspace(0,np.pi/2,90)
Mach_test = 2
Mach = [1.2,1.4,1.6,1.8,2,2.2,2.4,2.6,2.8,3,3.5,4,5,100]
gamma = 1.4

def cot(vinkel):
    return 1/np.tan(vinkel)

def theta(b,m): 
    theta_vinkel = np.arctan((2*cot(b)*(m**2*np.sin(b)**2-1))/(m**2*(gamma + np.cos(2*b)+2)))
    return theta_vinkel

for i in Mach:
    theta_value = theta(beta,i)

    positive_mask = theta_value >= 0
    
    beta_positive = beta[positive_mask]
    theta_positive = theta_value[positive_mask]

    plt.plot(np.degrees(beta_positive), np.degrees(theta_positive),label=f'Mach {i:.1f}')

    midpoint_index = len(beta_positive) // 2

    plt.text(np.degrees(beta_positive[midpoint_index]), np.degrees(theta_positive[midpoint_index]), f'{i:.1f}', fontsize=10, color='black')    

plt.xlabel('Beta (degrees)')
plt.ylabel('Theta (degrees)')
plt.xticks(np.arange(0, 90, 20))
plt.yticks(np.arange(0, 30, 10))

plt.grid()
plt.show()

#Verdiene er litt lave, men det er sikkert en feil i funksjonen