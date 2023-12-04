import random

def jouer_pierre_papier_ciseaux(choix_utilisateur):
    choix_ordinateur = random.choice(["pierre", "papier", "ciseaux"])

    print(f"Vous avez choisi : {choix_utilisateur}")
    print(f"L'ordinateur a choisi : {choix_ordinateur}")

    if choix_utilisateur == choix_ordinateur:
        print("C'est une égalité !")
    elif (choix_utilisateur == "pierre" and choix_ordinateur == "ciseaux") or \
         (choix_utilisateur == "papier" and choix_ordinateur == "pierre") or \
         (choix_utilisateur == "ciseaux" and choix_ordinateur == "papier"):
        print("Vous avez gagné !")
    else:
        print("L'ordinateur a gagné !")

# Choix aléatoire de l'utilisateur
choix_utilisateur = random.choice(["pierre", "papier", "ciseaux"])

# Appeler la fonction avec le choix aléatoire de l'utilisateur
jouer_pierre_papier_ciseaux(choix_utilisateur)
