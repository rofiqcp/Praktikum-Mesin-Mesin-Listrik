import math
try:
 import matplotlib.pyplot as plt
except ImportError: plt=None
V=12.0; R=1.2; L=0.012; ke=0.055; kt=0.055; J=0.0025; B=0.0008; load_torque=0.02
dt=0.0005; tmax=2.0; i=0.0; w=0.0
T=[]; I=[]; RPM=[]; E=[]
for n in range(int(tmax/dt)):
 t=n*dt
 di=(V-R*i-ke*w)/L
 dw=(kt*i-B*w-load_torque)/J
 i+=di*dt; w+=dw*dt
 if n%20==0:
  T.append(t); I.append(i); RPM.append(w*60/(2*math.pi)); E.append(ke*w)
print(f'I_start model={I[0]:.2f} A, I_final={I[-1]:.2f} A, rpm_final={RPM[-1]:.1f}, backEMF={E[-1]:.2f} V')
if plt:
 plt.plot(T,I,label='Armature current (A)'); plt.plot(T,[x/100 for x in RPM],label='rpm/100'); plt.grid(True); plt.legend(); plt.xlabel('time (s)'); plt.show()