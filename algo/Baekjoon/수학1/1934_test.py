T = input()

for i in range(int(T)):
    A, B = map(int, input().split())
    for ii in range(max(A, B), (A*B)+1):
        if ii % A == 0 and ii % B == 0:
            print(ii)
            break
