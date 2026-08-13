"""P16 - Latihan responsi akhir interaktif lintas topik."""
import math
import random

bank = [
    ("TRAFO", "Vnl=24.6 V, Vfl=22.8 V. Regulasi (%)", lambda: (24.6-22.8)/22.8*100),
    ("TRAFO", "V1=220 V, V2=24 V. Rasio V1/V2", lambda: 220/24),
    ("MOTOR_DC", "V=12 V, I=2 A, Ra=1 ohm. Back-EMF (V)", lambda: 12-2*1),
    ("MOTOR_DC", "T=0.5 Nm, n=1200 rpm. Daya mekanik (W)", lambda: 0.5*(2*math.pi*1200/60)),
    ("IM3P", "Motor 4 pole 50 Hz. Ns (rpm)", lambda: 120*50/4),
    ("IM3P", "Ns=1500 rpm, Nr=1440 rpm. Slip (%)", lambda: (1500-1440)/1500*100),
    ("IM3P", "Slip 4%, f=50 Hz. Frekuensi rotor (Hz)", lambda: 0.04*50),
    ("IM1P", "f=50 Hz, C=20 uF. Xc (ohm)", lambda: 1/(2*math.pi*50*20e-6)),
    ("SYNC", "Generator 4 pole 1500 rpm. Frekuensi (Hz)", lambda: 4*1500/120),
    ("DAYA", "Pin=1000 W, Pout=820 W. Efisiensi (%)", lambda: 82.0),
]

category, question, fn = random.choice(bank)
answer = fn()
print(f"[{category}] {question}")
try:
    user = float(input("Jawab: "))
    tolerance = max(0.05, abs(answer)*0.01)
    if abs(user-answer) <= tolerance:
        print("BENAR")
    else:
        print(f"Belum tepat; acuan {answer:.3f}")
except ValueError:
    print(f"Input bukan angka; acuan {answer:.3f}")

print("Lanjutkan dengan penjelasan lisan: rumus, satuan, arti fisik, dan pemeriksaan kewajaran hasil.")
