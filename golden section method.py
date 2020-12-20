# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 07:03:31 2020

@author: Görkem

golden section method
"""
import pandas as pd


a=1.5
b=2
eps = 0.05

def function(x):
    function = (x**4)+(8*x**3)-(6*x**2)-(72*x)
    return function

#-------------------------

ai = []
bi = []
Ei = []
x1 = []
x2 = []
fx1 = []
fx2 = []
Note = []

#-------------------------

ai.append(a)
bi.append(b)

i=0
while True:
    x1.append(ai[i] + (0.381566011*(bi[i]-ai[i])))
    x2.append(ai[i] + (0.618033589*(bi[i]-ai[i])))
    fx1.append(function(x1[i]))
    fx2.append(function(x2[i]))
   
    if fx1[i] < fx2[i]:
        bi.append(x2[i])
        ai.append(ai[i])
        Note.append("new b = x2")
        Ei.append(x2[i]-ai[i])
        if (x2[i]-ai[i]) < eps:
            break
    else:
        ai.append(x1[i])       
        bi.append(bi[i])      
        Note.append("new a = x1")   
        Ei.append(bi[i]-x1[i])     
        if (bi[i]-x1[i]) < eps:
            break
    
    i+=1



ai.pop()
bi.pop()

df = pd.DataFrame({'ai': ai, 
                    'bi': bi, 
                    'Ei': Ei,
                    'x1': x1,
                    'x2': x2,
                    'F(x1)': fx1,
                    'F(x2)': fx2,
                    'Note' : Note}) 

print(df)