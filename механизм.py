import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

# Параметры
length = 1  # Длина маятника
angle1 = np.pi / 4  # Начальный угол первого маятника
angle2 = -np.pi / 4  # Начальный угол второго маятника
num_frames = 100  # Количество кадров в анимации

# Переменные для хранения состояния коробки
box_at_first = True  # Коробка изначально у первого маятника

# Функция для обновления анимации
def update(frame):
    global box_at_first
    plt.clf()
    # Углы маятников
    theta1 = angle1 * np.cos(frame * 2 * np.pi / num_frames)  # Вращение первого маятника
    theta2 = angle2 * np.cos(frame * 2 * np.pi / num_frames)  # Вращение второго маятника

    # Координаты концов маятников
    x1 = length * np.sin(theta1)
    y1 = -length * np.cos(theta1)
    x2 = length + length * np.sin(theta2)  # Второй маятник на расстоянии
    y2 = -length * np.cos(theta2)

    # Проверка на соприкосновение
    if (x1 >= x2 - 0.1 and x1 <= x2 + 0.1) and (y1 >= y2 - 0.1 and y1 <= y2 + 0.1):
        box_at_first = not box_at_first  # Переключаем состояние коробки

    # Рисуем маятники
    plt.plot([0, x1], [0, y1], 'r-', lw=2)  # Первый маятник
    plt.plot([length, x2], [0, y2], 'b-', lw=2)  # Второй маятник

    # Рисуем коробку
    if box_at_first:
        box = Rectangle((x1 - 0.05, y1 - 0.05), 0.1, 0.1, color='orange')  # Коробка у первого маятника
    else:
        box = Rectangle((x2 - 0.05, y2 - 0.05), 0.1, 0.1, color='orange')  # Коробка у второго маятника

    plt.gca().add_patch(box)

    # Устанавливаем границы
    plt.xlim(-1, 2 * length)
    plt.ylim(-1.5, 0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')  # Отключаем оси

# Создаем анимацию
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Сохраняем анимацию в формате GIF
ani.save('pendulums_with_box_transfer.gif', writer='imagemagick', fps=20)

plt.show()
