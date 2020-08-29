# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:43:43 2020

@author: lenovo
"""

#created by Sanjana K, b19139

import pandas as pd
import matplotlib.pyplot as plt

# defining a function to Calculate the Expectation of pmf
# E(x) =sum(x*P(x))
def expectation(e): 
    c=0
    for i in e:
        c+=(i*e[i])
    return c

# defining a function to Calculate the  Variance of given data
# var(x) = E(x^2)-E(x)
def var(e,m):
    c=0
    for i in e:
        c+=(i*i*e[i])
    c-=(m*m)
    return c

# defining a function to sort the dictionary and update it with the required  probabilities
def sorting_dict(e,t):
    l=list(e.items())
    l.sort()
    e=dict(l)
    for i in e:
        e[i]/=t
    return e

# defining a function to plot the PMF of given data
def plotting(dt,case,m,v):
    fig=plt.figure()
    a=dt.keys()
    b=dt.values()
    plt.bar(a,b, align='center', alpha=1)
    if(case[0]=='A'):
        plt.xlabel("Age")
    else:
        plt.xlabel("No. of days")
    plt.ylabel("Probability")
    q=case
    plt.title(q)
    plt.show()
    print("Expectation (E(x))=",m)
    print("Variance (var(x)) =",v)
 
# Q1
df=pd.read_excel(r'C:\Users\lenovo\Desktop\Sanjana\IC-252\Covid19IndiaData_Q1.xlsx')
x=df['Age'].values
y=df['StatusCode'].values
z=df['GenderCode0F1M'].values

#empty dictionary for no. of recovered patients
r={}
#empty dictionary for no. of hospitalized
h={}
#empty dictionary for no. of dead
d={}
#empty dictionary for all patients
dn={}
#empty dictionary for no. of male patients
m={}
#empty dictionary for no. of female patients
f={}

# the respective count for the empty dictionaries created above
ad=0
bh=0
cr=0
am=0
bf=0

for n in range(0,1315):
    i=x[n]
    j=y[n]
    k=z[n]
    if i in dn:
        dn[i]+=1
    else:
        dn[i]=1
    if(j=="Dead"):
        ad+=1
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    elif(j=="Hospitalized"):
        bh+=1
        if i in h:
            h[i]+=1
        else:
            h[i]=1
    else:
        cr+=1
        if i in r:
            r[i]+=1
        else:
            r[i]=1
    if(k==0):
        bf+=1
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    else:
        am+=1
        if i in m:
            m[i]+=1
        else:
            m[i]=1

#pmf, expectation and variance for all
dn=sorting_dict(dn,1315)
dne=expectation(dn)
dnv=var(dn,dne)

#pmf, expectation and variance for recovered
r=sorting_dict(r,cr)
re=expectation(r)
rv=var(r,re)

#pmf, expectation and variance for hospitalized
h=sorting_dict(h,bh)
he=expectation(h)
hv=var(h,he)

#pmf, expectation and variance for dead
d=sorting_dict(d,ad)
de=expectation(d)
dv=var(d,de)

#pmf, expectation and variance for male
m=sorting_dict(m,am)
me=expectation(m)
mv=var(m,me)

#pmf, expectation and variance for female
f=sorting_dict(f,bf)
fe=expectation(f)
fv=var(f,fe)

# Q1 (a)
print("")
print("Q1 (a) PMF of Patients (Age wise)",dn)
plotting(dn,"Age vs No. of cases for all patients",dne,dnv)
print("As variance is large, we can say that the data is spread out i.e. covid is present in a lot of age groups")

# Q1 (b)
print("")
print("Q1 (b)(i) PMF of Recovered Patients (Age wise)",r)
plotting(r,"Age vs No. of cases for Recovered patients",re,rv)
print("Q1 (b)(ii) PMF of Dead Patients (Age wise)")
plotting(d,"Age vs No. of cases for Dead patients",de,dv)
print("Therefore it can be said that the chances of death due to Covid-19 increases with age and people with less age have more chances to be recovered")

# Q1 (c)
print("")
print("Q1 (c)(i) PMF of Male Patients (Age wise)",m)
plotting(m,"Age vs No. of cases for Male patients",me,mv)
print("Q1 (c)(ii) PMF of Female Patients (Age wise)",f)
plotting(f,"Age vs No. of cases for Female patients",fe,fv)
print("With expected age of male and female patients almost similar but variances different, we can conclude that in the case of males, covid is spread out to many age group in enough amounts, while for females, covid is more concentrated at women aged 38-39")

# Q2 (a)
d1=pd.read_excel(r"C:\Users\lenovo\Desktop\Sanjana\IC-252\Incubation_IncludingWR.xlsx")
x1=d1['Incubation Period'].values

#incubation period-including wuhan residents
ip1={}
inc1=0


for i in x1:
    inc1+=1
    if i in ip1:
        ip1[i]+=1
    else:
        ip1[i]=1

#pmf, expectation and variance for incubation period inluding wuhan residents
ip1=sorting_dict(ip1,inc1)
ip1m=expectation(ip1)
ip1v=var(ip1,ip1m)

print("")
print("Q2 (a) PMF of the all patients (including Wuhan Residents)")
# Only Travel to Wuhan, Contact with case, Contact with Wuhan resident and Lives-works-studies in Wuhan cases are considered for plotting this graph and calculation of the Incubation Period
# For Lives-works-studies in Wuhan, those whose ExposurL was not given, is assumed as 01-12-2019 i.e. the reporting date of first covid patient
plotting(ip1,"Incubation Period Graph for all the patients",ip1m,ip1v)

# Q2 (b)
d2=pd.read_excel(r"C:\Users\lenovo\Desktop\Sanjana\IC-252\Incubation_ExcludingWR.xlsx")
x2=d2['Incubation Period'].values

#incubation period-excluding wuhan residents
ip2={}
inc2=0


for i in x2:
    inc2+=1
    if i in ip2:
        ip2[i]+=1
    else:
        ip2[i]=1

#pmf, expectation and variance for incubation period excluding wuhan residents
ip2=sorting_dict(ip2,inc2)
ip2m=expectation(ip2)
ip2v=var(ip2,ip2m)

print("")
print("Q2 (b) PMF of the patients excluding Wuhan Residents")
#Note: Only Travel to Wuhan, Contact with case, Contact with Wuhan residens are considered for plotting this graph and calculation of the Incubation Period
plotting(ip2,"Incubation Period Graph for patients Excluding Wuhan Residents",ip2m,ip2v)
print("There is a large difference between the Incubation Period in both cases which shows that Wuhan residents were exposed to the virus a long time before and thus it could have been controlled way back if the matter was dealt seriously")

# Q2 (c)
# (Part 1)
d3=pd.read_excel(r"C:\Users\lenovo\Desktop\Sanjana\IC-252\Onset_Hospitalisation_Death.xlsx")
x3=d3['H-O'].values
x4=d3['X-O'].values
x5=d3['X-H'].values

ip3={}
inc3=0
for i in x3:
    inc3+=1
    if i in ip3:
        ip3[i]+=1
    else:
        ip3[i]=1

ip4={}        
inc4=0
for i in x4:
    inc4+=1
    if i in ip4:
        ip4[i]+=1
    else:
        ip4[i]=1
 
ip5={}
inc5=0       
for i in x5:
    inc5+=1
    if i in ip5:
        ip5[i]+=1
    else:
        ip5[i]=1

#PMF of the onset to hospitalization (O-H) of dead patients
ip3=sorting_dict(ip3,inc3)
ip3m=expectation(ip3)
ip3v=var(ip3,ip3m)

print("")
print("Q2 (c) (i) PMF of the onset to hospitalization (O-H) of dead ptients")
plotting(ip3,"PMF of the onset to hospitalization (O-H) of dead patients",ip3m,ip3v)

#PMF of the onset to death (O-X) of the patients
ip4=sorting_dict(ip4,inc4)
ip4m=expectation(ip4)
ip4v=var(ip4,ip4m)

print("")
print("Q2 (c) (ii) PMF of the onset to death (O-X) of the patients")
plotting(ip4,"PMF of the onset to death (O-X) of the patients",ip4m,ip4v)

#PMF of the hospitalization to death (H-X) of the Patients
ip5=sorting_dict(ip5,inc5)
ip5m=expectation(ip5)
ip5v=var(ip5,ip5m)

print("")
print("Q2 (c) (iii) PMF of the hospitalization to death (H-X) of the patients")
plotting(ip5,"PMF of the hospitalization to death (H-X) of the Patients",ip5m,ip5v)
print("The three graphs are quite similar and it can be said that, more the days it took for the patients to visit the hospital, their chance of surviving became less")

# (Part 2)
d6=pd.read_excel(r"C:\Users\lenovo\Desktop\Sanjana\IC-252\H-O_All_Patients.xlsx")
x6=d6['H-O'].values

ip6={}
inc6=0


for i in x6:
    inc6+=1
    if i in ip6:
        ip6[i]+=1
    else:
        ip6[i]=1

#PMF of the onset to hospitalization (O-H) of the survived patients
ip6=sorting_dict(ip6,inc6)
ip6m=expectation(ip6)
ip6v=var(ip6,ip6m)

print("")
print("Q2 (c) (iv) PMF of the onset to hospitalization (O-H) of the survived patients")
# All the cases of survived patients have been included in this plot
plotting(ip6,"PMF of the onset to hospitalization (O-H) of the survived patients",ip6m,ip6v)
print("It is clear by the plot that the sooner the sooner the patient was reported to the hospital, more became his chances of surviving")