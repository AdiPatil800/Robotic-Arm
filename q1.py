import math
l1=float(input("Link length 1 : "))
l2=float(input("Link length 2 : "))
theta1=math.pi/(180/float(input("Theta 1 : ")))
theta2=math.pi/(180/float(input("Theta 2 : ")))
x=l1*math.cos(theta1) + l2*math.cos(theta1+theta2)
y=l1*math.sin(theta1) + l2*math.sin(theta1+theta2)
print("x =",x,"y =",y)