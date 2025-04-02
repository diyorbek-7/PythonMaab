def is_prime(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True