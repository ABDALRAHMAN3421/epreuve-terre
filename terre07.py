import sys

argument = sys.argv[1:]

if len(argument) > 1:
    print("one argument only in this script.")

string = argument[0]



caractere = 0

for lettre in string:
    if lettre.isalpha():
        caractere = caractere+1
    else:
        print("Erreur")
        
print(caractere)