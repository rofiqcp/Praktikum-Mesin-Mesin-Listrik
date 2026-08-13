import csv
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def read_data(path):
    rows = []
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            rows.append({k: float(v) for k, v in row.items()})
    return rows


def analyze(rows):
    if not rows:
        return rows
    vnl = rows[0]["V2"]
    imax = max(r["I2"] for r in rows) or 1.0
    for r in rows:
        r["Pout"] = r["V2"] * r["I2"] * r["pf"]
        r["reg"] = 0.0 if r["I2"] == 0 else (vnl - r["V2"]) / r["V2"] * 100.0
        r["eta"] = 0.0 if r["Pin"] == 0 else r["Pout"] / r["Pin"] * 100.0
        r["loss"] = max(r["Pin"] - r["Pout"], 0.0)
        r["pcu_rel"] = (r["I2"] / imax) ** 2
    return rows


if __name__ == "__main__":
    path = Path(__file__).with_name("data_trafo.csv")
    rows = analyze(read_data(path))
    print("load,V2,I2,pf,Pout,reg,eta,loss,Pcu_rel")
    for r in rows:
        print(
            f"{r['load_pct']:.0f},{r['V2']:.2f},{r['I2']:.2f},{r['pf']:.2f},"
            f"{r['Pout']:.2f},{r['reg']:.2f},{r['eta']:.2f},{r['loss']:.2f},{r['pcu_rel']:.3f}"
        )

    active = [r for r in rows if r["I2"] > 0]
    if active:
        best = max(active, key=lambda r: r["eta"])
        print(f"best_eta={best['eta']:.2f}% at load={best['load_pct']:.0f}%")

    if plt and rows:
        x = [r["load_pct"] for r in rows]
        plt.figure()
        plt.plot(x, [r["reg"] for r in rows], "o-", label="regulasi %")
        plt.plot(x, [r["eta"] for r in rows], "s-", label="efisiensi %")
        plt.xlabel("Beban (%)")
        plt.ylabel("Persen")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig("trafo_regulasi_efisiensi.png", dpi=150)
        print("saved=trafo_regulasi_efisiensi.png")