A, B = map(int, input().split())

for i in range(min(A, B), 0, -1):
    print(i)
    if A % i == 0 and B % i == 0:
        print(i)
        break
