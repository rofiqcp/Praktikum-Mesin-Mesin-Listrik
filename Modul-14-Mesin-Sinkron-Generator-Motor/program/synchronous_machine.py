import math
try:
 import matplotlib.pyplot as plt
except ImportError:
 plt=None
poles=4
for f in [25,40,50,60]:
 print(f'f={f} Hz -> Ns={120*f/poles:.0f} rpm')
If=[i/10 for i in range(0,31)]
V=[240*(1-math.exp(-1.35*x)) for x in If]
Ia=[2.0+1.25*(x-1.5)**2 for x in If]
imin=min(range(len(Ia)), key=Ia.__getitem__)
print(f'Model V-curve minimum current at If={If[imin]:.2f} A')
if plt:
 plt.plot(If,V,'o-'); plt.xlabel('Field current (A)'); plt.ylabel('No-load voltage'); plt.grid(True); plt.show()
 plt.plot(If,Ia,'s-'); plt.xlabel('Field current (A)'); plt.ylabel('Armature current (A)'); plt.grid(True); plt.show()