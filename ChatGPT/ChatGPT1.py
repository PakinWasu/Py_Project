def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

# Generating the first 1000 prime numbersa
n_primes = 1000
prime_numbers = [num for num in range(2, 10000) if is_prime(num)][:n_primes]

# Printing the first 1000 prime numbers
print(prime_numbers)
