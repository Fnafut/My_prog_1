import numpy as np 
import scipy 
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

def sys_x(z, t):
    phi, omega = z
    dphi_dt=omega 
    domega_dt=-g*np.sin(phi)/L-rd*omega
    return [dphi_dt, domega_dt]
g = 9.81 
L = 1
m = 1
V0=0
W0=V0/L
gamma_=90
gamma=gamma_*np.pi/180
alpha=0.00
rd=alpha/m 

Z0x=[gamma, W0]

td=10 #длительность 
t_eval=np.linspace(0, td, 800)

sol_phi=scipy.integrate.odeint(sys_x, Z0x, t_eval)
phi=sol_phi[:,0]
omega=sol_phi[:,1]
phi_acc=gamma*np.cos(np.power(g/L,0.5)*t_eval)

N=len(t_eval)

fig=plt.figure()
ax=plt.axes(xlim=(-3, 3), ylim=(-3, 3))
line1,=plt.plot([],[], color='r', lable=f'точном решении', maker='*')
line2,=plt.plot([],[], color='b', lable=f'приближенном решении', maker='о')

T_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12, verticalalignment='top')

def line_func():
    line1.set_data([],[])
    line2.set_data([],[])
    T_text.set_text('')
    return line1, line2

def anim_line(frame):

    t=phi[frame]
    x=L*np.sin(t)
    y=L*np.cos(t)
    x0=[0,x]
    x1=[0+2,-y]

    t2=phi[frame]
    xx=L*np.sin(t2)
    yy=L*np.cos(t2)
    y0=[0,xx]
    y1=[0+2,-yy]

    line1.set_data(x0,x1)
    line2.set_data(y0,y1)

T_text.set_text(f't={np.round(t_eval[frame],3)},\ngamma={gamma_}')
return line1,line2, T_text

anim=animation.FuncAnimation(fig,anim_line,frames=N, init_func=line_func,interval=5,blit=True,repeat=True)

plt.title
plt.grid(True)
plt.legend(loc=8)

plt.show()