def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
          
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def main():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ").strip()
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    try:
        if choice == '1':
            print(f"Result = {add(a, b)}")
        elif choice == '2':
            print(f"Result = {subtract(a, b)}")
        elif choice == '3':
            print(f"Result = {multiply(a, b)}")
        elif choice == '4':
            print(f"Result = {divide(a, b)}")
        else:
            print("Invalid choice.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()
