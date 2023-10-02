def eliminar_vocales(texto):
    vocales="AEIOUaeiou"
    resultado = " "
    for caracter in texto:
        if caracter not in vocales:
            resultado += caracter  
    return resultado
texto = input("Input: ")
texto_sin_vocales = eliminar_vocales(texto)
print("Output:", texto_sin_vocales)