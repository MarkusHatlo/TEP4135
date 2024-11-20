import numpy as np

S_0 = 0.02
n = 0.0145
A = 0.39
Pe = 1.57
Rh = 0.346
tol = 0.001
test = 1
y_t = 0.28

print('Start')
A_new = A + 0.1*y_t
Pe_new = Pe + y_t*2*0.1
Q = A_new*(1/n)*(A_new/Pe_new)**(2/3)*S_0**(1/2)

print(f'Dette er Q = {Q}')
print(f'Dette er y = {y_t}')

# while test > tol:
#     A_new = A + 0.1*y
#     Pe_new = Pe + y*2*0.1
#     Q = A_new*(1/n)*(A_new/Pe_new)**(2/3)*S_0**(1/3)
#     y += 1
#     test = abs(Q-3)

# for y in range(100):
#     A_new = A + 0.1*y
#     Pe_new = Pe + y*2*0.1
#     Q = A_new*(1/n)*(A_new/Pe_new)**(2/3)*S_0**(1/3)
#     test = abs(Q-3)
#     if test < tol:
#         svar = Q
#         print(f'Dette er Q = {svar}')
#         print(f'Dette er y = {y}')
