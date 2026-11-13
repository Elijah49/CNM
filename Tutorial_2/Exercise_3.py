import numpy as np
import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def ImplicitEuler(lam,y0,h,tf):
    N=int(np.ceil(tf/h))
    t_num=np.arange(0,N+1)*h
    dtype = np.result_type(y0, lam, float)
    y_num=np.zeros(N+1,dtype=dtype); y_num[0]=y0
    for i in range (N):
        y_num[i+1]=1/(1-h*lam)*y_num[i]
    return t_num,y_num 

def ExplicitEuler(lam,y0,h,tf):
    N=int(np.ceil(tf/h))
    t_num=np.arange(0,N+1)*h
    dtype = np.result_type(y0, lam, float)
    y_num=np.zeros(N+1,dtype=dtype); y_num[0]=y0
    for i in range (N):
        y_num[i+1]=(1+lam*h)*y_num[i]
    return t_num,y_num 


tf=20
lam=-2
y0=5
hmax=2
h=hmax
t=np.linspace(0,tf,500)
y_exact=y0*np.exp(lam*t)
t_num_2_a_i, y_num_2_a_i = ImplicitEuler(lam,y0,1.1,tf)
t_num_2_a_e, y_num_2_a_e = ExplicitEuler(lam,y0,1.1,tf)

t_num_2_b_i, y_num_2_b_i = ImplicitEuler(lam,y0,0.1,tf)
t_num_2_b_e, y_num_2_b_e = ExplicitEuler(lam,y0,0.1,tf)
lam=1j
t_num_3_a_i, y_num_3_a_i = ImplicitEuler(lam,y0,1,tf)
t_num_3_a_e, y_num_3_a_e = ExplicitEuler(lam,y0,1,tf)
t_num_3_b_i, y_num_3_b_i = ImplicitEuler(lam,y0,0.1,tf)
t_num_3_b_e, y_num_3_b_e = ExplicitEuler(lam,y0,0.1,tf)

plt.figure(figsize=(10,10))
plt.plot(t_num_2_a_i,y_num_2_a_i,'ko-',ms=6,label=r'Implicit Euler, $h=1.1$')
plt.plot(t_num_2_a_e,y_num_2_a_e,'ro-',ms=6,label=r'Explicit Euler, $h=1.1$')
plt.plot(t, y_exact,'b-',lw=1,label=fr'exact $y={y0}e^{{{lam}t}}$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()

plt.figure(figsize=(10,10))

plt.plot(t_num_2_b_i,y_num_2_b_i,'k*-',ms=3,label=r'Implicit Euler, $h=0.1$')
plt.plot(t_num_2_b_e,y_num_2_b_e,'r*-',ms=3,label=r'Explicit Euler, $h=0.1$')
plt.plot(t, y_exact,'b-',lw=1,label=fr'exact $y={y0}e^{{{lam}t}}$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(t_num_3_a_i, y_num_3_a_i.real, y_num_3_a_i.imag,
        'k*-', ms=3, label=r'implicit, $\lambda=i,\ h=1$')
#ax.plot(t_num_3_a_e, y_num_3_a_e.real, y_num_3_a_e.imag,
 #       'r*-', ms=3, label=r'explicit, $\lambda=i,\ h=1$')
ax.plot(t, (y0*np.exp(1j*t)).real, (y0*np.exp(1j*t)).imag,
        'b-', lw=1, label=r'exact $5e^{it}$')
ax.set_box_aspect((1, 1, 1))
plt.xlabel('t')
plt.ylabel('y')
plt.legend()



fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(t_num_3_b_i, y_num_3_b_i.real, y_num_3_b_i.imag,
        'k*-', ms=3, label=r'implicit, $\lambda=i,\ h=0.1$')
ax.plot(t_num_3_b_e, y_num_3_b_e.real, y_num_3_b_e.imag,
        'r*-', ms=3, label=r'explicit, $\lambda=i,\ h=0.1$')
ax.plot(t, (y0*np.exp(1j*t)).real, (y0*np.exp(1j*t)).imag,
        'b-', lw=1, label=r'exact $5e^{it}$')
ax.set_box_aspect((1, 1, 1))
plt.xlabel('t')
plt.ylabel('y')
plt.legend()






plt.show()
