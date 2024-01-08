N = [3, 1, 2, 5, 4]
for i in range(len(N)-1, -1, -1):
    max = i
    for j in range(len(N)-1, i, -1):
        if N[max] < N[j]:
            max = j
            N[max], N[i] = N[i], N[max]

    # if N[max] != N[i-1]:
    #     print(f'{N[max]},{N[i-1]}')
    #     max = i-1
    #     N[max], N[i] = N[i], N[max]
print(N)
