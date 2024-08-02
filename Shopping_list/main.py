import source

print("Bienvenue dans l'application de gestion de liste de courses.")
while True:
    choice = input(source.OPTIONS)
    if choice == "1":
        item = input("Veuillez entrer l'élément à ajouter à la liste : ")
        source.add_element(item)
    elif choice == "2":
        item = input("Veuillez entrer l'élément à supprimer de la liste : ")
        source.remove_element(item)
    elif choice == "3":
        source.display_list()
    elif choice == "4":
        source.clear_list()
    elif choice == "5":
        source.exit_program()
        break
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")