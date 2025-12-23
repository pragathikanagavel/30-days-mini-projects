import math

history = []

def show_menu():
    print("\n Scientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Logarithm (base 10)")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. View History")
    print("12. Exit")

while True:
    show_menu()

    try:
        choice = int(input("Enter your choice (1-12): "))

        if choice == 12:
            print("Exiting Calculator. Goodbye!")
            break

        if choice == 11:
            print("\n Calculation History:")
            if not history:
                print("No calculations yet.")
            else:
                for h in history:
                    print(h)
            continue

        if choice in [1, 2, 3, 4, 5]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

        if choice == 1:
            result = a + b
            expression = f"{a} + {b} = {result}"

        elif choice == 2:
            result = a - b
            expression = f"{a} - {b} = {result}"

        elif choice == 3:
            result = a * b
            expression = f"{a} * {b} = {result}"

        elif choice == 4:
            if b == 0:
                print("Division by zero not allowed")
                continue
            result = a / b
            expression = f"{a} / {b} = {result}"

        elif choice == 5:
            result = math.pow(a, b)
            expression = f"{a}^{b} = {result}"

        elif choice == 6:
            x = float(input("Enter number: "))
            result = math.sqrt(x)
            expression = f"√{x} = {result}"

        elif choice == 7:
            x = float(input("Enter number: "))
            result = math.log10(x)
            expression = f"log({x}) = {result}"

        elif choice == 8:
            x = float(input("Enter angle in degrees: "))
            result = math.sin(math.radians(x))
            expression = f"sin({x}) = {result}"

        elif choice == 9:
            x = float(input("Enter angle in degrees: "))
            result = math.cos(math.radians(x))
            expression = f"cos({x}) = {result}"

        elif choice == 10:
            x = float(input("Enter angle in degrees: "))
            result = math.tan(math.radians(x))
            expression = f"tan({x}) = {result}"

        else:
            print("Invalid choice")
            continue

        print("Result:", result)
        history.append(expression)

    except ValueError:
        print("Invalid input. Please enter numbers only.")

