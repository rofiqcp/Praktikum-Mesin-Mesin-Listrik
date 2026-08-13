"""P14 - Analisis dataset OCC dan V-curve mesin sinkron."""
import csv
import math
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

path = Path(__file__).with_name("data_synchronous.csv")
rows = []
with path.open(newline="", encoding="utf-8") as f:
    for raw in csv.DictReader(f):
        r = {
            "kind": raw["kind"],
            "load_pct": float(raw["load_pct"]),
            "If": float(raw["If"]),
            "V": float(raw["V"]),
            "Ia": float(raw["Ia"]),
            "PF": float(raw["PF"]),
            "rpm": float(raw["rpm"]),
            "poles": int(raw["poles"]),
        }
        r["f"] = r["poles"] * r["rpm"] / 120.0
        r["S"] = math.sqrt(3.0) * r["V"] * r["Ia"] if r["Ia"] else 0.0
        r["P"] = r["S"] * r["PF"] if r["Ia"] else 0.0
        r["Q_mag"] = math.sqrt(max(r["S"] ** 2 - r["P"] ** 2, 0.0)) if r["Ia"] else 0.0
        flags = []
        if r["poles"] <= 0:
            flags.append("POLES")
        if not 0.0 <= r["PF"] <= 1.0:
            flags.append("PF")
        if r["rpm"] < 0:
            flags.append("RPM")
        r["flags"] = "|".join(flags) if flags else "OK"
        rows.append(r)

occ = [r for r in rows if r["kind"] == "OCC"]
vcurve = [r for r in rows if r["kind"] == "VCURVE"]

print("kind,If,V,Ia,PF,rpm,f,P,Qmag,flags")
for r in rows:
    print(f"{r['kind']},{r['If']:.2f},{r['V']:.1f},{r['Ia']:.2f},{r['PF']:.2f},{r['rpm']:.0f},{r['f']:.2f},{r['P']:.1f},{r['Q_mag']:.1f},{r['flags']}")

if vcurve:
    minimum = min(vcurve, key=lambda r: r["Ia"])
    print(f"vcurve_min=If {minimum['If']:.2f} A, Ia {minimum['Ia']:.2f} A, PF {minimum['PF']:.2f}")

if len(occ) >= 2:
    slopes = []
    for a, b in zip(occ, occ[1:]):
        dif = b["If"] - a["If"]
        slopes.append((b["If"], (b["V"] - a["V"]) / dif if dif else 0.0))
    print("occ_incremental_slopes=", ", ".join(f"If={x:.1f}:{m:.1f} V/A" for x, m in slopes))

if plt:
    if occ:
        plt.figure()
        plt.plot([r["If"] for r in occ], [r["V"] for r in occ], "o-")
        plt.xlabel("Field current If (A)")
        plt.ylabel("No-load voltage (V)")
        plt.title("P14 - OCC")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("p14_occ.png", dpi=150)
    if vcurve:
        plt.figure()
        plt.plot([r["If"] for r in vcurve], [r["Ia"] for r in vcurve], "o-")
        plt.xlabel("Field current If (A)")
        plt.ylabel("Armature current Ia (A)")
        plt.title("P14 - V-curve")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("p14_vcurve.png", dpi=150)
