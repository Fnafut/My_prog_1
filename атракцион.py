import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры маятника
length = 1.0  # Длина маятника
g = 9.81      # Ускорение свободного падения
theta = np.pi / 4  # Начальный угол (45 градусов)
omega = 0      # Начальная угловая скорость

# Параметры анимации
dt = 0.05      # Шаг времени
frames = 300    # Количество кадров

# Параметры стены
wall_x = 1.5   # Положение стены
platform_width = 0.1
platform_height = 0.02

# Создание фигуры и осей
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid()

# Создание линии маятника и платформы
line, = ax.plot([], [], lw=2, color='blue')
platform, = ax.plot([], [], lw=2, color='red')

# Функция для инициализации анимации
def init():
    line.set_data([], [])
    platform.set_data([], [])
    return line, platform

# Функция для обновления анимации
def update(frame):
    global theta, omega

    # Уравнения движения маятника
    alpha = -g / length * np.sin(theta)  # Угловое ускорение
    omega += alpha * dt                   # Обновление угловой скорости
    theta += omega * dt                   # Обновление угла

    # Положение маятника
    x = length * np.sin(theta)
    y = -length * np.cos(theta)

    # Обновление линии маятника
    line.set_data([0, x], [0, y])

    # Положение платформы
    platform_x = x - platform_width / 2
    platform_y = y - platform_height / 2
    platform.set_data([platform_x, platform_x + platform_width], [platform_y, platform_y])

    # Проверка на столкновение со стеной
    if x >= wall_x:
        # Имитация разрушения платформы
        platform.set_data([], [])
        # Можно добавить логику для разлета осколков

    return line, platform

# Создание анимации
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=dt*1000)

# Сохранение png
ani.save('maiatnik.png', writer='imagemagick')
