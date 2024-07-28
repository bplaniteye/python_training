# Exercice module random
# Dans cet exercice, vous devez générer deux nombres aléatoires et indiquer à l'utilisateur lequel des deux nombres est le plus grand.
# Par exemple :
# Un nombre a est généré aléatoirement et prend la valeur de 15.
# Un nombre b est généré aléatoirement et prend la valeur de 26.
# Votre script doit afficher la phrase suivante :
# "Le nombre b est plus grand que le nombre a."
# Dans le cas contraire, le script devra afficher :
# "Le nombre a est plus grand que le nombre b."
# Si les nombres sont égaux, le script devra afficher :
# "Le nombre a et le nombre b sont égaux."
# Les deux nombres générés aléatoirement peuvent être des nombres entier ou des nombres décimaux, cela n'a pas d'importance. Vous pouvez également choisir n'importe quel intervalle pour générer votre nombre aléatoire.
# Attention, il est bien important que vous affichiez ces phrases précisément. Pour valider l'exercice, votre script doit afficher l'une ou l'autre des phrases ci-dessus. Si vous oubliez le point à la fin de la phrase ou la majuscule par exemple, l'exercice ne sera pas validé ! Aussi, vous ne devez pas afficher les valeurs des nombres a et b mais bien la lettre a et la lettre b (pas besoin de concaténer les variables a et b dans la phrase donc !).

import random
random_number1 = random.randint(0 , 1000)
random_number2 = random.randint(0 , 1000)
input_number = input(f"Lequel des 2 nombres {random_number1} et {random_number2} est le plus grand? : 981")
while int(input_number) != random_number1 and int(input_number) != random_number2 :
    input_number = input(f"Lequel des 2 nombres {random_number1} et {random_number2} est le plus grand? : ")
if random_number1 > random_number2 and int(input_number) == random_number1 :
    print(f"Bien joué! {random_number1} est plus grand que {random_number2}")
elif random_number2 > random_number1 and int(input_number) == random_number2 :
    print(f"Bien joué! {random_number2} est plus grand que {random_number1}")
elif random_number1 == random_number2 and input_number == random_number2 :
    print("Les 2 nombres sont égaux")
else :
    print("Vous avez échoué !")
