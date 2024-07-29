
# Récupérer des éléments dans une liste imbriquée
# Dans cet exercice, vous allez devoir récupérer des informations à l'intérieur de listes imbriquées.

# Le script dispose de deux listes contenant plusieurs listes imbriquées, une liste langages et une liste nombres.

# Vous devez récupérer dans les variables python, deux et sept, respectivement la chaîne de caractères 'Python' contenue dans la liste langages et les nombres 2 et 7, contenus dans la liste nombres.

# ⚠️Vous n'avez pas besoin d'afficher les variables avec print, il suffit de récupérer les bonnes valeurs dans les variables à partir des listes et avec les indices des éléments.

langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

python = langages[0][0]
deux = nombres[1][1][0]
sept = nombres[4][0][0]
print(f"{python} - {deux} - {sept}")