binary = input("Enter a binary number: ")

decimal = 0
power = len(binary) - 1

for bit in binary:
    if bit == '1':
        decimal += 2 ** power
    power -= 1

print(f"Decimal: {decimal}")
