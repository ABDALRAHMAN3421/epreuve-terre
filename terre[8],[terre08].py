def puissance(base, exsposant):
    return base ** exsposant


base = int(input("Enter the base: "))
exposant = int(input("Enter the exponent: "))
power_result = puissance(base, exposant)
print("Result:", power_result)