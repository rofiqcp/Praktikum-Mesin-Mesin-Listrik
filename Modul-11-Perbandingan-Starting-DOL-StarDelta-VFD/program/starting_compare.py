import math
try:
 import matplotlib.pyplot as plt
except ImportError: plt=None
T=[i/100 for i in range(0,501)]
def dol(t): return (5.5*math.exp(-t/0.45)+1.0, 1-math.exp(-t/0.7))
def sd(t):
 if t<1.5: return (2.2*math.exp(-t/0.6)+1.0, .72*(1-math.exp(-t/0.9)))
 if t<1.7: return (3.0, .70)
 return (1.0+1.7*math.exp(-(t-1.7)/.35), .70+.30*(1-math.exp(-(t-1.7)/.55)))
def vfd(t): return (1.1+.35*math.exp(-t/1.4), min(1,t/2.3))
for name,fn in [('DOL',dol),('STAR-DELTA',sd),('VFD',vfd)]:
 vals=[fn(t) for t in T]; peak=max(x[0] for x in vals); t90=next((t for t,x in zip(T,vals) if x[1]>=.9),None); print(name,'Ipeak pu=',round(peak,2),'t90=',t90)
 if plt: plt.plot(T,[x[0] for x in vals],label=name)
if plt: plt.xlabel('time (s)'); plt.ylabel('Current (pu)'); plt.grid(True); plt.legend(); plt.show()