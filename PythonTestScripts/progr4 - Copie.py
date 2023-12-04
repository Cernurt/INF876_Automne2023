def est_nombre_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True

number_to_check = 13

if est_nombre_premier(number_to_check):
    print(f"{number_to_check} est un nombre premier.")
else:
    print(f"{number_to_check} n'est pas un nombre premier.")
