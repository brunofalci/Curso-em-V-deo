medida = float(input('Uma distancia em m '))

km = medida / 1000
hm = medida / 100
dam = medida /10
m = medida
cm = medida * 100
mm = medida * 1000

print(f'A medida de {medida:.2f}m corresponde a\n{km:.3f}km\n{hm:.2f}hm\n{dam:.1f}dam\n{m:.0f}m\n{cm:.0f}cm\n{mm:.0f}mm')