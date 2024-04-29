def reverseString(phrase):
    return phrase[::-1]

user_input = input("Please enter a phrase: ")

if user_input.isdigit():
    print("Please enter a phrase containing alphabetic characters.")
else:
    print(reverseString(user_input))