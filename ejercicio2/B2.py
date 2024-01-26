#Encapsula aquesta lògica en una funció.
def contar_vocales(palabra):
    contador_vocales = 0 
    vocales = "aeiouAEIOU"
    for caracter in palabra: 
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales


palabra = input("Dime una palabra: ")
resultado = contar_vocales(palabra)
print(palabra,  " tiene", resultado, "vocales")
