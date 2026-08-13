import csv
from pathlib import Path
p=Path(__file__).with_name('multi_machine_cases.csv')
rows=list(csv.DictReader(p.open(encoding='utf-8')))
print('case,machine,metric,deviation_pct')
for r in rows:
    ref=float(r['reference']); val=float(r['measured'])
    dev=(val-ref)/abs(ref)*100 if ref else 0
    print(f"{r['case_id']},{r['machine']},{r['metric']},{dev:.2f}")
print(f'rows={len(rows)}')
