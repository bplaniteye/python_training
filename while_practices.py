
def user_continue() :    
    continuer = input("Voulez-vous continuer ? o/n : ")
    while continuer == "o":
        print("On continue !")
        input("Voulez-vous continuer ? o/n ")
        if continuer != "o" or continuer != "n" :
            print("Saisissez une valeur correcte ")
            input("Voulez-vous continuer ? o/n ")
        elif continuer == "n" :
            break