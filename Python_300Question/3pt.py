#021Q~030Q
# 021 문자열 인덱싱 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.

# >> letters = 'python'
# 실행 예
# p t

letters = 'python'
print(letters[0],letters[2])

# 022 문자열 슬라이싱 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.

# >> license_plate = "24가 2210"
# 실행 예: 2210

license_plate = "24가 2210"
print(license_plate[4:])

#solution
# 문자열에서 여러 글자를 가져오는 것을 슬라이싱이라고 부릅니다. 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미합니다. 슬라이싱에서 시작 인덱스를 생락혀면 0으로 간주하고 끝 인덱스를 생략하면 문자열의 끝을 의미합니다.
license_plate = "24가 2210"
print(license_plate[-4:])

# 023 문자열 인덱싱 아래의 문자열에서 '홀' 만 출력하세요.

# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

#solution 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.
print("23번은 다시 풀어보세요.")
string = "홀짝홀짝홀짝"
print(string[::2])

# 024 문자열 슬라이싱 문자열을 거꾸로 뒤집어 출력하세요.

# >> string = "PYTHON"
# 실행 예:
# NOHTYP
print("24번은 다시 풀어보세요.")
string = 'PYTHON'
#My solution
#print(string.revrse()) #list에서만 가능

#solution
print(string[::-1]) #for문을 사용해서 string[-1]하는 것보다 효율적
# i = 0
# for a in string:
#     i += -1
#     print(string[-i])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.

# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222
print("25번은 다시 풀어보세요.")
phone_number = "010-1111-2222"

#solution
phone_number = phone_number.replace("-", " ")
print(phone_number)


# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.

# 실행 예
# 01011112222
phone_number = "010-1111-2222"
phone_number = phone_number.replace("-","")
print(phone_number)

# 027 문자열 다루기 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
# 실행 예:
# kr
url = "http://sharebook.kr"
print(url[-2:])

# 028 문자열은 immutable 아래 코드의 실행 결과를 예상해보세요.

# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)
#My solution
print("Python")
#solution
print("error가 발생한다. 그 이유는 문자열이 할당 메서드를 지원하지 않는다.=>immutable 따라서 문자열은 변경할 수 없다.")
# 029 replace 메서드 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A
#My solution
string = 'abcdfe2a354a32a'
print(string.replace('a','A'))
#solution
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 030 replace 메서드 아래 코드의 실행 결과를 예상해보세요.

# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)

#My solution
print("aBcd")

#solution
print("문자 'abcd' 그대로 출력된다. 문자열은 변경할 수 없다.")