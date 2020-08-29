# -*- coding: utf-8 -*-
"""
@author: Sanjana

"""
#Q1
import random
import math
import numpy as np

def PiValue(n):
    # number of points inside the circle
    inside_circle = 0
    # number of points inside the square
    inside_square = 0
    # Iterate for the number of points
    for i in range(0, n):
        # Generate random x, y in [-1,1).
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        # Increment if inside unit circle.
        if round(x,3)**2 + round(y,3)**2 <= 1.0:
            inside_circle += 1
    # inside / total = pi / 4
    pi = (inside_circle / n) * 4
    return pi
print("Q1")
print("the value of pi for sample size=100 is ",PiValue(100))
print("the value of pi for sample size=1000 is ",PiValue(1000))
print("the value of pi for sample size=10000 is ",PiValue(10000))

#Q2
def get_rand_number(min_value, max_value):
    range = max_value - min_value
    choice = random.uniform(0,1)
    return round(min_value + range*choice,3)

def f_of_x(x):
    return (2/(1+ x**2))

def monte_carlo(num_samples):
    
    sum_of_samples = 0
    for i in range(num_samples):
        x = get_rand_number(0,1)
        sum_of_samples += f_of_x(x)
    
    return (1) * float(sum_of_samples/num_samples)

print("\nQ2")
print("the value of integral for sample size=100 is",round(monte_carlo(100),5))
print("the value of integral for sample size=1000 is",round(monte_carlo(1000),5))
print("the value of integral for sample size=10000 is",round(monte_carlo(10000),5))

#Q3
def sample(n):
    l=[1,2,3,4,5,6,7,8,9,10]
    c=0
    for i in range(0,n):
       random.shuffle(l)
       flag=1
       for i in range(10):
           if(l[i]==i+1):
               flag=0
               break
       if(flag==1):
           c+=1
    return round(n/c,5)

print("\nQ3")
print("the value of e when sample size= 1000 is ",sample(1000))   
print("the value of e when sample size= 3000 is ",sample(3000))  
print("the value of e when sample size= 5000 is ",sample(5000))  
print("the value of e when sample size= 10000 is ",sample(10000))  

print("\n In all three questions we have used the monte carlo approximation and prved that by increasing the sample size, we get closer to the desired outcome")        
    



















