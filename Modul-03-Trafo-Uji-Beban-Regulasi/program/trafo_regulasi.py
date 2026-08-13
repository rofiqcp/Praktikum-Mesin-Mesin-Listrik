import csv
try:
 import matplotlib.pyplot as plt
except ImportError: plt=None
rows=[]
with open('data_trafo.csv',newline='') as f:
 for r in csv.DictReader(f): rows.append({k:float(v) for k,v in r.items()})
vnl=rows[0]['V2']
for r in rows:
 pout=r['V2']*r['I2']*r['pf']
 r['reg']=0 if r['I2']==0 else (vnl-r['V2'])/r['V2']*100
 r['eta']=0 if r['Pin']==0 else pout/r['Pin']*100
 print(f"load={r['load_pct']:3.0f}% V2={r['V2']:.2f}V reg={r['reg']:.2f}% eta={r['eta']:.2f}%")
if plt:
 x=[r['load_pct'] for r in rows]
 plt.plot(x,[r['reg'] for r in rows],'o-',label='regulasi %')
 plt.plot(x,[r['eta'] for r in rows],'s-',label='efisiensi %')
 plt.xlabel('Beban (%)'); plt.grid(True); plt.legend(); plt.show()