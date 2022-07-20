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


# 053
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# 정답확인
movie_rank.append("슈퍼맨")
print(movie_rank)

# 053
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# 정답확인
movie_rank.append("슈퍼맨")
print(movie_rank)

#solution
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 058
# 다음 리스트의 합을 출력하라.

# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 15
# 정답확인

nums = [1, 2, 3, 4, 5]
tmp = 0
for n in nums:
    tmp += n
print(tmp)

#solution
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 061
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]
# 정답확인
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])
# 062
# 슬라이싱을 사용해서 홀수만 출력하라.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]
# 정답확인
# 063
# 슬라이싱을 사용해서 짝수만 출력하라.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]
# 정답확인
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])
# 064
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.

# nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]
# 정답확인
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])
# 065
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

# interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자 Naver
# 정답확인

# 066 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
# 정답확인
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(" ".join(interest))
# 067 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
# 정답확인
# 068 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
# 정답확인
# 069 문자열 split 메서드
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.

# string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.

# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']
# 정답확인

# 070 리스트 정렬
# 리스트에 있는 값을 오름차순으로 정렬하세요.

# data = [2, 4, 3, 1, 5, 10, 9]
# 정답확인
print("tupple문제는 전체적으로 다시 봐야합니다.")
# 071 ~ 080
# 071
# my_variable 이름의 비어있는 튜플을 만들라.

# 정답확인
# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)

# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
# 정답확인
# 073
# 숫자 1 이 저장된 튜플을 생성하라.

# 정답확인
# 074
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.

# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# 정답확인
# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?

# t = 1, 2, 3, 4
# 정답확인


# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.

# t = ('a', 'b', 'c')
# 정답확인
# 077
# 다음 튜플을 리스트로 변환하라.

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# 정답확인
# 078
# 다음 리스트를 튜플로 변경하라.

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# 정답확인
# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.

# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
# 정답확인
# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.

# (2, 4, 6, 8 ... 98)
# 정답확인