#Se pide un  numero al usuario 
#En esta version se valida que el numero sea positivo, 
#si se teclea un numeronegativo marca error y se vuelve a pedir el numero
while True:
    numero = int(input("Teclea un numero positivo:"))
    if numero < 0 :
        print("Error-> El numero debe ser positivo")
    else:
        print(f"El numero que se tecleo fue {numero}")
        print("Fin del programa")
        break


