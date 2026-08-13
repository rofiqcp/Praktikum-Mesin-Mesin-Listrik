import csv
import math
from pathlib import Path

path = Path(__file__).with_name('data_induction_load.csv')
rows = []
with path.open(newline='') as f:
    for row in csv.DictReader(f):
        r = {k: float(v) for k, v in row.items()}
        rows.append(r)

print(f'rows={len(rows)}')
print('columns=', ','.join(rows[0].keys()) if rows else '-')

for r in rows:
    load = r.get('load_pct', 0.0)
    rpm = r.get('rpm', 0.0)
    current = r.get('I', r.get('current', 0.0))
    pf = r.get('PF', r.get('pf', 0.0))
    print(f'load={load:6.1f}% rpm={rpm:8.1f} I={current:7.3f} PF={pf:6.3f}')

if rows:
    by_current = max(rows, key=lambda x: x.get('I', x.get('current', 0.0)))
    by_pf = max(rows, key=lambda x: x.get('PF', x.get('pf', 0.0)))
    print('max-current load=', by_current.get('load_pct', 0.0))
    print('max-PF load=', by_pf.get('load_pct', 0.0))
