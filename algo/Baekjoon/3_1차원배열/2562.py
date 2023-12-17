for i in range(9):
    x = list(map(int, input()))
    max_i = x[0]
    if max_i < x[i]:
        max_i = x[i]
print(max_i)
