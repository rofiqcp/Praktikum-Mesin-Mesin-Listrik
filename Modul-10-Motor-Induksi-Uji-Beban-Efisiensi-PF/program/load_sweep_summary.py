import csv
from pathlib import Path

path = Path(__file__).with_name('data_induction_load.csv')
rows = []
with path.open(newline='') as f:
    for row in csv.DictReader(f):
        r = {k: float(v) for k, v in row.items()}
        r['Iavg'] = (r['IA'] + r['IB'] + r['IC']) / 3.0
        rows.append(r)

print(f'rows={len(rows)}')
print('load | rpm | Iavg | PF | Pin | torque')
for r in rows:
    print(
        f"{r['load_pct']:5.1f}% | {r['rpm']:7.1f} | {r['Iavg']:5.3f} | "
        f"{r['PF']:5.3f} | {r['Pin']:7.1f} | {r['torque']:6.3f}"
    )

if rows:
    by_current = max(rows, key=lambda x: x['Iavg'])
    by_pf = max(rows, key=lambda x: x['PF'])
    by_torque = max(rows, key=lambda x: x['torque'])
    min_rpm = min(rows, key=lambda x: x['rpm'])
    print('\n=== TITIK PENTING ===')
    print(f"arus rata-rata maksimum: load={by_current['load_pct']:.0f}% Iavg={by_current['Iavg']:.3f} A")
    print(f"PF maksimum: load={by_pf['load_pct']:.0f}% PF={by_pf['PF']:.3f}")
    print(f"torsi maksimum: load={by_torque['load_pct']:.0f}% T={by_torque['torque']:.3f} Nm")
    print(f"rpm minimum: load={min_rpm['load_pct']:.0f}% rpm={min_rpm['rpm']:.1f}")
