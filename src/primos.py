n = int(input())
for i in range(1, n+1):
    divisores = 0
    for divisor in range(1, i+1):
        if i % divisor == 0:
            divisores += 1
    if divisores == 2:
        print(i, end=' ')
