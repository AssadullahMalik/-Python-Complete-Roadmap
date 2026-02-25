def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

    
    def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)


print_reverse(5)
print(factorial(5))
print(fibonacci(6))  

