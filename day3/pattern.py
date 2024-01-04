rows = int(input("Enter the number of rows: "))

# Right-aligned Triangle
print("\nRight-aligned Triangle:")
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)

# Diamond Pattern
print("\nDiamond Pattern:")
for i in range(1, rows, 2):
    print(" " * ((rows - i) // 2) + "*" * i)

for i in range(rows, 0, -2):
    print(" " * ((rows - i) // 2) + "*" * i)
