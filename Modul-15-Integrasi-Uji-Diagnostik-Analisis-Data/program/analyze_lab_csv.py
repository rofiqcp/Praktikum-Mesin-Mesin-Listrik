import csv, math
from pathlib import Path
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt=None
path=Path(__file__).with_name('lab_data.csv')
rows=[]
with path.open(newline='') as f:
    for r in csv.DictReader(f):
        for k in ['timestamp','V','I','P','PF','rpm','torque','temp']:
            r[k]=float(r[k])
        r['pout']=r['torque']*r['rpm']*2*math.pi/60
        r['eta']=100*r['pout']/r['P'] if r['P'] else 0
        rows.append(r)
Vbase=rows[0]['V']
print('test,V,I,rpm,temp,eta,flags')
for r in rows:
    flags=[]
    if abs(r['V']-Vbase)/Vbase>0.015: flags.append('V_DEVIATION')
    if r['temp']>55: flags.append('TEMP_HIGH_FOR_DATASET')
    if r['rpm']<1430: flags.append('RPM_LOW')
    print(f"{r['test']},{r['V']:.0f},{r['I']:.2f},{r['rpm']:.0f},{r['temp']:.0f},{r['eta']:.1f},{'|'.join(flags) or 'OK'}")
if plt:
    x=[r['timestamp'] for r in rows]
    plt.plot(x,[r['V'] for r in rows],'o-',label='V')
    plt.plot(x,[r['temp'] for r in rows],'s-',label='temp')
    plt.grid(True); plt.legend(); plt.show()