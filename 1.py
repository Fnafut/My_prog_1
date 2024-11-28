import matplotlib.pyplot as plt

x = [1, 5, 5, 1, 1]
y = [5, 5, 1, 1, 5] 

# Создаем график
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Квадрат")
plt.xlabel("X-координаты")
plt.ylabel("Y-координаты")
plt.axis('equal')  # масштаб
plt.grid(True)
plt.xlim(0, 6)  #  оси X
plt.ylim(0, 6)  #  оси Y
plt.savefig('fig_1.png')