def factorials(*numbers):
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    return [factorial(num) for num in numbers]

# Print result
print(factorials(4, 5, 3))