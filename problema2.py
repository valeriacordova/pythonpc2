
h = int(input('Ingrese la altura del triangulo: '))

for i in range(h):
    print('#' * (i+1))
for i in range(h-1,0,-1):
    print ('#'*i)