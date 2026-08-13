# Formula Ringkas Responsi 1

## Umum
`omega = 2*pi*n/60`  
`Pmek = T*omega`  
`eta = Pout/Pin*100%`

## Transformator
`V1/V2 = N1/N2`  
`PF0 = P0/(V0*I0)`  
`Rc = V0^2/P0`  
`Ic = P0/V0`  
`Im = sqrt(I0^2-Ic^2)`  
`Xm = V0/Im`  
`VR = (Vnl-Vload)/Vload*100%`

## Motor DC
`V = E + Ia*Ra`  
`E = Ke*omega`  
`T = Kt*Ia`  
`Pin = V*Ia`  
`Pcu = Ia^2*Ra`  
`Pout = T*omega`

## Motor Induksi
`Ns = 120*f/P`  
`s = (Ns-Nr)/Ns`  
`fr = s*f`  
`P3 = sqrt(3)*VL*IL*PF`

Star: `VL=sqrt(3)*Vph`, `IL=Iph`  
Delta: `VL=Vph`, `IL=sqrt(3)*Iph`

## Logika
Invariant utama:

- FWD dan REV tidak boleh aktif bersamaan.
- STAR dan DELTA tidak boleh aktif bersamaan.
- fault membuat state kembali ke kondisi aman pada model.

Gunakan formula setelah menuliskan diketahui, ditanya, satuan, dan konteks soal.