import math as mt
import physics_mod as pm
h = 100
a = 45
B = 35
g = pm.g
v = mt.sqrt(g*h*(mt.tan(B))**2 / 2*(mt.cos(a))**2 * (1-mt.tan(B) * mt.tan (a)))
print (v)

