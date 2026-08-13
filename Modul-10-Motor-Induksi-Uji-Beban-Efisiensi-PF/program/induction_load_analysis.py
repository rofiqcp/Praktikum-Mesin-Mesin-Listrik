import csv, math
from pathlib import Path
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt=None
f=50; poles=4; ns=120*f/poles; rows=[]
path=Path(__file__).with_name('data_induction_load.csv')
with path.open(newline='') as fh:
    for r in csv.DictReader(fh):
        x={k:float(v) for k,v in r.items()}
        x['Iavg']=(x['IA']+x['IB']+x['IC'])/3
        x['unb']=100*max(abs(x['IA']-x['Iavg']),abs(x['IB']-x['Iavg']),abs(x['IC']-x['Iavg']))/x['Iavg']
        x['slip']=100*(ns-x['rpm'])/ns
        x['pout']=x['torque']*x['rpm']*2*math.pi/60
        x['eta']=100*x['pout']/x['Pin'] if x['Pin'] else 0
        rows.append(x)
        print(f"load={x['load_pct']:.0f}% Iavg={x['Iavg']:.2f}A unb={x['unb']:.2f}% slip={x['slip']:.2f}% eta={x['eta']:.1f}%")
if plt:
    L=[r['load_pct'] for r in rows]
    plt.plot(L,[r['PF'] for r in rows],'o-',label='PF'); plt.plot(L,[r['eta']/100 for r in rows],'s-',label='eta/100'); plt.grid(True); plt.legend(); plt.show()
    plt.plot(L,[r['slip'] for r in rows],'o-'); plt.xlabel('Load (%)'); plt.ylabel('Slip (%)'); plt.grid(True); plt.show()