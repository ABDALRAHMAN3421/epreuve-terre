def alphabetFrom():
    x = "abcdefghijklmnopqrstuvwxyz"
    user_lettre = input('please enter a lowercaes lettre: ')
    lowerInput = user_lettre.lower()
    while True:
        if lowerInput in x:
            index = x.index(lowerInput)
            return x[index:-1]
            break
        else:
            print("Veuillez rentrer une lettre")









print(alphabetFrom())



























    