# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:55:14 2020

@author: Görkem

section method
"""
import pandas as pd


a=0
b=1
eps = 0.1

def function(x):
    function = (x**4)+(8*x**3)-(6*x**2)-(72*x)
    return function

#-------------------------

Fxi = []
xi = []

#-------------------------


step = (b-a)/eps
counter = (b-a)/step

for i in range(int(step) +1):
    xi.append(a)
    Fxi.append(function(a))
    a += counter


df = pd.DataFrame({'xi': xi, 
                   'F(xi)': Fxi}) 

print(df)

