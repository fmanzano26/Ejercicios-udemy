n1 = int(input("Digite un numero :"))      
n2 = int(input("Digite un numero :"))      

if n1%2==0 and n2%2==0:
    print("ambos numeros son pares")
elif n1%2==0 and n2%2!=0:
    print(f"el {n1} es par")
elif n1%2!=0 and n2%2==0:
    print(f"el {n2} es par")
else:
    print("ambos numeros son impares")    
    
       

