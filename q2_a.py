import numpy as np
import math

a1 = 1.2
a2 = 1.6
alpha1 = 0
alpha2 = 0
d1 = 0
d2 = 0
theta1 = 34
theta2 = 22
A1 = [[math.cos(theta1), -math.sin(theta1)*math.cos(alpha1), math.sin(theta1)*math.sin(alpha1), a1*math.cos(theta1)],
      [math.sin(theta1), math.cos(theta1)*math.cos(alpha1), -
       math.cos(theta1)*math.sin(alpha1), a1*math.sin(theta1)],
      [0, math.sin(alpha1), math.cos(alpha1), d1],
      [0, 0, 0, 1]]
A2 = [[math.cos(theta2), -math.sin(theta2)*math.cos(alpha2), math.sin(theta2)*math.sin(alpha2), a2*math.cos(theta2)],
      [math.sin(theta2), math.cos(theta2)*math.cos(alpha2), -
      math.cos(theta2)*math.sin(alpha2), a2*math.sin(theta2)],
      [0, math.sin(alpha2), math.cos(alpha2), d2],
      [0, 0, 0, 1]]
T1 = A1
T2 = np.dot(A1, A2)
x = T2[0][3]
y = T2[1][3]
print(x, y)
