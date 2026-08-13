import math
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt=None

ratio=220/24
loss_factor=0.018
v1=[44,88,132,176,220]
v2_ideal=[v/ratio for v in v1]
v2_model=[x*(1-loss_factor*(x/220)**2) for x in v2_ideal]
i0=[0.04+0.00045*v for v in v1]
print('V1,V2_model,I0,ratio_measured')
for a,b,c in zip(v1,v2_model,i0): print(f'{a:.1f},{b:.3f},{c:.3f},{a/b:.3f}')
if plt:
    plt.plot(v1,v2_ideal,'o-',label='ideal')
    plt.plot(v1,v2_model,'s-',label='model sederhana')
    plt.xlabel('V1 (V)'); plt.ylabel('V2 (V)'); plt.grid(True); plt.legend(); plt.show()