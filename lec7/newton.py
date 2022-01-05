import numpy as np
import math


#### Defining the function ####
def func(y):
    f = y**2 - 10
    return(f)

#### Defining the derivative of the function ####
def func_derivative(y):
    f_prime = 2*y
    return(f_prime)
    
def NewtonRaphson():
    epsilon = 0.00001
    x = [0.001]# It will make the derivative in this case 
    #blow up hence we should chose something else maybe a positive number would do. 
    for i in range(0,100):
        h = func(x[i])/ func_derivative(x[i])
        if (np.abs(h) < epsilon):
            
            return(x[i])
        elif ( func_derivative(x[i]) != 0):
            r = x[i] - h
            x.append(r)
    return(x[99])
print(NewtonRaphson())
