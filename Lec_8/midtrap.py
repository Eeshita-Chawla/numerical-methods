#importing the module
import math
import numpy as np

#defining the functions
def func(y):
    f = 10 - 3*y
    return(f)

#initialising the values
a=0
b=1
n=100
dx= (b-a)/(n-1)
init = (func(a)+func(b))/2
integral = 0

#initialization
x3= np.zeros(n)
x= np.zeros(n)
A_prime3 = 0

#mid point rule
for i in range(1,n):
    x3[i] = a + (i-0.5)*dx
    A3 = func(x3[i])*dx
    A_prime3 = A3 + A_prime3

#Trapezoidal rule
for i in range(1,n-1):
    x[i] = a + i*dx
    ff = func(x[i])
    integral = ff + integral
Value = dx*(init + integral)
Difference = Value - A_prime3
print("Value of integral by mid point rule is ",A_prime3)
print("Value of integral by trapezoidal rule is ",Value)
print("Difference between value of integral between trapezoidal and mid point rule is ",Difference)

