import numpy as np
x = np.array([0,1,2],float)
y = np.array([1,2,4],float)
xp = 1.5
yp = 0
for i in range(3):
    
    p = 1
    
    for j in range(3):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]
print('Interpolated value at %.3f is %.3f.' % (xp, yp))

