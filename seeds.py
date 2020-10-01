power = int(63)
b = int(1)
c = int(0)
areaN = float(502.7)  # km2
areaNO = float(178200)  # km2
areaR = float(17100000)  # km2
areaP = float(16.695)  # mm2
heightP = float(2.5)  # mm
yieldNO = int(1706000) #tons/year
yieldR = int(127500000)  #tons/year
while power > 0:
    b = b * 2
    c = c + b
    power = power - 1

amount = c + 1
massP = amount * 50 / 1000000000
print amount, 'grains of wheat'
print massP, 'tons'

hNm =((amount * areaP) / 1000000000000 / areaN) * heightP / 1000  # sloy phenitsi na novosibirsk
hNkm = ((amount * areaP) / 1000000000000 / areaN) * heightP / 1000000
hNOm = ((amount * areaP) / 1000000000000 / areaNO) * heightP / 1000  # sloy phenitsi na novosibirskaya obl
hRm = ((amount * areaP) / 1000000000000 / areaR) * heightP / 1000  # sloy phenitsi na Russia
hRcm = ((amount * areaP) / 1000000000000 / areaR) * heightP / 10
print hNm, 'meters above Novosibirsk or', hNkm, 'kilometers above Novosibirsk'
print hNOm, 'meters above Novosibirskaya Oblast'
print hRm, 'meters above Russia or', hRcm, 'centimeters above Russia'

yearsNO = massP / yieldNO
yearsR = massP / yieldR
print yearsNO, 'years it will take to grow all this wheat in Novosibirskaya Oblast'
print yearsR, 'years it will take to grow all this wheat in Russia'
