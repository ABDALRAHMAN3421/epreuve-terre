import sys

args = sys.argv[1:]

number = list(map(int, args))

if len (number) != 3:
    print("please enter a full number 3 times. ")
    sys.exit(1)


sorted_number = sorted(number)

a, b, c = sorted_number

print("La valeur du milieu est :", b)