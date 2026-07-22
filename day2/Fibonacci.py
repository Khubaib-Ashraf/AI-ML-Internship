def generate_fibonacci(n):
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

terms = int(input("How many Fibonacci terms? "))
print(generate_fibonacci(terms))
