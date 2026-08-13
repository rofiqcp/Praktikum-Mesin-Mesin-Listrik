def ramp_profile(ramp_s, f_target=50.0, v_target=1.0, dt=0.5):
    n = int(ramp_s / dt) + 1
    out = []
    for i in range(n + 1):
        t = min(i * dt, ramp_s)
        ratio = 1.0 if ramp_s == 0 else t / ramp_s
        f_pu = ratio
        v_pu = ratio
        out.append((t, f_target * f_pu, v_target * v_pu))
    return out


if __name__ == '__main__':
    for ramp in [2.0, 5.0, 10.0]:
        p = ramp_profile(ramp)
        print(f'=== ramp {ramp:.1f}s ===')
        for t, f, v in p:
            print(f't={t:5.1f}s f={f:6.2f}Hz Vpu={v:5.3f}')
        print()
