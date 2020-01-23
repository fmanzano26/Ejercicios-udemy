saldo = 1000

print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero en la cuenta")
print("3. Mostrar dinero en la cuenta")
print("4. Salir")

opcion = int(input("Ingrese una de las opciones: "))

print()

if opcion==1:
   extra = float(input("cuanto dinero desea ingresar: "))
   saldo += extra
   print(f"Dinero en la cuenta {saldo}")
elif opcion==2:
    retirar = float(input("cuanto dinero desea retirar: "))
    if retirar>saldo:
        print("Dinero insuficiente") 
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta {saldo}")
elif opcion==3:
    print(f"su dinero en cuenta es {saldo}")
elif opcion==4:  
    print("Gracias por utilizar su cajero automatico")      
else:
    print("se equivoco de opcion de menu")        