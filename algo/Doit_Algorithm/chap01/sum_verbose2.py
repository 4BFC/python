# a 부터 b까지 정수의 합 구하기 2
print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

# a가 클경우 b를 큰수로 바꿔 줘야하는 스와이프의 역할이다.
if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):  # 2,5
    print(f'{i}+', end='')
    sum += i  # 2,3,4,5

print(f'{b} = ', end='')
sum += b

print(sum)
