import math
caps=[5,10,15,20,30,40]
def xc(f,c): return 1/(2*math.pi*f*c*1e-6)
print('C_uF,Xc_50Hz,Xc_60Hz')
for c in caps:
    print(f'{c},{xc(50,c):.2f},{xc(60,c):.2f}')
