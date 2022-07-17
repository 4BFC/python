print( "023 문자열 인덱싱 아래의 문자열에서 '홀' 만 출력하세요.")

# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

#solution 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.

print("024 문자열 슬라이싱 문자열을 거꾸로 뒤집어 출력하세요.")

# >> string = "PYTHON"
# 실행 예:
# NOHTYP

print( "025 문자열 치환 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.")

# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222

print( "028 문자열은 immutable 아래 코드의 실행 결과를 예상해보세요.")

# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)

print("035 문자열 출력 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 '%' formatting을 사용해서 다음과 같이 출력해보세요.")

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13

# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

print("036 문자열 출력 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.")

print("037 문자열 출력 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.")

print("038 컴마 제거하기 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.")

# 상장주식수 = "5,969,782,550"
# My solution

# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
# My solution
hello = 'hello'
hello[0].upper()
print(hello)

#solution
hello = hello.capitalize()
print(hello)

# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"
# 정답확인

file_name = "보고서.xlsx"
print(file_name.endswith(".xlsx"))

# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.

# file_name = "보고서.xlsx"
# 정답확인

file_name = "보고서.xlsx"
file_name = file_name.endswith(("xlsx", "xls"))
print(file_name)

# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# a = "hello world"
# 정답확인

a = "hello world"
a = a.split(' ')
print(a)

# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.

# data = "039490     "

data = "039490     "
data = data.rsplit()
print(data)
