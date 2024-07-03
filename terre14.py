import sys

arguments = sys.argv[1:]

if len(arguments) < 3:
    print("Please put 3 arguments or +.")
else:
    if not all(arg.isdigit() for arg in arguments):
        print("Please put 3 numbers or +.")
    else:
        nombres = [int(arg) for arg in arguments]
        triee = True
        for i in range(len(nombres)-1):
            if nombres[i] > nombres[i+1]:
                triee = False
                break
            
if triee:
    print("Sorted")
else:
    print("not Sorted")
            