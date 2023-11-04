# 1부터 n까지 정수의 합 구하기(n값은 양수만 입력받음)

print('1부터 n까지 정수의 합을 구합니다.')

while True:
    n = int(input('n값을 입력하세요.: '))
    if n > 0:  # 0보다 작을 경우 while문을 통한 반복으로 n의 값이 0보다 큰 정수만을 고집하는 루트
        break
sum = 0
i = 1

for i in range(1, n+1):  # n(n+1인 6이지만)이 5개라면 1,2,3,4,5까지 출력
    sum += i
    i += 1  # 1씩 증가

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
