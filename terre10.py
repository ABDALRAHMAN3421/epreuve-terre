import sys

def est_premier(nombre):
    return nombre > 1 and all(nombre % i != 0 
        for i in range(2, int(nombre**0.5) + 1))

if len(sys.argv) != 2:
    print("Usage: python script.py <nombre>")
    sys.exit(1)

try:
    nombre = int(sys.argv[1])
except ValueError:
    print("Veuillez entrer un nombre entier positif.")
    sys.exit(1)

if est_premier(nombre):
    print(f"oui, {nombre} est un nombre premier.")
else:
    print(f"non, {nombre} n'est pas un nombre premier.")