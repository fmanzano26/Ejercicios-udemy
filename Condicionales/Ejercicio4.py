
v1 = float(input("Introduce el primer valor :"))
v2 = float(input("Introduce el segundo valor :"))
oper = input("especifica la operacion (s,r,m,d) :")

if oper=='s':
    suma = v1+v2
    print(f"el resultado de la suma es {suma}")
elif oper=='r':
    resta = v1-v2
    print(f"el resultado de la resta es {resta}")
elif oper=='m':
    multiplicacion = v1*v2
    print(f"el resultado de la multiplicacion es {multiplicacion}")
elif oper=='d':
    division = v1/v2
    print(f"el resultado de la division es {division:.2f}")
else:
    print("se equivoco de operacion")