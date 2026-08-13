from pathlib import Path
import py_compile, sys
root=Path(__file__).resolve().parents[1]
files=sorted(root.glob('Modul-*/program/*.py'))
failed=[]
for f in files:
    try:
        py_compile.compile(str(f),doraise=True)
        print('OK',f.relative_to(root))
    except Exception as e:
        failed.append((f,e)); print('FAIL',f,e)
print(f'\nPython files checked: {len(files)}, failed: {len(failed)}')
sys.exit(1 if failed else 0)
