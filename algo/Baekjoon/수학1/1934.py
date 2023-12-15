T = input()  # 3
for x in range(int(T)):
    A, B = map(int, input().split())
    if (A*B) % 2 != 0:
        print(A*B)
    else:
        print(int((A*B) / 2))
