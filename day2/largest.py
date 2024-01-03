# Taking 3 number as input without using loop
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

# Checking largest number (basic)
if (num1 > num2) and (num1 > num3):
    print("Largest number: " + str(num1))
elif (num2 > num3) and (num2 > num1):
    print("Largest number: " + str(num2))
else:
    print("Largest number: " + str(num3))