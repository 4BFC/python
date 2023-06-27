# 203
# def print_coin():
#   print("비트코인")
# 201번에서 정의한 print_coin 함수를 100번호출하라.
# 정답확인

# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
# 정답확인

# 221
# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.

# print_reverse("python")
# nohtyp
# 정답확인

# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# for문 사용하지 말 것.
# print_score ([1, 2, 3])
# 2.0
# 정답확인

# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.

# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12
# 정답확인


# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]
# 정답확인

# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.

# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸
# 정답확인

# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.

# calc_monthly_salary(12000000)
# 1000000
# 정답확인

# 230
# 아래 코드의 실행 결과를 예측하라.

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200)
# 정답확인

# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.

# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]
# 정답확인

# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.

# convert_int("1,234,567")
# 1234567
# 정답확인

# 241 현재시간
# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
# 정답확인

# 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
# 정답확인

# 244 strftime
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# 18:35:01 
# 정답확인

# 245 strptime
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요

# 246 sleep 함수
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.

# 정답확인

# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
# 정답확인

# 248 os 모듈
# os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.

# 정답확인

# 249 rename 함수
# 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.

# 정답확인

# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.

# >>> areum = Human()
# 응애응애
# 정답확인

#255~259 세트 문제
# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
# 정답확인

# 257 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자
# 정답확인

# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")
# 정답확인

# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라
# 정답확인

# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

# class OMG : 
#     def print() :
#         print("Oh my god")

# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()

# TypeError: print() takes 0 positional arguments but 1 was given
# 정답확인