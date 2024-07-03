import sys

def inverse_chaine(chaine):
    chaine_inverse = ""
    for caractere in chaine:
        chaine_inverse = caractere + chaine_inverse
    return chaine_inverse

def print_error(message):
    print(f"Error: {message}")

if len(sys.argv) > 1:
    chaine = sys.argv[1]
else:
    chaine = input("Please enter a sentence: ")

if chaine.isdigit():
    print_error("You cannot enter a number")
else:
    print("Inverse:", inverse_chaine(chaine))

    



