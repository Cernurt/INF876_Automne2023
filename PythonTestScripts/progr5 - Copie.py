def somme_carres_nombres_pairs(seuil):
    return sum(x**2 for x in range(100, seuil + 1, 2))

seuil_calcul = 10000
resultat = somme_carres_nombres_pairs(seuil_calcul)

print(f"La somme des carrés des nombres pairs jusqu'à {seuil_calcul} est : {resultat}")
