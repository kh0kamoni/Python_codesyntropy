# Input a number
num = int(input("Number: "))

# Calculation of factorial of the given number
if num == 0 or num == 1:
    result = 1;
    print(result)
else:
    result = 1
    while num != 0:
        result = result * num
        num -= 1
    print(result)