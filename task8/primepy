def find_prime_numbers(*args):
    def prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in args if prime(num)]

print(find_prime_numbers(1, 2, 3, 4, 5, 6, 7, 8))