def factorial(n):
    factor = 1
    for i in range(1, n+1):
        print(factor)
        factor *= i
    return factor
liczba=5
print("silnia dla %i"%liczba)
print(factorial(liczba))
