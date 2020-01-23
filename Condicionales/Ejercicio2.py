
num1 = int(input("Digite el primer numero :"))
num2 = int(input("Digite el segundo numero :"))
num3 = int(input("Digite el tercer numero :"))

if num1>=num2 and num1>=3:
    print(f"el {num1} es el mayor")
elif num2>=num1 and num2>=num3:
    print(f"el {num2} es el mayor")
elif num3>=num1 and num3>=num2:
    print(f"el {num3} es el mayor")
