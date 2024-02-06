# 세 정수를 이력받아 최댓값 구하기

print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a  # 최댓값 maximum 변수에 a값을 대입
print(maximum)  # 현재 최댓값을 확인 하기 위한 print

if b > maximum:
    maximum = b  # a와 b를 비교해서 b가 클경우 최댓값은 b가 된다.
    print(maximum)  # 현재 최댓값을 확인 하기 위한 print
if c > maximum:
    maximum = c  # c와 b를 비교해서 c가 클경우 최댓값은 c가 된다.
    print(maximum)  # 현재 최댓값을 확인 하기 위한 print
print(f"최댓값은 {maximum}입니다.")
