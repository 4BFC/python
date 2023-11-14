number = int(input("정수를 입력하세요.->"))
n = int(input("확인하고 싶은 배수를 입력하세요."))
result = number % n

if result :
    print(f"{n}의 배수인 홀수 => {result} ")
else :
    print(f"{n}의 배수인 짝수 => {result} ")
