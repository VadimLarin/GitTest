def kvadratniy(N):
    x: list = []
    for i in range(-N, N+1):
        x.append(i**2)
    return x

y = int(input('Введите число --> '))
print(kvadratniy(y))

