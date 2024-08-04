import sys
import random

RULES = """Règles du jeu
Le but du jeu est de deviner le nombre mystère compris entre1 et 100.
Vous avez droit à 5 chances. Vous perdez une chance à chaque échec et le jeu se termine
si vous épuuisez toutes vos chances
"""
MSG_WELCOME = "BIENVENUE DANS LE JEU DU NOMBRE MYSTERE"
MSG_GOODBYE = "MERCI D'AVOIR JOUE. AU REVOIR"
MSG_LOWER_NUMBER = "Votre nombre est plus petit que le nombre mystère"
MSG_HIGHER_NUMBER = "Votre nombre est plus grand que le nombre mystère"
MSG_UNAVAILABLE_INPUT = "Viotre saisie n'est pas correcte"
MSG_USER_CHOICE = "Devinez le nombre mystère : "
MSG_WIN = "Bien joué ! Vous avez trouvé."
MSG_LOSE = "Vous avez perdu"
SEPARATOR = "-" * 50

chance = 5
print(MSG_WELCOME)
print(RULES)
print(SEPARATOR)

mystery_number = random.randrange(1 , 100)
print(mystery_number)

user_choice = input(MSG_USER_CHOICE)
while (not user_choice.isdigit() and chance > 0) or (user_choice.isdigit() and int(user_choice) != mystery_number and chance > 0):
    if not user_choice.isdigit() and chance > 0:
        print(MSG_UNAVAILABLE_INPUT)    
        print(SEPARATOR)
        # user_choice = input(MSG_USER_CHOICE)
    if user_choice.isdigit() and int(user_choice) != mystery_number and chance > 0:
        chance -= 1
        print(f"Il vous reste {chance} chance(s) pour deviner le nombre")
        print(SEPARATOR)
    # user_choice = input(MSG_USER_CHOICE)
    if int(user_choice) < mystery_number:
        print(MSG_LOWER_NUMBER)
    elif int(user_choice) > mystery_number:
        print(MSG_HIGHER_NUMBER)
    elif int(user_choice) == mystery_number:
        print(MSG_WIN)
        sys.exit()
    elif int(user_choice) != mystery_number and chance == 0:
        print(MSG_LOSE)
        sys.exit()
    user_choice = input(MSG_USER_CHOICE)