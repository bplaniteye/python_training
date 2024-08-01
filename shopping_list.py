# from pprint import pprint

shopping_list = []
element = input("Ajouter un élément à la liste de course : ")
shopping_list.append(element)

action = input("""Appuyez sur
    1 pour ajouter un élément à la liste de courses
    2 pour retirer un élément de la liste de courses
    3 pour afficher les éléments de la liste de courses
    4 pour vider la liste de courses
    5 pour quitter le programmer : """)

if action == "1" :
    element = input("Ajouter un élément à la liste de course : ")
    shopping_list.append(element)
    action = input("""Appuyez sur
    1 pour ajouter un élément à la liste de courses
    2 pour retirer un élément de la liste de courses
    3 pour afficher les éléments de la liste de courses
    4 pour vider la liste de courses
    5 pour quitter le programmer : """)
    
elif action == "2" :
    element_to_cancel = input("Quel élément voulez-vous supprimer de la liste de courses? : ")
    shopping_list.remove(element_to_cancel)
    action = input("""Appuyez sur
    1 pour ajouter un élément à la liste de courses
    2 pour retirer un élément de la liste de courses
    3 pour afficher les éléments de la liste de courses
    4 pour vider la liste de courses
    5 pour quitter le programmer : """)
        
elif action == "3" :
    shopping_list_sorted = sorted(shopping_list)
    shopping_list_elements = "\n".join(shopping_list_sorted)
    print(shopping_list_elements)
    action = input("""Appuyez sur
    1 pour ajouter un élément à la liste de courses
    2 pour retirer un élément de la liste de courses
    3 pour afficher les éléments de la liste de courses
    4 pour vider la liste de courses
    5 pour quitter le programmer : """)
    
elif action == "4" :
    shopping_list.clear()
    print("Votre liste de courses est vide")
    action = input("""Appuyez sur
    1 pour ajouter un élément à la liste de courses
    2 pour retirer un élément de la liste de courses
    3 pour afficher les éléments de la liste de courses
    4 pour vider la liste de courses
    5 pour quitter le programmer : """)
    
elif action == "5" :
    print("Votre liste de courses a bien été enregistrée. Au revoir !")