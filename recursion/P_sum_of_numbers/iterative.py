def sum_itr(n):
    total = 1
    for i in range(1, n+1):
        total += i
    return total


num = input('Enter Number: ')
n = int(num)
print(sum_itr(n))