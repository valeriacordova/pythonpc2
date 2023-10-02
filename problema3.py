pares = 0
impares = 0
listanumeros = 0
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if respuesta == "NO":
        break
    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        listanumeros.append(numero)
        if numero % 2 == 0:
            pares += 1  # Si es par, incrementamos el contador de pares
        else:
            impares += 1  # Si es impar, incrementamos el contador de impares
    else:
        print("Respuesta no válida. Por favor, responda 'SI' o 'NO'.")

# Mostramos los resultados
print("Numeros:",listanumeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)