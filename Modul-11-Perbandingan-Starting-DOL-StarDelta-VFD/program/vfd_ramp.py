def ramp_profile(ramp_s, f_target=50.0, v_target=1.0, dt=0.5):
    if ramp_s < 0 or dt <= 0:
        raise ValueError('ramp_s must be >= 0 and dt must be > 0')
    if ramp_s == 0:
        return [(0.0, f_target, v_target)]

    out = []
    steps = int(ramp_s / dt)
    for i in range(steps + 1):
        t = i * dt
        ratio = min(t / ramp_s, 1.0)
        out.append((t, f_target * ratio, v_target * ratio))

    if out[-1][0] < ramp_s:
        out.append((ramp_s, f_target, v_target))
    return out


if __name__ == '__main__':
    for ramp in [2.0, 5.0, 10.0]:
        p = ramp_profile(ramp)
        print(f'=== ramp {ramp:.1f}s ===')
        for t, f, v in p:
            print(f't={t:5.1f}s f={f:6.2f}Hz Vpu={v:5.3f}')
        print()
