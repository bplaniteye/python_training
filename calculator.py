# Ask the user the first number
first_number = input("1. Entrez un nombre : ")
# Check if the input is a number
while not first_number.isdigit():
    print("Votre entrée n'est pas correcte")
    first_number = input("1. Entrez un nombre : ")    
# Ask the user the second number
second_number = input("2. Entrez un nombre : ")
# Check if the input is a number
while not second_number.isdigit():
    print("Votre entrée n'est pas correcte")
    second_number = input("2. Entrez un nombre : ")
# Addition of the 2 numbers
result = int(first_number) + int(second_number)
# Print the result
print(f"Addition : {first_number} + {second_number} = {result}")