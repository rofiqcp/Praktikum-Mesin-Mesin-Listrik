from pathlib import Path
import subprocess,sys,os
root=Path(__file__).resolve().parents[1]
interactive={'responsi_quiz.py','final_responsi.py'}
files=sorted(f for f in root.glob('Modul-*/program/*.py') if f.name not in interactive)
env=os.environ.copy(); env['MPLBACKEND']='Agg'
failed=[]
for f in files:
    print('\nRUN',f.relative_to(root))
    p=subprocess.run([sys.executable,f.name],cwd=f.parent,env=env,text=True,capture_output=True,timeout=30)
    print(p.stdout[:2000])
    if p.returncode:
        failed.append((f,p.stderr)); print(p.stderr[:2000])
print(f'\nPrograms run: {len(files)}, failed: {len(failed)}')
sys.exit(1 if failed else 0)
