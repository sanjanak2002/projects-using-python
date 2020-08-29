# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:11:03 2020
lab 5 assignment solutions
@author: Sanjana K (b19139)
"""

#Q1)a)
#importing the required libraries
import random
import matplotlib.pyplot as plt
import numpy as np

#creating an empty list to collect the values of Y
l=[]                 
#creating random numbers with given probability
choices=[0,1]
weight1=[0.75,0.25]
weight2=[0.35,0.65]

#iterating 10000 times
for i in range(10000):
    a=random.randint(0,1)         #here, a is the value of X
    if a==0:
        b1= np.random.choice(choices,p=weight1)
    else:
        b2= np.random.choice(choices,p=weight2)    
    l.append(b1)
    l.append(b2)
y0=l.count(0)                   #counting no. of zeros
y1=l.count(1)                   #counting no. of ones

#plotting graph for P(Y=0) and P(Y=1)
x=('0','1')
y=(y0/10000,y1/10000)
plt.bar(x,y)
plt.show()    

#Q1)b)
#verifying calculated and simulated output
#from the given formula,
#P(Y = 0) = P(Y = 0|X = 0)P(X = 0) + P(Y = 0|X = 1)P(X = 1), 
#P(Y = 1) = P(Y = 1|X = 0)P(X = 0) + P(Y = 1|X = 1)P(X = 1)
#we obtain P(Y=0)=0.55 and P(Y=1)=0.45
print('the calculated output P(Y=0) is 0.55 and simulated output is',y0/20000)
print('the calculated output P(Y=1) is 0.45 and simulated output is',y1/20000)

#Q2)a)
#importing the required libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import random

style.use('ggplot')

#defining empty list to collect the input signal x
l1=[]
#iterating 10000 times
for i in range(10000):
    a=random.randint(0,1)        #here a is the value of X
    l1.append(a)
#for X    
x1=l1.count(1)
x0=l1.count(0)
p_x0=x0/10000
p_x1=x1/10000


#the same steps as above for Y
#defining empty list to collect the output signal y
l2=[]
choices=[0,1]                   #to obtain random no. with given probability
weight1=[0.75,0.25]
weight2=[0.35,0.65]
for i in range(10000):
    a=random.randint(0,1)    
    if a==0:
        b1= np.random.choice(choices,p=weight1)
    else:
        b2= np.random.choice(choices,p=weight2)    
    l2.append(b1)
    l2.append(b2)

y1=l2.count(1)                    #counting no. of ones
y0=l2.count(0)                    #counting no. of zeros
p_y0=y0/20000
p_y1=y1/20000

#the values of the joint probability entities 
a1=0.75/p_y0
a2=0.25/p_y1
a3=0.35/p_y0
a4=0.65/p_y1
#plotting 3D bar graph of joint probability distribution
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x=[-0.1,-0.1,0.9,0.9]
y=[-0.1,0.9,-0.1,0.9]
z=np.zeros(4)

dx=[.2,.2,.2,.2]
dy=[.2,.2,.2,.2]
dz=[a1,a2,a3,a4]
ax.bar3d(x, y, z, dx, dy, dz)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

#Q2)b)
#verifyng theoritical and simulated outputs
#using P(Y = y|X = x) = P(X = x,Y = y).P(X = x),
#we obtain P(X=0,Y=0)=1.36,
#P(X=0,Y=1)=0.55,
#P(X=1,Y=0)=0.63,
#P(X=1,Y=1)=1.44
print('theoritical P(X=0,Y=0)=1.36 and simulated output is',a1)
print('theoritical P(X=0,Y=1)=0.55 and simulated output is',a2)
print('theoritical P(X=1,Y=0)=0.63 and simulated output is',a3)
print('theoritical P(X=1,Y=1)=1.44 and simulated output is',a4)

#the end






























