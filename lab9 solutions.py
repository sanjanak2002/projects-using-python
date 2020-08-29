# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:46:58 2020

@author: lenovo
"""



#Q1
import random
import matplotlib.pyplot as plt
import numpy as np
print("Q1")
#1.(a)
def exp_rv(m):#defining fuction for exponential rv
    l1=[]
    for i in range(m):
        a=random.uniform(0,1000)
        b=np.exp(-a)
        l1.append(round(b,2))
    s1=sum(l1)/m
    return s1
#plotting sample mean for exponential rv
x1=[10,100,500,1000,5000,10000,50000]
y1=[exp_rv(10),exp_rv(100),exp_rv(500),exp_rv(1000),exp_rv(5000),exp_rv(10000),exp_rv(50000)] 
fig1, ax1 = plt.subplots(1)

ax1.set_xlabel("m")
ax1.set_ylabel("sample mean")
ax1.set_title("Verifying WLLN for exponential rv")
ax1.plot(x1,y1)
plt.show()


#1.(b)
def u_rv(m):#defining function for uniform rv
    l2=[]
    for i in range(m):
        a=random.uniform(1,2)
        l2.append(round(a,2))
    s2=sum(l2)/m
    return s2
#plotting sample mean for uniform distribution
x2=[10,100,500,1000,5000,10000,50000]
y2=[u_rv(10),u_rv(100),u_rv(500),u_rv(1000),u_rv(5000),u_rv(10000),u_rv(50000)]
fig2, ax2 = plt.subplots(1) 

ax2.set_xlabel("m")
ax2.set_ylabel("sample mean")
ax2.set_title("Verifying WLLN for uniform rv")
ax2.plot(x2,y2)
plt.show()

#1.(c)
def flip(p):#defining biased outcome
    return 1 if random.random() < p else 0 
def b_rv(m):#definfig function for bernoulli rv
    l3=[]
    for i in range(m):
        a=flip(0.2)
        l3.append(a)
    s3=sum(l3)/m
    return s3

#plotting sample mean for bernoulli distribution
x3=[10,100,500,1000,5000,10000,50000]
y3=[b_rv(10),b_rv(100),b_rv(500),b_rv(1000),b_rv(5000),b_rv(10000),b_rv(50000)]
fig3, ax3 = plt.subplots(1) 

ax3.set_xlabel("m")
ax3.set_ylabel("sample mean")
ax3.set_title("Verifying WLLN for bernoulli rv")
ax3.plot(x3,y3)
plt.show()

#Q2
#2.(a)
import numpy as np
from numpy.random import seed
from numpy.random import uniform
from numpy.random import randint
from numpy import mean

import matplotlib.pyplot as plt
# seed the random number generator, so that the experiment is replicable
seed(1)
# calculate the mean for n=1,2,4,8,16 and 32  10000 times
m1 = [mean(np.exp(uniform(1, 2, 1))) for _i in range(10000)]
m2 = [mean(np.exp(uniform(1, 2, 2))) for _i in range(10000)]
m3 = [mean(np.exp(uniform(1, 2, 4))) for _i in range(10000)]
m4 = [mean(np.exp(uniform(1, 2, 8))) for _i in range(10000)]
m5 = [mean(np.exp(uniform(1, 2, 16))) for _i in range(10000)]
m6 = [mean(np.exp(uniform(1, 2, 32))) for _i in range(10000)]

# plot the distribution of sample means
print("\nthe distribution of the sample mean for exponential rvs")
plt.subplot(2,3,1)
plt.title("n=1")
plt.hist(m1)
plt.subplot(2,3,2)
plt.title("n=2")
plt.hist(m2)
plt.subplot(2,3,3)
plt.title("n=4")
plt.hist(m3)
plt.subplot(2,3,4)
plt.title("n=8")
plt.hist(m4)
plt.subplot(2,3,5)
plt.title("n=16")
plt.hist(m2)
plt.subplot(2,3,6)
plt.title("n=32")
plt.hist(m2)
plt.tight_layout()
plt.show()
#Normal Distribution values for a particular range
def normal(x,n,mean,stdev):
    return 1/((2*np.pi)**0.5*stdev)*np.exp(-0.5*((x-mean)/stdev)**2)

#No. of Random Variables
no=[1,2,4,8,16,32]

#No. of Samples generated
m=10000

#Exponential Distribution
Lambda=1
mean=1/Lambda
stdev=1/Lambda
for n in no:
    values=np.zeros(m)
    for j in range(n):
        values+=np.random.exponential(1/Lambda,m)
    values/=n
    
    mn=min(values)
    mx=max(values)
    hist=np.histogram(values,bins=100,density=True)
    
    fig,ax=plt.subplots(1)
    ax.plot(normal(hist[1],n,mean,stdev/n**0.5))
    ax.bar(range(100),hist[0],width=1,color='orange')
    ax.set_xticks(np.linspace(1,100,6))
    ax.set_xticklabels(np.around(np.linspace(mn,mx,6),2))
    plt.title('Exponential Distribution')
    plt.show()
"""
#2.(b)
# seed the random number generator, so that the experiment is replicable
seed(1)
# calculate the mean for n=1,2,4,8,16 and 32  10000 times
m1 = [mean(uniform(1, 2, 1)) for _i in range(10000)]
m2 = [mean(uniform(1, 2, 2)) for _i in range(10000)]
m3 = [mean(uniform(1, 2, 4)) for _i in range(10000)]
m4 = [mean(uniform(1, 2, 8)) for _i in range(10000)]
m5 = [mean(uniform(1, 2, 16)) for _i in range(10000)]
m6 = [mean(uniform(1, 2, 32)) for _i in range(10000)]
# plot the distribution of sample means
print("")
print("the distribution of the sample mean for uniform rvs")
plt.subplot(2,3,1)
plt.title("n=1")
plt.hist(m1)
plt.subplot(2,3,2)
plt.title("n=2")
plt.hist(m2)
plt.subplot(2,3,3)
plt.title("n=4")
plt.hist(m3)
plt.subplot(2,3,4)
plt.title("n=8")
plt.hist(m4)
plt.subplot(2,3,5)
plt.title("n=16")
plt.hist(m2)
plt.subplot(2,3,6)
plt.title("n=32")
plt.hist(m2)
plt.tight_layout()
plt.show()
"""
#Uniform Distribution
a,b=1,2
mean=(a+b)/2
stdev=(b-a)/12**0.5
for n in no:
    values=np.zeros(m)
    for j in range(n):
        values+=np.random.uniform(a,b,m)
    values/=n
    
    mn=min(values)
    mx=max(values)
    hist=np.histogram(values,bins=100,density=True)
    fig,ax=plt.subplots(1)
    ax.plot(normal(hist[1],n,mean,stdev/n**0.5))
    ax.bar(range(100),hist[0],width=1,color='orange')
    ax.set_xticks(np.linspace(1,160,6))
    ax.set_xticklabels(np.around(np.linspace(mn,mx,6),2))
    plt.title('Uniform Distribution')
    plt.show()
#3.(c)
def flip(x):
    arr=[]
    for i in range(x):
        a=  numpy.random.binomial(1, .2, size=1)
        b=numpy.mean(a)
        arr.append(b)
    return arr 
   

#Bernoulli Distribution
p=0.2
mean=p
stdev=(p*(1-p))**0.5
for n in no:
    values=np.zeros(m)
    for j in range(n):
        values+=np.random.binomial(1,0.2,m)
    values/=n
    
    mn=min(values)
    mx=max(values)
    hist=np.histogram(values,bins=100,density=True)
    
    fig,ax=plt.subplots(1)
    ax.plot(normal(hist[1],n,mean,stdev/n**0.5))
    ax.bar(range(100),hist[0],width=1,color='orange')
    ax.set_xticks(np.linspace(1,100,6))
    ax.set_xticklabels(np.around(np.linspace(mn,mx,6),2))
    plt.title('Bernoulli Distribution')
    plt.show()

    




    


















