import math

f = 50.0
poles = 4
Vth_base = 210.0
Rth = 1.1
Xth = 1.8
R2_base = 0.9
X2 = 1.6

ns_rpm = 120.0 * f / poles
ws = 2.0 * math.pi * ns_rpm / 60.0


def torque_at_slip(s, vth=Vth_base, r2=R2_base):
    r = r2 / s
    den = ws * ((Rth + r) ** 2 + (Xth + X2) ** 2)
    return 3.0 * vth**2 * r / den


def sweep(label, vth=Vth_base, r2=R2_base):
    slips = [i / 1000.0 for i in range(1, 1001)]
    torques = [torque_at_slip(s, vth, r2) for s in slips]
    i_max = max(range(len(torques)), key=torques.__getitem__)
    s_max = slips[i_max]
    rpm_max = (1.0 - s_max) * ns_rpm
    print(
        f"{label:20s} | Tstart={torque_at_slip(1.0, vth, r2):7.2f} Nm | "
        f"Tmax={torques[i_max]:7.2f} Nm | s@Tmax={s_max:6.3f} | rpm={rpm_max:7.1f}"
    )


print(f"Ns = {ns_rpm:.1f} rpm")
print("=== SWEEP TEGANGAN ===")
for factor in [0.90, 1.00, 1.10]:
    sweep(f"Vth {factor:.0%}", vth=Vth_base * factor)

print("\n=== SWEEP RESISTANSI ROTOR ===")
for factor in [0.50, 1.00, 1.50, 2.00]:
    sweep(f"R2 {factor:.0%}", r2=R2_base * factor)

print("\nCatatan: parameter adalah model akademik. Bandingkan tren, bukan menganggapnya data motor tertentu.")
