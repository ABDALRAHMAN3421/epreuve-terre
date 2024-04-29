def est_pair(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
nombre = int(input("Voulez-vous fournir un nombre: "))
if est_pair(nombre):
    print(nombre, "est un nombre pair.")
else:
    print(nombre, "est un nombre impair.")













