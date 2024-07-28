# code a method or function that asks a user for their first name, last name, and age and returns a string that looks like this:
# "Hello, my name is [first name] [last name] and I am [age] years old."
# The first name should be capitalized, the last name should be uppercased, and the age should be an integer.
# The function should also count the number of times the letter "a" appears in the string and print it to the console.
# The function should return the string.
# The function should be called presentation.
def presentation():
    first_name = input("Enter your first name: ")
    first_name = first_name.capitalize()
    last_name = input("Enter your last name: ")
    last_name = last_name.upper()
    full_name = first_name + " " + last_name
    age = input("Enter your age: ")
    presentation = "Hello, my name is " + full_name + " and I am " + age + " years old."
    print(presentation)   
    return presentation