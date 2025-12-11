def get_number(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
a = get_number("Enter the first number: ")
b = get_number("Enter the second number: ")

print("Numbers are:", a, "and", b)
print(Add:, a + b)