# Vérifier qu'un élément est dans une liste
# Dans cet exercice, vous devez :
# Ajouter le nombre 6 dans la liste.
# Faire une vérification par la suite pour vous assurer que l'élément a bien été ajouté.
# La liste de départ est la suivante :
# liste = [1, 2, 3, 4, 5]
# Vous devez ajouter le nombre 6 dans la liste.
# Vérifiez ensuite si le nombre 6 est présent dans la liste, si c'est le cas, affichez la chaîne de caractères 'Le nombre 6 a bien été ajouté à la liste.'

liste = [1, 2, 3, 4, 5]
liste.append(6)
print(liste)
if 6 in liste :
    print("Le nombre 6 a bien été ajouté à la liste")
else :
    print("Le nombre 6 n'a pas été ajouté à la liste")