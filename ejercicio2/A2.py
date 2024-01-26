#Encapsula aquesta lògica en una funció.
def comparar_numeros():
    numero1 = int(input("Dime un numero: "))
    numero2 = int(input("Dime otro numero: "))

    if numero1 == numero2:
        print("Los números son iguales")
    elif numero1 > numero2:
        print(str(numero1) + " es mayor que " + str(numero2))
    else:
        print(str(numero2) + " es mayor que " + str(numero1))

comparar_numeros()
