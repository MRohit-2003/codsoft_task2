def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

print("Available operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5.Exit")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
choice = int(input("Enter your choice of operation: "))
result = None

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)
elif choice == 5:
    print("GoodBye!")
    exit()  
else:
    print("Invalid input")

if result is not None:
    print("Result:", result)
