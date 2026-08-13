"""P02 - Analisis transformator 1 fasa tanpa beban.

Program menjalankan dua bagian:
1) sweep rasio tegangan model sederhana;
2) perhitungan PF0, Ic, Im, Rc, dan Xm dari dataset contoh.
Tidak membutuhkan input interaktif sehingga cocok untuk VS Code, Colab, dan CI.
"""
import math

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


def no_load_parameters(v0, i0, p0):
    s0 = v0 * i0
    pf0 = p0 / s0 if s0 else 0.0
    # Clamp untuk mencegah error numerik jika dataset dibulatkan.
    pf0 = max(0.0, min(pf0, 1.0))
    ic = i0 * pf0
    im_sq = max(i0 * i0 - ic * ic, 0.0)
    im = math.sqrt(im_sq)
    rc = v0 / ic if ic else float("inf")
    xm = v0 / im if im else float("inf")
    return s0, pf0, ic, im, rc, xm


def transformer_ratio_sweep():
    ratio = 220.0 / 24.0
    loss_factor = 0.018
    v1_data = [44.0, 88.0, 132.0, 176.0, 220.0]
    rows = []
    for v1 in v1_data:
        v2_ideal = v1 / ratio
        v2_model = v2_ideal * (1.0 - loss_factor * (v1 / 220.0) ** 2)
        i0_model = 0.04 + 0.00045 * v1
        ratio_measured = v1 / v2_model if v2_model else 0.0
        rows.append((v1, v2_ideal, v2_model, i0_model, ratio_measured))
    return rows


if __name__ == "__main__":
    rows = transformer_ratio_sweep()
    print("=== SWEEP RASIO TEGANGAN ===")
    print("V1(V), V2_ideal(V), V2_model(V), I0_model(A), rasio_model")
    for row in rows:
        print(f"{row[0]:.1f}, {row[1]:.3f}, {row[2]:.3f}, {row[3]:.3f}, {row[4]:.3f}")

    print("\n=== PARAMETER TANPA BEBAN ===")
    datasets = [
        (110.0, 0.20, 9.0),
        (165.0, 0.29, 20.0),
        (220.0, 0.40, 35.0),
    ]
    print("V0(V), I0(A), P0(W), S0(VA), PF0, Ic(A), Im(A), Rc(ohm), Xm(ohm)")
    for v0, i0, p0 in datasets:
        s0, pf0, ic, im, rc, xm = no_load_parameters(v0, i0, p0)
        print(
            f"{v0:.1f}, {i0:.3f}, {p0:.1f}, {s0:.2f}, {pf0:.4f}, "
            f"{ic:.4f}, {im:.4f}, {rc:.2f}, {xm:.2f}"
        )

    if plt:
        v1 = [r[0] for r in rows]
        v2_ideal = [r[1] for r in rows]
        v2_model = [r[2] for r in rows]
        plt.figure()
        plt.plot(v1, v2_ideal, "o-", label="ideal")
        plt.plot(v1, v2_model, "s-", label="model sederhana")
        plt.xlabel("V1 (V)")
        plt.ylabel("V2 (V)")
        plt.title("P02 - Rasio Tegangan Transformator")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig("trafo_no_load_ratio.png", dpi=150)
        print("\nGrafik tersimpan: trafo_no_load_ratio.png")