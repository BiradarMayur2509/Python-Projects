number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")   

# Convert inputs to floats so both integers and decimals can be handled

num1 = float(number_1)
num2 = float(number_2)

# if user input is abc, the program will crash with a ValueError

print("Numbers are:", num1, "and", num2)
print("Add:", num1 + num2)

