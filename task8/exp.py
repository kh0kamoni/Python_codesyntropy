def calculate_exponential(base, *exponents):
    return [base ** exp for exp in exponents]

print(calculate_exponential(4, 6))