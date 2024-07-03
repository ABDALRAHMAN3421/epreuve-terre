import sys


arguments = sys.argv[1:]

if len(arguments) != 2:
    print("Erreur d'arguments.")
else:
    if not all(arg.isdigit() for arg in arguments):
        print("Que des nombres.")
    else:
        Number_1 = int(sys.argv[1])
        Number_2 = int(sys.argv[2])
        print(Number_1**Number_2)
