def add(x, y):
    return x+y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("select operation.")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        try:

            num1 = float(input("sisesta esimene number:"))
            num2 = float(input("sisesta teine number"))
        except ValueError:
            print("vale sisend. Palun sisesta number")
            continue

        if choice == '1':
           print(num1, "+", num2, "=", add(num1, num2)) 

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))


        next_calculation = input ("teeme järgmise arvutuse? (yes/no): ")
        
        if next_calculation == "no":
            break
        
        else:
            print("invalid input")


