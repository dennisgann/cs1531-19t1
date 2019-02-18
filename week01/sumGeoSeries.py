# hello

def sumN(n):
    sum = 0
    for i in range(1, n + 1):
        sum += n**i
    return sum

print(sumN(2))
