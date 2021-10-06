def fact_itr(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total


n = int(input("Enter Number: "))
print(fact_itr(n))
