#Se pide un  numero al usuario 
#En esta version se valida que el numero sea positivo, si se teclea un numeronegativo marca error
numero = int(input("Teclea un numero positivo:"))
if numero < 0 :
    print("Error-> El numero debe ser positivo")
else:
    print(f"El numero que se tecleo fue {numero}")
    print("Fin del programa")

