import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Длина 
l = 2


theta = np.pi/4


t_max = 10

#время
dt = 0.1

# массив
t = np.arange(0, t_max, dt)

# Вычисление положения маятника
x = l * np.sin(theta * np.cos(2 * np.pi * t / t_max))
y = -l * np.cos(theta * np.cos(2 * np.pi * t / t_max))
# Создание фигуры и оси
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim([-l * 1.2, l * 1.2])
ax.set_ylim([-l * 1.2, l * 1.2])
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Маятник')

line, = ax.plot([], [], 'r-', lw=2)

# кадры
def update(frame):
    line.set_data([0, x[frame]], [0, y[frame]])
    return line,

#  анимация
ani = FuncAnimation(fig, update, frames=len(t), interval=10, blit=True)

# Сохранение png
ani.save('maiatnik.png', writer='imagemagick')