"""P01 - Peta konsep dan kalkulator dasar mesin-mesin listrik."""
from math import pi, sqrt

systems = {
    "Transformator": {
        "conversion": "AC -> medan magnet -> AC",
        "variables": "V, I, rasio, rugi, regulasi, efisiensi",
        "meeting": "P2-P3",
    },
    "Motor DC": {
        "conversion": "DC -> medan magnet -> mekanik",
        "variables": "V, I, back-EMF, rpm, torsi",
        "meeting": "P4-P5",
    },
    "Motor Induksi": {
        "conversion": "AC -> medan putar -> mekanik",
        "variables": "f, pole, Ns, Nr, slip, PF",
        "meeting": "P6, P9-P11",
    },
    "Mesin Sinkron": {
        "conversion": "listrik <-> mekanik pada kecepatan sinkron",
        "variables": "f, pole, Ns, eksitasi, PF",
        "meeting": "P14",
    },
}

print("=== PETA MESIN-MESIN LISTRIK ===")
for name, info in systems.items():
    print(f"- {name:15s} | {info['conversion']}")
    print(f"  variabel: {info['variables']} | materi: {info['meeting']}")

# Contoh 1: transformator ideal
v1, n1, n2 = 220.0, 500.0, 100.0
ratio = n1 / n2
v2 = v1 / ratio
print(f"\nTrafo ideal: a={ratio:.2f}, V2={v2:.2f} V")

# Contoh 2: motor DC
v, i, rpm, torque = 24.0, 2.0, 1200.0, 0.25
pin = v * i
omega = 2 * pi * rpm / 60
pmech = torque * omega
eta = pmech / pin * 100
print(f"Motor DC: Pin={pin:.2f} W, omega={omega:.2f} rad/s, Pmech={pmech:.2f} W, eta={eta:.2f}%")

# Contoh 3: motor induksi
f, poles, nr = 50.0, 4, 1440.0
ns = 120 * f / poles
slip = (ns - nr) / ns
print(f"Motor induksi: Ns={ns:.0f} rpm, Nr={nr:.0f} rpm, slip={100*slip:.2f}%")

# Contoh 4: daya 3 fasa
vl, il, pf = 380.0, 2.5, 0.82
p3 = sqrt(3) * vl * il * pf
print(f"Daya aktif 3 fasa contoh: {p3:.1f} W")

print("\nWorkflow belajar: teori -> model/simulasi -> dataset -> program -> grafik -> kesimpulan")