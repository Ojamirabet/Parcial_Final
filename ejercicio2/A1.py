#Fes un programa que, donats dos nombres (enters o decimals) ens digui si un nombre és més gran que l’altre o si són iguals. 
numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime otro numero: "))

if numero1 == numero2:
    print("Els numeros son iguals")
elif numero1 > numero2:
    print(str(numero1) + " es mayor que " + str(numero2))
else:
    print(str(numero2) + " es mayor que " + str(numero1))

