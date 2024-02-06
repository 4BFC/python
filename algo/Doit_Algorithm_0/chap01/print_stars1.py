# *를 n개 출력하되 w개마다 줄바꿈하기 1
print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))  # 5
w = int(input("몇 개마다 줄바꿈할까요?"))  # 2

for i in range(n):
    print('*', end='')
    if i % w == w - 1:  # w-1의 값일 때만 줄바꿈 2일땐 1인경우에 줄바꿈 즉, 0,1까지
        print()

if n % w:
    print()
