import numpy as np
import matplotlib.pyplot as plt


def Explicit( h: float, omega: float,tb: float,x0: float):
    mesh_number= int(np.ceil(tb/h))
    x_num=np.zeros(mesh_number+1)


    t_num=np.linspace(0,tb,mesh_number+1)
    x_num[0] = x0
    for i in range(1, len(t_num)):
        x_num[i] = x_num[i-1] + h *  (-x_num[i-1]+ np.sin(omega*i*h))
    return x_num, t_num
h: float = 2
omega: float = 2
tb: float = 10
x0: float = 10

def RK4(h:float, omega:float, tb:float, x0:float):
    mesh_number= int(np.ceil(tb/h))
    t_num=np.linspace(0,tb,mesh_number+1)
    x_num=np.zeros(mesh_number+1)
    x_num[0] = x0

    for i in range(1, len(t_num)):
        k1=-x_num[i-1]+np.sin(omega*t_num[i-1])
        k2=-(x_num[i-1]+h/2*k1)+np.sin(omega*(t_num[i-1]+h/2))
        k3=-(x_num[i-1]+h/2*k2)+np.sin(omega*(t_num[i-1]+h/2))
        k4=-(x_num[i-1]+h*k3)+np.sin(omega*(t_num[i-1]+h))
        x_num[i] = x_num[i-1] + h/6 *  (k1+2*k2+2*k3+k4)
    return x_num, t_num

x_1, t_1 = Explicit(h, omega, tb, x0)
h=0.5
x_2, t_2 = Explicit(0.5, omega, tb, x0)

t_3,x_3 = RK4(0.5, omega, tb, x0)

t_4,x_4 = Explicit(0.1, omega, tb, x0)
plt.figure(figsize=(10,10))
plt.plot(t_1,x_1,'ko-',ms=6,label=r'Explicit Euler, $h=2$')
plt.plot(t_2,x_2,'ro-',ms=6,label=r'Explicit Euler, $h=0.5$')
plt.plot(t_3,x_3,'bo-',ms=6,label=r'RK4, $h=0.5$')
plt.plot(t_4,x_4,'go-',ms=6,label=r'Explicit Euler, $h=0.1$')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()

plt.show()


