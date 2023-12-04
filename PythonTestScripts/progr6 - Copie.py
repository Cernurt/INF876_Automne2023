def generer_nombres_premiers(seuil):
    primes = [2]
    current_number = 3

    while current_number <= seuil:
        if all(current_number % prime != 0 for prime in primes):
            primes.append(current_number)
        current_number += 2

    return primes

seuil_generation = 20
liste_premiers = generer_nombres_premiers(seuil_generation)

print(f"Liste de nombres premiers jusqu'à {seuil_generation} : {liste_premiers}")
