from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
 
t =np.linspace(0, 2 * np.pi, 1000)
 
def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = 
    y = 
    return x, y
 
 
fig, ax = plt.subplots()
heart, = plt.plot([], [], 'o', color='g', label='heart')
 
 
def animate(i):
    heart.set_data(circle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))
    return heart
 
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('animation_3.gif', writer="pillow")