import math
try:
 import matplotlib.pyplot as plt
except ImportError: plt=None
f=50.0; poles=4; Vth=210.0; Rth=1.1; Xth=1.8; R2=0.9; X2=1.6
ns_rpm=120*f/poles
ws=2*math.pi*ns_rpm/60
S=[i/1000 for i in range(1,1001)]
T=[]; RPM=[]
for s in S:
 r=R2/s
 torque=3*Vth**2*r/(ws*((Rth+r)**2+(Xth+X2)**2))
 T.append(torque); RPM.append((1-s)*ns_rpm)
imax=max(range(len(T)),key=T.__getitem__)
print(f'Ns={ns_rpm:.1f} rpm')
print(f'Breakdown torque={T[imax]:.2f} Nm at rpm={RPM[imax]:.1f}, slip={S[imax]:.3f}')
for s in [1,.1,.04,.02]:
 idx=min(range(len(S)), key=lambda i:abs(S[i]-s)); print(f's={s:.3f} rpm={RPM[idx]:.1f} T={T[idx]:.2f}Nm fr={s*f:.2f}Hz')
if plt:
 plt.plot(RPM,T); plt.xlabel('Rotor speed (rpm)'); plt.ylabel('Torque (Nm)'); plt.grid(True); plt.show()