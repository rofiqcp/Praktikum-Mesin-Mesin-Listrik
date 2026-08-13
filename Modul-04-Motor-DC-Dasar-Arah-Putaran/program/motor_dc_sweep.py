from motor_dc_start import steady_state

if __name__ == "__main__":
    print("V,I,E,rpm,T,Pin,Pconv,Pcu")
    for voltage in (6.0, 9.0, 12.0):
        for current in (0.5, 1.0, 2.0):
            e, rpm, tq, pin, pconv, pcu = steady_state(voltage, current)
            print(f"{voltage:.1f},{current:.1f},{e:.2f},{rpm:.1f},{tq:.3f},{pin:.2f},{pconv:.2f},{pcu:.2f}")
