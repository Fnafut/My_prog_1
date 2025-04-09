import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

# Параметры
length = 1  # Длина маятника
angle1 = np.pi / 4  # Начальный угол первого маятника
angle2 = -np.pi / 4  # Начальный угол второго маятника
angle3 = np.pi / 6  # Начальный угол третьего маятника
num_frames = 100  # Количество кадров в анимации

# Переменные для хранения состояния коробки
box_owner = 0  # 0 - первый маятник, 1 - второй, 2 - третий
collision_count = 0  # Счетчик столкновений

# Функция для обновления анимации
def update(frame):
    global box_owner, collision_count
    plt.clf()
    
    # Углы маятников
    theta1 = angle1 * np.cos(frame * 2 * np.pi / num_frames)  # Вращение первого маятника
    theta2 = angle2 * np.cos(frame * 2 * np.pi / num_frames)  # Вращение второго маятника
    theta3 = angle3 * np.cos(frame * 2 * np.pi / num_frames)  # Вращение третьего маятника

    # Координаты концов маятников
    x1 = length * np.sin(theta1)
    y1 = -length * np.cos(theta1)
    x2 = length + length * np.sin(theta2)  # Второй маятник на расстоянии
    y2 = -length * np.cos(theta2)
    x3 = 2 * length + length * np.sin(theta3)  # Третий маятник на расстоянии
    y3 = -length * np.cos(theta3)

    # Проверка на соприкосновение
    if (box_owner == 0 and (x1 >= x2 - 0.1 and x1 <= x2 + 0.1) and (y1 >= y2 - 0.1 and y1 <= y2 + 0.1)):
        collision_count += 1
        if collision_count == 3:
            box_owner = 1  # Передаем коробку второму маятнику
            collision_count = 0  # Сбрасываем счетчик
    elif (box_owner == 1 and (x2 >= x3 - 0.1 and x2 <= x3 + 0.1) and (y2 >= y3 - 0.1 and y2 <= y3 + 0.1)):
        collision_count += 1
        if collision_count == 3:
            box_owner = 2  # Передаем коробку третьему маятнику
            collision_count = 0  # Сбрасываем счетчик
    elif (box_owner == 2 and (x3 >= x1 - 0.1 and x3 <= x1 + 0.1) and (y3 >= y1 - 0.1 and y3 <= y1 + 0.1)):
        collision_count += 1
        if collision_count == 3:
            box_owner = 0  # Передаем коробку первому маятнику
            collision_count = 0  # Сбрасываем счетчик

    # Рисуем маятники
    plt.plot([0, x1], [0, y1], 'r-', lw=2)  # Первый маятник
    plt.plot([length, x2], [0, y2], 'b-', lw=2)  # Второй маятник
    plt.plot([2 * length, x3], [0, y3], 'g-', lw=2)  # Третий маятник

    # Рисуем коробку
    box_color = ['orange', 'purple', 'cyan'][box_owner]  # Цвет коробки в зависимости от владельца
    if box_owner == 0:
        box = Rectangle((x1 - 0.05, y1 - 0.05), 0.1, 0.1, color=box_color)  # Коробка у первого маятника
    elif box_owner == 1:
        box = Rectangle((x2 - 0.05, y2 - 0.05), 0.1, 0.1, color=box_color)  # Коробка у второго маятника
    else:
        box = Rectangle((x3 - 0.05, y3 - 0.05), 0.1, 0.1, color=box_color)  # Коробка у третьего маятника

    plt.gca().add_patch(box)

    # Устанавливаем границы
    plt.xlim(-1, 3 * length)
    plt.ylim(-1.5, 0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')  # Отключаем оси

# Создаем анимацию
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=50)

# Сохраняем анимацию в формате GIF
ani.save('pendulums_with_box_transfer.gif', writer='imagemagick', fps=20)

plt.show()
