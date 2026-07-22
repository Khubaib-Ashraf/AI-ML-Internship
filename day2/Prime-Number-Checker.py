def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1): # Optimized: check up to square root
        if n % i == 0: return False
    return True

num = int(input("Enter a number: "))
print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}.")
