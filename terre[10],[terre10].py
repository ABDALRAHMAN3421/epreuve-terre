def est_premier(nombre):
    return nombre > 1 and all(nombre % i != 0 for i in range(2, int(nombre**0.5) + 1))

nombre = int(input("Entrez un nombre entier positif: "))
if est_premier(nombre):
    print(nombre, "est un nombre premier.")
else:
    print(nombre, "n'est pas un nombre premier.")