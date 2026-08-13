from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
mods=sorted(p for p in root.iterdir() if p.is_dir() and p.name.startswith('Modul-'))
errors=[]
if len(mods)!=16: errors.append(f'Expected 16 modules, found {len(mods)}')
for i,m in enumerate(mods,1):
    prefix=f'Modul-{i:02d}-'
    if not m.name.startswith(prefix): errors.append(f'Ordering/name mismatch: {m.name}, expected prefix {prefix}')
    for req in ['Materi.md','Jobsheet.md']:
        if not (m/req).exists(): errors.append(f'{m.name}: missing {req}')
    if not (m/'program').is_dir(): errors.append(f'{m.name}: missing program directory')
    elif not list((m/'program').glob('*.py')) and i not in []: errors.append(f'{m.name}: missing Python program')
    if i in {8,12,16}:
        if not (m/'Project.md').exists(): errors.append(f'{m.name}: missing Project.md')
        if (m/'TugasVideo.md').exists(): errors.append(f'{m.name}: should use Project.md, not TugasVideo.md')
    else:
        if not (m/'TugasVideo.md').exists(): errors.append(f'{m.name}: missing TugasVideo.md')
print(f'Modules found: {len(mods)}')
if errors:
    print('\n'.join('ERROR '+e for e in errors)); sys.exit(1)
print('Structure OK: 16 modules, required docs and programs are present.')
