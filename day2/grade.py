# Input number
num = int(input("Mark: "))

# Converting to grade
if num > 80:
    print("Grade: A")
elif num > 70:
    print("Grade: B")
elif num > 60:
    print("Grade: C")
elif num > 50:
    print("Grade: D")
else:
    print("Grade: F")