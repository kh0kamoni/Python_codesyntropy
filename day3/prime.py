start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)
