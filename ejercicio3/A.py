# Fes una funció que donada una llista de nombres enters, ens mostri quin és l’element més gran i quin l’element més petit.
def encontrar_extremos(lista):
    maximo = minimo = lista[0]
    for numero in lista[1:]:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
    return maximo, minimo
numeros = [5, 2, 8, 1, 9, 3]
maximo, minimo = encontrar_extremos(numeros)
print("Lista:" + str(numeros))
print("Elemento más grande:" + str(maximo))
print("Elemento más pequeño:" + str(minimo))
