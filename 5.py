import numpy as np
import matplotlib.pyplot as plt

R = 1
t = np.linspace(0, 2 * np.pi, 100)

x = R * (t - np.sin(3*t))
y = R * (1 - np.cos(3*t))

plt.figure(figsize=(10, 5))
plt.plot(x, y,
         label='цикл', color='b')
plt.title('цикл')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0,
color='r', linewidth=0.5,
ls='--')
plt.axvline(0,
color='r', linewidth=0.5,
ls='--')
plt.grid()
plt.legend()
plt.axis('equal')
plt.show()
            