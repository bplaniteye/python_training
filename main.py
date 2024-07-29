# word = "PYTHON"
# reversed_word = reversed(word)
# for i in reversed_word :
#     print(i)

continuer = input("Voulez-vous continuer ? o/n : ")
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")   
    if continuer != "o" and continuer != "n" :
        print("Saisissez une valeur correcte ")
        continuer = input("Voulez-vous continuer ? o/n ")
    elif continuer == "n" :
        break
    


# if continuer != "o" and continuer != "n" :
#     print("Saisissez une valeur correcte ")
#     continuer = input("Voulez-vous continuer ? o/n ")
# elif continuer == "n" :
# break