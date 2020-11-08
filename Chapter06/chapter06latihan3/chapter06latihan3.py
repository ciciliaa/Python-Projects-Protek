def faktorial(n):
    if n == 0:
        return 1
    else:
        return (n * faktorial(n - 1))

print(faktorial(5))
print(faktorial(3))
print(faktorial(10))
print(faktorial(7))
