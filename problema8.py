def calcular_factorial(numero):
    factorial=1
    for i in range(1, numero+1):
        factorial *=i
    return factorial 

numero = int(input("Ingrese un número entero no negativo: "))
if numero < 0:
    print("El número debe ser no negativo.")
else:
    resultado = calcular_factorial(numero)
    print(f"El factorial de {numero} es {resultado}")