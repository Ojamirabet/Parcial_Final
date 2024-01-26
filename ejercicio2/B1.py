#Fes un programa que, donat un string, conti les vocals que té.
palabra = input("Dime una palabra: ")
contador_vocales = 0 
vocales = "aeiouAEIOU"
for caracter in palabra: 
    if caracter in vocales:
        contador_vocales += 1
print(palabra,  " tiene", contador_vocales, "vocales")