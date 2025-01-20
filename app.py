def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Select an operation (1-5): "))

            if choice == 5:
                print("Exiting the calculator. Goodbye!")
                break

            if choice in [1, 2, 3, 4]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    print(f"Result: {add(num1, num2)}")
                elif choice == 2:
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == 3:
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == 4:
                    print(f"Result: {divide(num1, num2)}")
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
