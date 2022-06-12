import math as m
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
from matplotlib.animation import FuncAnimation

x_data = [0, 1.152, -1.6]
y_data = [0, -0.336, 1.2]
fig, ax = plt.subplots()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
line, = ax.plot(-1, 1)
plt.grid(axis='both')


def inverse_kinematics(positionx, positiony):
    l1 = 1.2
    l2 = 1.6
    x = positionx
    y = positiony
    rsquared = x**2 + y**2
    r = m.sqrt(rsquared)
    if x < 0:
        theta2 = m.acos(-(l1**2 + l2**2 - rsquared)/(2*l1*l2))
        theta1 = m.atan(y/x) - m.atan((l2*m.sin(theta2)/(l1+l2*m.cos(theta2))))
        x1 = -l1*m.cos(theta1)
        y1 = -l1*m.sin(theta1)
        x2 = -(l1*m.cos(theta1) + l2*m.cos(theta1+theta2))
        y2 = -(l1*m.sin(theta1) + l2*m.sin(theta1+theta2))

    else:
        theta2 = m.acos(-(l1**2 + l2**2 - rsquared)/(2*l1*l2))
        if x == 0:
            theta1 = m.pi/2 - m.atan((l2*m.sin(theta2)/(l1+l2*m.cos(theta2))))
        else:
            theta1 = m.atan(y/x) - \
                m.atan((l2*m.sin(theta2)/(l1+l2*m.cos(theta2))))
        x1 = l1*m.cos(theta1)
        y1 = l1*m.sin(theta1)
        x2 = l1*m.cos(theta1) + l2*m.cos(theta1+theta2)
        y2 = l1*m.sin(theta1) + l2*m.sin(theta1+theta2)
    print("Theta1 , Theta2 : ", theta1, theta2)
    print("x , y           : ", x2, y2)
    return x1, y1, x2, y2


def swing(i):
    if i <= 320:
        xf = -1.6+(1.6/320)*i
        yf = (-(1/1.6)*xf*xf)+2.8
    elif (i > 320 and i <= 640):
        xf = (i/200)-1.6
        yf = (-(1/1.6)*xf*xf)+2.8
    elif (i > 640 and i <= 720):
        xf = 1.6-(1.6/80)*(i-640)
        yf = 1.2
    else:
        xf = -(1.6/80)*(i-720)
        yf = 1.2
    x1, y1, x2, y2 = inverse_kinematics(xf, yf)
    x_data.pop(1)
    y_data.pop(1)
    x_data.insert(1, x1)
    y_data.insert(1, y1)
    x_data.pop(2)
    y_data.pop(2)
    x_data.insert(2, x2)
    y_data.insert(2, y2)
    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,


animation = FuncAnimation(fig, func=swing, frames=800, interval=10.0)
plt.show()

