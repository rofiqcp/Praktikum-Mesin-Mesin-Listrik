"""P16 - Bank latihan numerik lintas topik."""
import math

questions = [
    ("Trafo ratio V1=220 V, V2=24 V", 220/24, "ratio"),
    ("Regulation Vnl=24.6 V, Vfl=22.8 V", (24.6-22.8)/22.8*100, "%"),
    ("DC back-EMF V=12 V, I=2 A, R=1 ohm", 12-2*1, "V"),
    ("Mechanical power T=2 Nm, n=1500 rpm", 2*(2*math.pi*1500/60), "W"),
    ("Induction Ns 4 pole 50 Hz", 120*50/4, "rpm"),
    ("Induction slip Ns=1500, Nr=1440", (1500-1440)/1500*100, "%"),
    ("Rotor frequency s=0.04, f=50 Hz", 0.04*50, "Hz"),
    ("Capacitive reactance f=50 Hz, C=20 uF", 1/(2*math.pi*50*20e-6), "ohm"),
    ("Synchronous frequency 4 pole, 1500 rpm", 4*1500/120, "Hz"),
    ("Efficiency Pin=1000 W, Pout=820 W", 820/1000*100, "%"),
]

print("P16 FINAL PRACTICE BANK")
for i, (text, answer, unit) in enumerate(questions, 1):
    print(f"{i:02d}. {text}")
    print(f"    answer={answer:.3f} {unit}")
print(f"total={len(questions)}")
