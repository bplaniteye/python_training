import sys

# Declaration of the shopping list
SHOPPING_LIST = []
# List of user choices
OPTIONS = """1 = Ajouter un élément dans la liste
2 = Supprimer un élément de la liste
3 = Afficher la liste de courses
4 = Vider la liste de courses
5 = Quitter le programme
Veuillez choisir une option : """
separator = "--------------------------------------------------------------------------"

# Add element in the list
def add_element(element):
    SHOPPING_LIST.append(element)
    print(f"L'élément {element} a bien été ajouté à la liste.")
    print(separator)
    return SHOPPING_LIST

# Remove element from the list
def remove_element(element):
    if element in SHOPPING_LIST:
        SHOPPING_LIST.remove(element)
        print(f"L'élément {element} a bien été supprimé de la liste.")
        print(separator)
    else:
        print(f"L'élément {element} n'est pas présent dans la liste.")
        print(separator)
    return SHOPPING_LIST

# Display the list
def display_list():
    if SHOPPING_LIST:
        print("Voici la liste de courses : ")
        for i , item in enumerate(SHOPPING_LIST , 1):
            print(f"{i} - {item}")
            print(separator)
    else:
        print("La liste de courses est vide.")
        print(separator)
    return SHOPPING_LIST

# Clear the list
def clear_list():
    SHOPPING_LIST.clear()
    print("La liste de courses a bien été vidée.")
    print(separator)
    return SHOPPING_LIST

# Exit the program
def exit_program():
    print("Merci d'avoir utilisé notre application.")
    return sys.exit()