# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:22:56 2020

@author: lenovo
"""
'''
pd.Series(map(lambda x: dict(yes=1, no=0)[x],
              sample.housing.values.tolist()), sample.index)
'''

#Q1
import math
import numpy as np
import matplotlib.pyplot as plt

#function for pdf
def pdf(x):
    pdf=lamb*math.e**(-lamb*x)
    return pdf
 
#function for cdf    
def cdf(x):
    cdf=1-math.e**(-lamb*x)
    return cdf

lamb=57

X= np.linspace(0.04,1,100)
Y= [pdf(x) for x in X]

plt.title(" probability density function of the wait time for the next Covid-19 confirmed case")
plt.xlabel("wait time in hours")
plt.ylabel("probability density")

print("Q1)A.")
plt.plot(X,Y)
plt.show()

time=1/60
print("Q1)B.")
print("the probability of the wait time for the next Covid-19 confirmed case to be less than or equal to 1 minute",cdf(time))

time2=2/60
print("Q1)C.")
print("the probability of the wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes",cdf(time2)-cdf(time))

print("Q1)D.")
print("the probability of the wait time for the next Covid-19 confirmed case to be more than 2 minutes",1-cdf(time2))

lamb*=0.5
print("Q1)E.")
print("when the average number of cases per hour doubled",cdf(time2)-cdf(time))    



#Q2
import math
import pandas as pd
# assigning values to different Status and reading file using panda library
file_handler = open("IC252_Lab8.csv", "r")

df=pd.read_csv(file_handler, sep = ",")

file_handler.close()

Status = {'Hospitalized': 1,'Recovered': 2, 'Dead':3}

df.Status = [Status[item] for item in df.Status] 


stat=df['Status'].values
pop=df['Population'].values
sr=df['SexRatio'].values
lit=df['Literacy'].values
age=df['Age'].values
st=df['SmellTrend'].values
gen=df['Gender'].values


#defining a function for standard deviation 
def SD(l):
    c=0
    for i in l:
        c=c+i
    e=c/2310
    var=0
    for j in l:
        var= var+ (j-e)**2
    sd=math.sqrt(var/2309)
    return sd

#defining function for covariance
def cov(l1,l2):
    c1=0
    c2=0
    for i in l1:
        c1+=i
    e1=c1/2310    
    for j in l2:
        c2+=j
    e2=c2/2310
    c3=0
    for i,j in zip(range(len(l1)),range(len(l2))):
        c3=c3+ (l1[i]-e1)*(l2[j]-e2)
    covariance=c3/2309
    return covariance
#defining function to find Pearson's correlation coefficient 'r'
def result(l1,l2):
    corr=cov(l1,l2)/(SD(l1)*SD(l2))
    return corr
print('Q2)B.')
print("a. Correlation between Status and Population is",result(stat,pop))
print("b. Correlation between Status and SexRatio is",result(stat,sr))
print("c. Correlation between Status and Literacy is",result(stat,lit))
print("d. Correlation between Status and Age is",result(stat,age))
print("e. Correlation between Status and SmellTrend is",result(stat,st))
print("f. Correlation between Status and Gender is",result(stat,gen))
print("")
l=[result(stat,pop), result(stat,sr), result(stat,lit), result(stat,age), result(stat,st), result(stat,gen)]
l.sort(reverse = True)

print('Q2)C.')
print("The correlation from highest to lowest is",l)















