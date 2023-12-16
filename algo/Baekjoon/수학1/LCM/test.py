A, B = map(int, input().split())

for i in range(max(A, B), (A*B)+1):
    print(i)
    if i % A == 0 and i % B == 0:
        print(i)
        break
