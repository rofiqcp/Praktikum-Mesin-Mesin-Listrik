import csv, math
from pathlib import Path
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt=None
rows=[]
path=Path(__file__).with_name('data_dc.csv')
with path.open(newline='') as f:
    for r in csv.DictReader(f):
        x={k:float(v) for k,v in r.items()}
        x['pin']=x['V']*x['I']; x['omega']=x['rpm']*2*math.pi/60
        x['pout']=x['torque']*x['omega']; x['eta']=0 if x['pin']==0 else 100*x['pout']/x['pin']; rows.append(x)
for r in rows: print(f"load={r['load_pct']:3.0f}% I={r['I']:.2f}A rpm={r['rpm']:.0f} T={r['torque']:.3f}Nm eta={r['eta']:.1f}%")
if plt:
    t=[r['torque'] for r in rows]
    plt.plot(t,[r['rpm'] for r in rows],'o-'); plt.xlabel('Torque (Nm)'); plt.ylabel('Speed (rpm)'); plt.grid(True); plt.show()
    plt.plot([r['load_pct'] for r in rows],[r['eta'] for r in rows],'s-'); plt.xlabel('Load (%)'); plt.ylabel('Efficiency (%)'); plt.grid(True); plt.show()