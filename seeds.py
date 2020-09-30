degree = int(63)
b = int(1)
c = int(0)
while degree > 0:
    b = b*2
    c = c + b
    degree = degree - 1

amount = c + 1
mass = amount*50/1000000000

print amount, 'grains of wheat'
print mass, 'tons'
