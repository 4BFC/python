n = int(input())  # 행의 수를 나타내는 변수, 원하는 크기로 변경 가능

for i in range(n):
    for j in range(n - i - 1):  # start,end,step
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
