import sys

def alphabetFrom():
    x = "abcdefghijklmnopqrstuvwxyz"
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <lowercase_letter>")
        sys.exit(1)

    user_lettre = sys.argv[1]
    
    if len(user_lettre) != 1:
        print("Please enter exactly one letter.")
        sys.exit(1)
    
    lowerInput = user_lettre.lower()
    
   
    if lowerInput in x:
        index = x.index(lowerInput)
        return x[index:]
    else:
        print("Please enter a valid lowercase letter.")
        sys.exit(1)

if __name__ == "__main__":
    print(alphabetFrom())



























    