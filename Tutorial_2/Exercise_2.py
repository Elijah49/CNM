import numpy as np
import  matplotlib.pyplot as plt
def ExplicitEuler_Df2(lam,y0,h,tf):
    N=int(np.ceil(tf/h))
    t_num=np.arange(0,N+1)*h
    dtype = np.result_type(y0, lam, float)
    y_num=np.zeros(N+1,dtype=dtype); y_num[0]=y0
    for i in range (N):
        y_num[i+1]=(1+lam*h+(lam*h)**2/2)*y_num[i]
    return t_num,y_num 

def ExplicitEuler(lam,y0,h,tf):
    N=int(np.ceil(tf/h))
    t_num=np.arange(0,N+1)*h
    dtype = np.result_type(y0, lam, float)
    y_num=np.zeros(N+1,dtype=dtype); y_num[0]=y0
    for i in range (N):
        y_num[i+1]=(1+lam*h)*y_num[i]
    return t_num,y_num 

tf=25
lam=-1
y0=5
hmax=2
h=hmax
t=np.linspace(0,25,500)
y_exact=y0*np.exp(-t)
t_num_2, y_num_2 = ExplicitEuler_Df2(lam, y0,hmax,tf)
t_num_c,y_num_c = ExplicitEuler_Df2(lam,y0,hmax/2,tf)
t_num_d,y_num_d = ExplicitEuler_Df2(lam,y0,hmax+0.1,tf)
t_num_2_1, y_num_2_1 = ExplicitEuler(lam, y0,hmax,tf)
t_num_c_1,y_num_c_1 = ExplicitEuler(lam,y0,hmax/2,tf)
t_num_d_1,y_num_d_1 = ExplicitEuler(lam,y0,hmax+0.1,tf)


plt.figure(figsize=(10,10))
plt.plot(t_num_2,y_num_2,'kd-',ms=6,label=r'Euler, $h=h_{\max}=2$')
plt.plot(t, y_exact,'k-',lw=1,label=fr'exact y={y0}e^{{-t}}$')
plt.plot(t_num_c,y_num_c,'ko-',ms=6,label=r'Euler, $h=h_{\max}/2=1$')
plt.plot(t_num_d,y_num_d,'k*-',ms=6,label=r'Euler, $h=h_{\max}+0.1=1.1$')
plt.plot(t_num_2_1,y_num_2_1,'rd-',ms=6,label=r'Euler, $h=h_{\max}=2$')
plt.plot(t, y_exact,'r-',lw=1,label=fr'exact y={y0}e^{{-t}}$')
plt.plot(t_num_c_1,y_num_c_1,'ro-',ms=6,label=r'Euler, $h=h_{\max}/2=1$')
plt.plot(t_num_d_1,y_num_d_1,'r*-',ms=6,label=r'Euler, $h=h_{\max}+0.1=1.1$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()


plt.figure(figsize=(10,8))
plt.plot(t_num_2,abs(y0*np.exp(lam*t_num_2)-y_num_2),'ko--',ms=6,label=r'Euler, $h=h_{\max}=2$')
plt.plot(t_num_c,abs(y0*np.exp(lam*t_num_c)-y_num_c),'rD--',ms=6,label=r'Euler, $h=h_{\max}/2=1$')
plt.plot(t_num_d,abs(y0*np.exp(lam*t_num_d)-y_num_d),'bd--',ms=6,label=r'Euler, $h=h_{\max}+0.1=1.1$')

plt.xlabel('t')
plt.ylabel('error')
plt.legend()

lam=1j
y0=5
hmax=0.1
tf=25
t_num_3,y_num_3=ExplicitEuler_Df2(lam,y0,hmax,tf)
plt.figure(figsize=(10,10))
plt.plot(t_num_3,y_num_3,'ko--',ms=6,label=r'Euler, $h=h_{\max}=2$')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()





plt.show()
