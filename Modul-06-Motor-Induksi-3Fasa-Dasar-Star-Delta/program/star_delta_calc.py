from math import sqrt
f=50.0; poles=4; vl=380.0; nr=1442.0; il_delta=3.2
ns=120*f/poles
slip=(ns-nr)/ns
vph_star=vl/sqrt(3); vph_delta=vl
iph_delta=il_delta/sqrt(3)
print(f'Ns={ns:.1f} rpm, Nr={nr:.1f} rpm, slip={100*slip:.3f}%')
print(f'Star: Vph={vph_star:.2f} V, IL=Iph')
print(f'Delta: Vph={vph_delta:.2f} V, jika IL={il_delta:.2f}A maka Iph={iph_delta:.2f}A')
print('PERINGATAN: pilih star/delta berdasarkan nameplate, bukan sekadar hasil rumus.')