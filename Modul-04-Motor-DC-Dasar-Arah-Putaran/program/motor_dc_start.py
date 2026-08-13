"""P04 - Simulasi dasar motor DC.

Menampilkan respons start dinamik dan tabel sweep steady-state.
Bisa dijalankan di VS Code, Google Colab, atau CI tanpa input interaktif.
"""
import math

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

# Parameter contoh motor untuk model pendidikan.
V = 12.0
R = 1.2
L = 0.012
ke = 0.055
kt = 0.055
J = 0.0025
B = 0.0008
load_torque = 0.02


def simulate_start(voltage=V, tmax=2.0, dt=0.0005):
    current = 0.0
    omega = 0.0
    time_data = [0.0]
    current_data = [0.0]
    rpm_data = [0.0]
    emf_data = [0.0]

    for step in range(1, int(tmax / dt) + 1):
        t = step * dt
        di = (voltage - R * current - ke * omega) / L
        effective_load = load_torque if omega > 0.0 else 0.0
        dw = (kt * current - B * omega - effective_load) / J
        current += di * dt
        omega = max(omega + dw * dt, 0.0)

        if step % 20 == 0 or step == int(tmax / dt):
            time_data.append(t)
            current_data.append(current)
            rpm_data.append(omega * 60.0 / (2.0 * math.pi))
            emf_data.append(ke * omega)

    return time_data, current_data, rpm_data, emf_data


def steady_state(voltage, current):
    """Estimasi titik steady-state dari V dan I menggunakan model back-EMF."""
    emf = max(voltage - current * R, 0.0)
    omega = emf / ke if ke else 0.0
    rpm = omega * 60.0 / (2.0 * math.pi)
    torque = kt * current
    pin = voltage * current
    pconv = emf * current
    copper_loss = current * current * R
    return emf, rpm, torque, pin, pconv, copper_loss


if __name__ == "__main__":
    T, I, RPM, E = simulate_start()
    peak_index = max(range(len(I)), key=I.__getitem__)

    print("=== RESPONS START MOTOR DC ===")
    print(f"arus pada t=0     : {I[0]:.3f} A")
    print(f"arus puncak model : {I[peak_index]:.3f} A pada t={T[peak_index]:.3f} s")
    print(f"arus steady akhir : {I[-1]:.3f} A")
    print(f"rpm akhir         : {RPM[-1]:.1f} rpm")
    print(f"back-EMF akhir    : {E[-1]:.3f} V")
    print(f"V/R (batas stall resistif sederhana) = {V/R:.3f} A")

    print("\n=== SWEEP STEADY-STATE ===")
    print(" V(V)  I(A)   E(V)    rpm    T(Nm)  Pin(W)  Pconv(W)  Pcu(W)")
    for voltage in (6.0, 9.0, 12.0):
        for current in (0.5, 1.0, 2.0):
            emf, rpm, tq, pin, pconv, pcu = steady_state(voltage, current)
            print(
                f"{voltage:4.1f}  {current:4.1f}  {emf:6.2f}  {rpm:7.1f}  "
                f"{tq:6.3f}  {pin:6.2f}  {pconv:8.2f}  {pcu:6.2f}"
            )

    if plt:
        plt.figure()
        plt.plot(T, I, label="Armature current (A)")
        plt.plot(T, [rpm / 100.0 for rpm in RPM], label="rpm/100")
        plt.xlabel("time (s)")
        plt.ylabel("scaled response")
        plt.title("P04 - DC Motor Start Response")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig("motor_dc_start_response.png", dpi=150)
        print("\nGrafik tersimpan: motor_dc_start_response.png")
