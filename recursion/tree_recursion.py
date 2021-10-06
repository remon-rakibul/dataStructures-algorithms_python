def calculation(n):
    if n > 0:
        calculation(n - 1)
        k = n ** 2
        print(k)
        calculation(n - 1)


calculation(3)