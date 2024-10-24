import numpy as np
x0=5
y0=9
v0x=1
v0y=-1
g=10
a=np.zeros([5,2])
for t in range(0,5):
    for i in 0,1:
        if i==0:
            x = x0 + v0x*t
            a[t,i]=x
        else:
            y = y0 + v0y*t - (g*t)**2 / 2
            a[t,i]=y
print(a)    