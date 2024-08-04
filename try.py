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
MSG_LOWER_NUMBER = "Votre nombre est plus petit que le nombre mystère"
MSG_HIGHER_NUMBER = "Votre nombre est plus grand que le nombre mystère"
MSG_UNAVAILABLE_INPUT = "Votre saisie n'est pas correcte"
MSG_USER_CHOICE = "Devinez le nombre mystère : "
MSG_WIN = "Bien joué ! Vous avez trouvé."
MSG_LOSE = "Vous avez perdu"
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
        print(MSG_LOWER_NUMBER)        
        print(f"Essai N° {chance} : Il vous reste {5 - chance} essai(s) pour deviner le nombre")
        print(SEPARATOR)
        user_choice = input(MSG_USER_CHOICE)
    elif user_choice.isdigit() and int(user_choice) > mystery_number:
        chance += 1
        print(MSG_HIGHER_NUMBER)        
        print(f"Essai N° {chance} : Il vous reste {5 - chance} essai(s) pour deviner le nombre")
        print(SEPARATOR)
        user_choice = input(MSG_USER_CHOICE)     
    elif not user_choice.isdigit():
        print(MSG_UNAVAILABLE_INPUT)    
        print(SEPARATOR)
        user_choice = input(MSG_USER_CHOICE)      
    elif int(user_choice) == mystery_number:
        chance += 1
        print(MSG_WIN)             
        print(f"Vous avez réussi au bout de {chance} essai(s)")
        print(SEPARATOR)        
        sys.exit()        
if chance == 5:
    print(MSG_LOSE)
    sys.exit()