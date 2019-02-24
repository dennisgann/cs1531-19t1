# For a given number, find the sum of n + n^2 + n^3 + ... + n^n

def sumN(n):
    sum = 0
    for i in range(1, n + 1):
        sum += n**i
    return sum

# example - 2
print(sumN(2))
