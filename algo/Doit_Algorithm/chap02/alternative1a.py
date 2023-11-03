# +와 -를 번갈아 출력하기 1

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?'))

for i in range(1, n+1):
    if i % 2:  # i % 2 == 0 *0은 FALSE
        # 홀수는 +출력
        print('+', end='')
        print(f'i = {i}, i % 2  = {i % 2}\n')
    else:  # 짝수는 -출력
        print('-', end='')
        print(f'i = {i}, i % 2  = {i % 2}\n')
print()
