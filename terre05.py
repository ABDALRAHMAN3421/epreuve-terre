import sys

def division_with_remainder(A, B):
    try:
        quotient = A // B
        remainder = A % B
        return quotient, remainder
    except ZeroDivisionError:
        error("Division by zero is not allowed.")
    except ValueError:
        error("Invalid input. Please enter integer values.")

def error(message):
    print(f"Error: {message}")
    sys.exit(1)

if len(sys.argv) != 3:
    error("Usage: python script.py <A> <B>")

try:
    A = int(sys.argv[1])
    B = int(sys.argv[2])
except ValueError:
    error("Invalid input. Please enter integer values.")

quotient, remainder = division_with_remainder(A, B)
print("Quotient:", quotient)
print("Remainder:", remainder)