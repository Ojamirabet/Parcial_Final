print("Per a què fem servir sentències de repetició? Posa exemples.")
print("Utilizariamos sentencias de repeticon cuando queremos hacer un programa que repita mas de una vez una serie de comandos como por ejemplo: ")
lista = []
contador = 0
while contador <3:
    lista.append(int(input("Dime un numero: ")))
    contador +=1
print(lista)