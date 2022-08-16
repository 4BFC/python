# 211~ 220
# 211
# 함수의 호출 결과를 예측하라.

# def 함수(문자열) :
#     print(문자열)

# 함수("안녕")
# 함수("Hi")
# 정답확인

"안녕"
"Hi"

# 212
# 함수의 호출 결과를 예측하라.

# def 함수(a, b) :
#     print(a + b)

# 함수(3, 4)
# 함수(7, 8)
# 정답확인

"7"
"15"

# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'
# 정답확인

"매개변수가 비어 있다."

#solution
"함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다."

# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.

# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3)
# TypeError: must be str, not int
# 정답확인

"매개변수의 자료형이 일치하지 않는다."

#solution
"정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다. 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는 에러가 발생합니다."

# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.

# 정답확인

def print_with_smile(a) :
  print(a,":D")

print_with_smile("안녕")


# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.

# 정답확인

print_with_smile("안녕하세요")

# 217
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.

# 정답확인

def print_upper_price(price) :
  print(price * 1.3)  #print(price * (100/30))

print_upper_price(100)

# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.

# 정답확인

def print_sum(a,b) : 
  return a + b

print(print_sum(1,3))

# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75
# 정답확인

def print_arithmetic_operation(a, b) :
  return a + b, a - b, a * b, a / b

print(print_arithmetic_operation(1,2))

# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

def print_max(a,b,c) : 
  if a > b : 
    return a
    if (a>b) != ture :
      return b

  elif b > c : 
    return b
    if (b>c) != ture :
      return c

  elif a > c : 
    return a
    if (a>c) != ture :
      return c

print(print_max(1,2,3))

#solution
"다시 풀기"

# 정답확인