from math import sqrt

systems = {
    'Transformator': 'AC -> magnetik -> AC',
    'Motor DC': 'DC -> magnetik -> mekanik',
    'Motor Induksi': '3ph AC -> medan putar -> mekanik',
    'Mesin Sinkron': 'mekanik/AC + eksitasi -> AC/mekanik'
}
print('PETA MESIN LISTRIK')
for k,v in systems.items(): print(f'- {k:15s}: {v}')

f=50; poles=4; nr=1440
ns=120*f/poles
slip=(ns-nr)/ns
vl=380; il=2.5; pf=.82
p3=sqrt(3)*vl*il*pf
print(f'\nContoh motor induksi: Ns={ns:.0f} rpm, Nr={nr} rpm, slip={100*slip:.2f}%')
print(f'Contoh daya 3 fasa: {p3:.1f} W')
print('Alur praktikum: teori -> simulasi -> wiring OFF -> verifikasi -> energize -> ukur -> analisa')