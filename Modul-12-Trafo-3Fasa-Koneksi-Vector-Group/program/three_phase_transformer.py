import math
try:
 import matplotlib.pyplot as plt
except ImportError: plt=None
N1=1000; N2=200; Vline1=380; a=N1/N2
connections=['Y-Y','D-D','D-Y','Y-D']
for c in connections:
 if c=='Y-Y': v2=Vline1/a
 elif c=='D-D': v2=Vline1/a
 elif c=='D-Y': v2=math.sqrt(3)*Vline1/a
 else: v2=Vline1/(math.sqrt(3)*a)
 print(f'{c}: Vline2 ideal={v2:.2f} V')
angles=[0,-120,120]
if plt:
 for ang in angles:
  r=math.radians(ang); plt.arrow(0,0,math.cos(r),math.sin(r),head_width=.05,length_includes_head=True)
 plt.axis('equal'); plt.grid(True); plt.title('Contoh phasor tiga fasa'); plt.show()