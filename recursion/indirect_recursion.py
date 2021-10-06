def calculate_a(n):
    if n > 0:
        calculate_b(n - 1)


def calculate_b(n):
    if n > 0:
        calculate_a(n - 1)
