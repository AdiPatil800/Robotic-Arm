import math
import numpy as np
from numpy import pi, sin, cos, sqrt, absolute, arccos, arctan, sign
import matplotlib.pyplot as plt
import matplotlib.animation as animation

l1 = 1.2
l2 = 1.6

x1 = 0
y1 = 0

# for i in range(35):
#     print(x2[i],y2[i])
ct = 1

for i in range(23):
    x2 = l1*math.cos((math.pi*i*1.5454545454)/180)
    y2 = l1*math.sin((math.pi*i*1.5454545454)/180)
    x3 = x2+l2*math.cos(((math.pi*i)+(math.pi*i*1.5454545454))/180)
    y3 = y2+l2*math.sin(((math.pi*i)+(math.pi*i*1.5454545454))/180)
    plt.figure()
    plt.plot([x1, x2], [y1, y2])
    plt.plot([x2, x3], [y2, y3])
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(0, 5.0)
    plt.ylim(0, 5.0)
    plt.title('2dof arm')
    name = str(ct)+'.png'
    plt.savefig(name)
    ct = ct+1
