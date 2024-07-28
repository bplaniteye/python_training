

note = input("Entrez votre note sur 20 : ")
while int(note) < 0 or int(note) > 20 :
    print("La valeur saisie n'est pas correcte")
    note = input("Entrez votre note sur 20 : ")

note = int(note)
commentaire = ""
# Change l'ordre des if / elif
if note < 3 :
    commentaire = "Sans commentaire..."

elif note >= 3 and note < 6:
    commentaire = "Tu n'as rien compris !"
elif note >= 7 and note < 10 :
    commentaire = "Il faut tout revoir..."
elif note >= 11 and note < 14 :
    commentaire = "Peut mieux faire."
elif note >= 15 and note < 18 :
    commentaire = "Bon travail !"
elif note >= 18 and note < 20:
    commentaire = "Excellent !!"
elif note == 20:
    commentaire = "C'est un sans faute !"


# Ne modifie pas la ligne ci-dessous
print(commentaire)