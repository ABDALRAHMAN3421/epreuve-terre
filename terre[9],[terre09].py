import math

entier = int(input("Entrez un entier positif : "))
while entier < 0:
    print("L'entier doit être positif.")
    entier = int(input("Entrez un entier positif : "))

print(f"La racine carrée de {entier} est : {math.sqrt(entier)}")