def moyenne_mobile(liste, fenetre):
    moyennes_mobiles = []
    for i in range(len(liste) - fenetre + 1):
        moyenne = sum(liste[i:i+fenetre]) / fenetre
        moyennes_mobiles.append(moyenne)
    return moyennes_mobiles

donnees = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
taille_fenetre = 3
resultats_mobiles = moyenne_mobile(donnees, taille_fenetre)

print(f"Moyenne mobile avec une fenêtre de {taille_fenetre} : {resultats_mobiles}")
