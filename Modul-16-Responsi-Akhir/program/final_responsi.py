import random
bank=[
 ('Trafo: Vnl=24.6 V, Vfl=22.8 V. Regulasi (%)', lambda:(24.6-22.8)/22.8*100),
 ('Motor induksi 4 pole 50 Hz, Nr=1440 rpm. Slip (%)', lambda:(1500-1440)/1500*100),
 ('Motor DC V=12 V, I=2 A, Ra=1 ohm. Back-EMF (V)', lambda:12-2*1),
 ('Generator 4 pole 1500 rpm. Frekuensi (Hz)', lambda:4*1500/120),
 ('Pin=1000 W, Pout=820 W. Efisiensi (%)', lambda:82)
]
q,fn=random.choice(bank); ans=fn(); print(q)
try:
 user=float(input('Jawab: ')); print('BENAR' if abs(user-ans)<=max(.05,abs(ans)*.01) else f'Belum tepat; acuan {ans:.3f}')
except ValueError:
 print(f'Input bukan angka; acuan {ans:.3f}')
print('Lanjutkan dengan penjelasan lisan tentang makna hasil.')