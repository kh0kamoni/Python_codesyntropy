# Define product function
def product(*numbers):
    result = 1

    # Iterate through the tuple of numbers and multiply
    for number in numbers:
        result *= number

    return result

# Print product of the numbers
print(product(1, 3, 4))