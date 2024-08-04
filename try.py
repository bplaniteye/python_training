import sys
import random

chance = 0

RULES = """Règles du jeu
Le but du jeu est de deviner le nombre mystère compris entre 1 et 100.
Vous avez droit à 5 chances. Vous perdez une chance à chaque échec et vous perdez
si vous épuisez toutes vos chances.
"""
MSG_WELCOME = "BIENVENUE DANS LE JEU DU NOMBRE MYSTERE"
MSG_GOODBYE = "MERCI D'AVOIR JOUE. AU REVOIR"
MSG_LOWER_USER_CHOICE = "Le nombre mystère est plus grand que {}"
MSG_HIGHER_USER_CHOICE = "Le nombre mystère est plus petit que {}"
MSG_UNAVAILABLE_INPUT = "Votre saisie n'est pas correcte"
MSG_NUMBER_OF_CHANCE = "Essai N° {} : Il vous reste {} essai(s) pour deviner le nombre"
MSG_USER_CHOICE = "Devinez le nombre mystère : "
MSG_WIN = "Bien joué ! Vous avez réussi au bout de {} essai(s)"
MSG_LOSE = "Vous avez perdu. Le nombre mystère était {}"
SEPARATOR = "-" * 50

print(MSG_WELCOME)
print(RULES)
print(SEPARATOR)

mystery_number = random.randrange(1 , 100)
# print(mystery_number)
user_choice = input(MSG_USER_CHOICE)    
while chance < 5:
    if user_choice.isdigit() and int(user_choice) < mystery_number:
        chance += 1
        print(MSG_LOWER_USER_CHOICE.format(user_choice))        
        print(MSG_NUMBER_OF_CHANCE.format(chance , 5 - chance))
        print(SEPARATOR)
        user_choice = input(MSG_USER_CHOICE)
    elif user_choice.isdigit() and int(user_choice) > mystery_number:
        chance += 1
        print(MSG_HIGHER_USER_CHOICE.format(user_choice))        
        print(MSG_NUMBER_OF_CHANCE.format(chance , 5 - chance))
        print(SEPARATOR)
        user_choice = input(MSG_USER_CHOICE)     
    elif not user_choice.isdigit():
        print(MSG_UNAVAILABLE_INPUT)    
        print(SEPARATOR)
        user_choice = input(MSG_USER_CHOICE)      
    elif int(user_choice) == mystery_number:
        chance += 1
        print(MSG_WIN.format(chance))       
        print(SEPARATOR)        
        sys.exit()        
if chance == 5:
    print(MSG_LOSE.format(mystery_number))
    sys.exit()