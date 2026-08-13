from math import pi

v1=220.0; n1=500.0; n2=100.0
print(f"V2 ideal = {v1*n2/n1:.2f} V")

v=24.0; i=2.0; rpm=1200.0; torque=0.25
pin=v*i; omega=2*pi*rpm/60; pmech=torque*omega
print(f"DC example: Pin={pin:.2f} W, omega={omega:.2f} rad/s, Pmech={pmech:.2f} W")

f=50.0; poles=4; nr=1440.0
ns=120*f/poles; slip=(ns-nr)/ns
print(f"Induction example: Ns={ns:.0f} rpm, slip={100*slip:.2f}%")
