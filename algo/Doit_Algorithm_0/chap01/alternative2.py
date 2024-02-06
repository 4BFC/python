# +와 -를 번갈아 출력하기2

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
range_ = n//2  # range값은 2를 담는다.
for _ in range(range_):  # //몫 5일경우 : 2의 범위를 가진다.
    print('+-', end='')
    # print(f'range_ = {range_}\n')

if n % 2:  # 5일경우 : n%2 = 1 => TRUE
    # 즉, 홀수 일 경우 출력
    print('+', end='')
    # print('\n')

print()
