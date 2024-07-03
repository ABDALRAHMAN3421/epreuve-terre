import sys

def is_even(number):
    return number % 2 == 0

def print_error(message):
    print(f"Error: {message}")
    sys.exit(1)

if len(sys.argv) != 2:
    print_error("Usage: python script.py <number>")

try:
    number = int(sys.argv[1])
except ValueError:
    print_error("Please provide a valid integer.")

if is_even(number):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")







