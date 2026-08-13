questions=[
 ('Trafo 220/24 V diberi 110 V primer. V2 ideal?',12.0),
 ('Motor 4 pole 50 Hz: Ns rpm?',1500.0),
 ('Nr=1440 rpm dan Ns=1500 rpm: slip %?',4.0),
 ('Pout=180 W, Pin=225 W: efisiensi %?',80.0)
]
score=0
for q,a in questions:
 try: x=float(input(q+' '))
 except ValueError: x=1e99
 ok=abs(x-a)<=max(0.05,abs(a)*0.01)
 print('BENAR' if ok else f'SALAH, acuan {a}')
 score+=ok
print(f'Skor {score}/{len(questions)}')
print('Pertanyaan lisan: mengapa interlock FWD/REV dan STAR/DELTA wajib?')