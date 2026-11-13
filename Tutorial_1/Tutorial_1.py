import numpy as np
import matplotlib.pyplot as plt


h=0.5
x_grid=np.arange(0,15+h,h)
f_grid=np.sin(x_grid)

df_grid=np.cos(x_grid)

x_analytical=np.linspace(0,15,500)
df_analytical=np.cos(x_analytical)


df_forward=(f_grid[1:]-f_grid[:-1])/h
x_forward=x_grid[:-1]


df_backward=(f_grid[1:]-f_grid[:-1])/h
x_backward=x_grid[1:]

df_cds=(f_grid[2:]-f_grid[:-2])/(2*h)

df_final=np.concatenate([[df_forward[0]],df_cds,[df_backward[-1]]])


# ------------------------------------- 1 ------------------------------------ #
plt.figure(figsize=(10,5))

# 1 a)
plt.plot(x_analytical, df_analytical, 'b-', linewidth=2, label="f'(x) = cos(x)")
# 1 b)
plt.plot(x_grid      , df_grid      , 'b*', linewidth=2, label="f'(x) = cos(x)")


plt.xlabel("x")
plt.ylabel("f'(x)")

plt.title("Analytical and numerical derivative of f(x)=sin(x) on [0,15]")

# ----------------------------------- 1 end ---------------------------------- #

# ------------------------------------- 2 ------------------------------------ #
plt.plot(x_forward, df_forward, 'r*', linewidth=2, label="FDS")
# ----------------------------------- 2 end ---------------------------------- #

# ------------------------------------- 3 ------------------------------------ #
plt.plot(x_backward, df_backward, 'g*', linewidth=2, label="BDS")
# ----------------------------------- 3 end ---------------------------------- #

# ------------------------------------- 4 ------------------------------------ #
#plt.plot(x_grid, df_final, 'k*', linewidth=2, label="CDS+boundary")
# ----------------------------------- 4 end ---------------------------------- #
plt.legend()
plt.grid(True)# show grid
plt.tight_layout()# automatically adjust the layout




plt.figure(figsize=(10,5))
d2f_analytical=-np.sin(x_analytical)
x_grid=np.arange(0,15+h,h)
d2f_grid=-np.sin(x_grid)
plt.plot(x_analytical, d2f_analytical, 'b-', linewidth=2, label="f''(x) = cos(x)")
plt.plot(x_grid      , d2f_grid      , 'b*', linewidth=2, label="f''(x) = cos(x) at nodes")

x_grid=np.arange(0,15+h,h)
f_grid=np.sin(x_grid)
d2f_grid=-np.sin(x_grid)
d2f_cds=(f_grid[:-2]-2*f_grid[1:-1]+f_grid[2:])/h**2
plt.plot(x_grid[1:-1]  , d2f_cds , 'r*-', linewidth=2, label="f''(x) = cos(x) using cds")
plt.xlabel("x")
plt.ylabel("f''(x)")

plt.title("Analytical and numerical secondary derivative of f(x)=sin(x) on [0,15]")
plt.legend()
plt.grid(True)# show grid
plt.tight_layout()# automatically adjust the layout

plt.figure(figsize=(10,5))
for h in [0.1, 0.5, 1]:
    x_grid=np.arange(0,15+h,h)
    f_grid=np.sin(x_grid)

    d2f_grid=-np.sin(x_grid)
    d2f_cds=(f_grid[:-2]-2*f_grid[1:-1]+f_grid[2:])/h**2
    plt.plot(x_grid[1:-1]  , np.abs(d2f_cds-d2f_grid[1:-1]) , 'r*-', linewidth=2, label="f'(x) = cos(x)")

    
plt.show()
