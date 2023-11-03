# a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.:'))  # 1
b = int(input('정수 b를 입력하세요.:'))  # 5

if a > b:
    a, b = b, a

sum = 0

for i in range(a, b+1):  # 여기서 b+!을 하는 이유는 if문의 조건때문이다.
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i}=', end='')
    sum += i  # sum은 현재 if문 안에 있다.
print(sum)
