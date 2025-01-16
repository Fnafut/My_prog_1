import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

l = 1.0  
m = 1.0  
g = 9.8  

# Начальные условия
theta0 = np.pi/4  
omega0 = 1.0      

# Время и шаг интегрирования
t_max = 10.0  # время (с)
dt = 0.01     

# движения
t = np.arange(0, t_max, dt)
theta = theta0 * np.cos(np.sqrt(g/l) * t) + (omega0 * np.sqrt(l/g)) * np.sin(np.sqrt(g/l) * t)


fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim([-l*1.2, l*1.2])
ax.set_ylim([-l*1.2, l*1.2])
ax.set_xlabel('Горизонтальное положение (м)')
ax.set_ylabel('Вертикальное положение (м)')
ax.set_title('Движение математического маятника')

# анимация
x = l * np.sin(theta)
y = -l * np.cos(theta)
line, = ax.plot([], [], 'o-', lw=2)

def animate(i):
    line.set_data([0, x[i]], [0, y[i]])
    return line,

ani = FuncAnimation(fig, animate, frames=len(t), interval=10, blit=True)

#  PNG
ani.save('maятник.png', dpi=300)
plt.show()