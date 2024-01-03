# Asking for temperature input method
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

op = input("1 or 2 ?: ")


# Decision making and calculating result
if op == "1":
    c = float(input("Temperature in celsius: "))
    f = 9 / 5 * c + 32
    print(str(c) + " degree celsius is: " + str(f) + " degree fahrenheit.")
elif op == "2":
    f = float(input("Temperature in fahrenheit: "))
    c = 5 / 9 * (f - 32)
    print(str(f) + " degree fahrenheit is: " + str(c) + " degree celsius.")
else:
    print("Invalid.")