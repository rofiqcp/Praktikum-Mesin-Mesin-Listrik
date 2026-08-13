import math

def signed_angle(deg):
    return ((deg + 180.0) % 360.0) - 180.0

def clock_angle(clock):
    if not 0 <= clock <= 11:
        raise ValueError('clock must be 0..11')
    deg = clock * 30.0
    return deg, signed_angle(deg)

def line_ratio(a, primary, secondary):
    if a <= 0:
        raise ValueError('a must be positive')
    factor = {'Y': math.sqrt(3.0), 'D': 1.0}
    if primary not in factor or secondary not in factor:
        raise ValueError('connection must be Y or D')
    return a * factor[primary] / factor[secondary]

def deviation_indicator(values):
    if len(values) != 3 or any(v < 0 for v in values):
        raise ValueError('three non-negative line values required')
    avg = sum(values) / 3.0
    return 0.0 if avg == 0 else max(abs(v-avg) for v in values) / avg * 100.0

print('clock,angle_0_360,angle_signed')
for c in [0,1,5,6,11]:
    a,b=clock_angle(c); print(f'{c},{a:.0f},{b:.0f}')
print('\nconnection,line_ratio_for_a5')
for p,s in [('Y','Y'),('D','D'),('Y','D'),('D','Y')]:
    print(f'{p}-{s},{line_ratio(5.0,p,s):.4f}')
vals=[380.0,378.0,382.0]
print(f'\nline_values={vals} deviation_indicator={deviation_indicator(vals):.3f}%')
