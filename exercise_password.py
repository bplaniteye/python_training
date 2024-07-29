# Dans cet exercice, vous devez :
# Afficher la phrase mdp_trop_court en majuscule si la longueur du mot de passe entré est égale à 0.
# Afficher la phrase mdp_trop_court avec une majuscule sur la première lettre si la longueur du mot de passe entré est plus petite que 8.
# Afficher la phrase "Votre mot de passe ne contient que des nombres." si le mot de passe entré ne contient que des nombres.
# Afficher la phrase "Inscription terminée." si le mot de passe est valide.
# Script de départ :
# mdp = input("Entrez un mot de passe (min 8 caractères) : ")
# mdp_trop_court = "votre mot de passe est trop court."
# Questions pour cet exercice
# Comment utiliser les structures conditionnelles et des méthodes de chaînes de caractères pour vérifier la validité du mot de passe ?

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

while len(mdp) < 8 or (len(mdp) >= 8 and mdp.isdigit() ) :
    if len(mdp) == 0 :
        print(mdp_trop_court.upper())
    elif len(mdp) < 8 :
        print(mdp_trop_court.capitalize())
    elif len(mdp) >= 8 and mdp.isdigit() :
        print("Votre mot de passe ne contient que des chiffres")
    mdp = input("Entrez un mot de passe (min 8 caractères) : ")
if len(mdp) >= 8 and not mdp.isdigit() :
    print("Inscription terminée")