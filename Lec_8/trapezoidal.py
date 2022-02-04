#Trapezoidal rule

import math
import numpy as np
def func(y):
    f = 10 - y*y
    return(f)
def func_derivative2(y):
    f_doubleprime = math.exp(y)
    return(f_doubleprime)

a= -2
b= 2
n = 100
dx = (b-a)/(n-1)
x= np.zeros(n)
init = (func(a)+func(b))/2

def trapezoidal():
        integral = 0
        for i in range(1,n-1):
            x[i] = a + i*dx
            ff = func(x[i])
            integral = ff + integral
        Value = dx*(init + integral)
        return(Value)
print("The value of integral using Trapezoidal rule is ",trapezoidal())

