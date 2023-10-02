numero = int(input("Ingrese el número: "))
digito = int(input("Ingrese el digito: "))

def contar(numero, digito):
    raiz = str(numero)
    cantidad = raiz.count(str(digito))
    return cantidad

cantidad = contar(numero, digito)
print(f"Cantidad de veces {digito} en el número: {cantidad}")