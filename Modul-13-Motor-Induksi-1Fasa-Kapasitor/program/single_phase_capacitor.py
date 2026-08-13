import math
try:
 import matplotlib.pyplot as plt
except ImportError:
 plt=None
f=50
caps=[5,10,15,20,30,40]
xc=[1/(2*math.pi*f*c*1e-6) for c in caps]
for c,x in zip(caps,xc): print(f'C={c:>2} uF -> Xc={x:7.2f} ohm')
if plt:
 plt.plot(caps,xc,'o-'); plt.xlabel('Capacitance (uF)'); plt.ylabel('Xc (ohm)'); plt.grid(True); plt.show()
print('Catatan: grafik untuk analisis konsep; gunakan kapasitor sesuai spesifikasi trainer/manufaktur.')