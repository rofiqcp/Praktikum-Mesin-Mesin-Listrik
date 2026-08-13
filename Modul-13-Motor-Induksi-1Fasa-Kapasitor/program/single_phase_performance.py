"""P13 - Analisis dataset performa motor satu fasa."""
import csv
import math
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

F_HZ = 50.0
POLES = 4
NS = 120.0 * F_HZ / POLES
PATH = Path(__file__).with_name("data_single_phase.csv")

rows = []
with PATH.open(newline="", encoding="utf-8") as f:
    for raw in csv.DictReader(f):
        r = {k: float(v) for k, v in raw.items()}
        r["slip_pct"] = (NS - r["rpm"]) / NS * 100.0
        r["pin"] = r["V"] * r["I"] * r["PF"]
        omega = 2.0 * math.pi * r["rpm"] / 60.0
        r["pout"] = r["torque"] * omega
        r["eta"] = 100.0 * r["pout"] / r["pin"] if r["pin"] > 0 else 0.0
        flags = []
        if not 0.0 <= r["PF"] <= 1.0:
            flags.append("PF_RANGE")
        if r["rpm"] > NS:
            flags.append("RPM_ABOVE_NS")
        if r["pout"] > r["pin"] * 1.001:
            flags.append("POUT_GT_PIN")
        if r["eta"] > 100.0:
            flags.append("ETA_GT_100")
        r["flags"] = "|".join(flags) if flags else "OK"
        rows.append(r)

print(f"Ns={NS:.1f} rpm")
print("load,I,PF,rpm,slip,Pin,Pout,eta,temp,flags")
for r in rows:
    print(f"{r['load_pct']:.0f},{r['I']:.2f},{r['PF']:.2f},{r['rpm']:.0f},{r['slip_pct']:.2f},{r['pin']:.1f},{r['pout']:.1f},{r['eta']:.1f},{r['temp']:.0f},{r['flags']}")

max_i = max(rows, key=lambda r: r["I"])
max_slip = max(rows, key=lambda r: r["slip_pct"])
best_eta = max(rows, key=lambda r: r["eta"])
print(f"max_current=load {max_i['load_pct']:.0f}% -> {max_i['I']:.2f} A")
print(f"max_slip=load {max_slip['load_pct']:.0f}% -> {max_slip['slip_pct']:.2f}%")
print(f"best_eta=load {best_eta['load_pct']:.0f}% -> {best_eta['eta']:.1f}%")

if plt:
    x = [r["load_pct"] for r in rows]
    for key, ylabel, filename in [
        ("I", "Current (A)", "single_phase_current.png"),
        ("rpm", "Speed (rpm)", "single_phase_speed.png"),
        ("slip_pct", "Slip (%)", "single_phase_slip.png"),
        ("eta", "Efficiency (%)", "single_phase_efficiency.png"),
    ]:
        plt.figure()
        plt.plot(x, [r[key] for r in rows], "o-")
        plt.xlabel("Load (%)")
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(filename, dpi=150)
