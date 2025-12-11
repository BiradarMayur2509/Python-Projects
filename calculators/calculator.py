def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice (1/2/3/4): ").strip()
            
a = get_number("Enter the first number: ")
b = get_number("Enter the second number: ")

if choice == '1':
    print("result:", a + b)
elif choice == '2':
    print("result:", a - b)
elif choice == '3':
    print("result:", a * b)
elif choice == '4':
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("result:", a / b)
else:
    print("Invalid choice.")
