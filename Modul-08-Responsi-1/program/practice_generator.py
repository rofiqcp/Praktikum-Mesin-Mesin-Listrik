import math

items = [
    ('rpm_to_rad_s', 1500 * 2 * math.pi / 60),
    ('transformer_ratio_example', 220 / 24),
    ('efficiency_example_pct', 180 / 225 * 100),
    ('sync_speed_example_rpm', 120 * 50 / 4),
    ('slip_example_pct', (1500 - 1440) / 1500 * 100),
    ('three_phase_power_factorless_coeff', math.sqrt(3) * 380 * 2.5),
]

print('P08 PRACTICE ANSWER KEY')
for name, value in items:
    print(f'{name:35s} = {value:.4f}')
