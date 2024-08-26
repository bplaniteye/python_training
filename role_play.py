from random import randrange
from sys import exit

# Rules of the role play
RULES = """Règles du jeu
Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.
Le jeu comporte deux joueurs : vous et un ennemi.
Vous commencez tous les deux avec 50 points de vie.
Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.
L'ennemi ne dispose d'aucune potion.
Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
Lorsque vous utilisez une potion, vous passez le prochain tour.
Déroulé de la partie
Lorsque vous lancez le script, vous devez demander à l'utilisateur s'il souhaite attaquer ou utiliser une potion :
"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
Cette phrase sera demandée à l'utilisateur au début de chaque tour.
?  Si l'utilisateur choisi la première option (1), vous infligez des points de dégât à l'ennemi.
Ces points seront compris entre 5 et 10 et déterminés aléatoirement par le programme.
?  Si l'utilisateur choisi la deuxième option (2), vous prenez une potion.
Les points de vie que la potion vous donne doivent être compris entre 15 et 50 et générés aléatoirement par le programme Python.
Vous devez vérifier que l'utilisateur dispose de suffisamment de potion et décrémenter le nombre de potions qu'il a dans son inventaire lorsqu'il en boit une. Si l'utilisateur n'a plus de potions, vous devez lui indiquer et lui proposer de nouveau de faire un choix (attaquer ou prendre une potion).
Quand le joueur prend une potion, il passe le prochain tour.
Une fois l'action du joueur exécutée, et si l'ennemi est encore vivant, il vous attaque. Si l'ennemi est mort, vous pouvez terminer le jeu et indiqué à l'utilisateur qu'il a gagné ?
L'attaque de l'ennemi inflige des dégâts au joueur compris entre 5 et 15, là encore déterminés aléatoirement par le script.
Si vous n'avez plus de points de vie, le jeu se termine et vous avez perdu la partie.
À la fin du tour, vous devez afficher le nombre de points de vie restants du joueur et de l'ennemi.
Toutes ces opérations se répètent tant que le joueur et l'ennemi sont en vie.
À chaque tour, vous attaquez en premier. Il ne peut donc pas y avoir de match nul. Si lorsque vous attaquez, votre attaque fait descendre les points de vie de l'ennemi en dessous (ou égal à) 0, vous gagnez la partie sans que l'ennemi n'ait le temps de vous attaquer en retour.
"""
SEPARATOR = "-" * 50
# Messages
MSG_CHOICE = "Voulez-vous attaquer (1) ou utiliser une potion (2) ? : "
MSG_PLAYER_NAME = "Quel est votre nom? : "
MSG_PLAYER_ATTACK = "⚡ Vous avez infilgé une attaque de {} points de vie à l'ennemi "
MSG_ENEMY_ATTACK = "🔥 L'ennemi vous a infilgé une attaque de {} points de vie"
MSG_POTION_USE = """Vous avez utilisé une potion de vie 🧪. Il vous en reste {}.
Vous avez gagné {} points de vie ❤"""
MSG_EMPTY_POTION = "Vous n'avez plus de potion ⚠"
MSG_PLAYER_WIN = "Bien joué {} ! Vous avez gagné."
MSG_PLAYER_LOSE = "{}, vous avez perdu!"
MSG_UNAVAILABLE_INPUT = "Votre saisie n'est pas correcte"
STATS = "{} : {} ❤ {} 🧪 | ENNEMI : {} ❤"
# Player
player_life = 50
player_attack = randrange(5 , 10)
player_life_potion = randrange(15 , 50)
life_potion_number = 3
# Enemy
enemy_life = 50
enemy_attack = randrange(10 , 20)

player_name = input(MSG_PLAYER_NAME)
print(STATS.format(player_name , player_life , life_potion_number , enemy_life))
player_choice = input(MSG_CHOICE)
while player_life > 0 or enemy_life > 0:
    if player_choice == "1"and player_life > 0 and enemy_life > 0:
        enemy_life -= player_attack
        player_life -= enemy_attack
        print(MSG_PLAYER_ATTACK.format(player_attack))
        print(MSG_ENEMY_ATTACK.format(enemy_attack))
        print(STATS.format(player_name , player_life , life_potion_number , enemy_life))
        print(SEPARATOR)
    elif player_choice == "2" and player_life > 0 and enemy_life > 0:
        if life_potion_number > 0:
            player_life += player_life_potion
            life_potion_number -= 1
            print(MSG_POTION_USE.format(life_potion_number , player_life_potion))       
            player_life -= enemy_attack
            print(MSG_ENEMY_ATTACK.format(enemy_attack))
            player_life -= enemy_attack        
            print(MSG_ENEMY_ATTACK.format(enemy_attack))
        elif life_potion_number == 0:
            print(MSG_EMPTY_POTION)            
        print(STATS.format(player_name , player_life , life_potion_number , enemy_life))
        print(SEPARATOR)
    elif player_life <= 0 and enemy_life > 0:
        print(STATS.format(player_name , player_life , life_potion_number , enemy_life))
        print(MSG_PLAYER_LOSE.format(player_name))
        exit()
    elif enemy_life <= 0 and player_life > 0:
        print(STATS.format(player_name , player_life , life_potion_number , enemy_life))
        print(MSG_PLAYER_WIN.format(player_name))
        exit()        
    elif not player_choice.isdigit() or player_choice not in ["1" , "2"]:
        print(MSG_UNAVAILABLE_INPUT)    
    player_choice = input(MSG_CHOICE)