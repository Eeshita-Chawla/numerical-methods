from scipy.interpolate import CubicSpline
import numpy as np
x=np.array([0,1,2])
y=np.array([1,2,4])
s=CubicSpline(x,y)
v1=s(1.5)
v2=2**1.5
print("Interpolated value is ",v1)
print("Value from original function is ",v2)
