# Input year
year = int(input("Year: "))

# Checking if year is leapyear
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year.")
else:
    print("Not leap year.")