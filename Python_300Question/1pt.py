#1Q~010Q

#001 print 기초 화면에 Hello World 문자열을 출력하세요.
print("Hello World")
#002 print 기초 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)
print("Mary's cosmetics")
#003 print 기초 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
print('신씨가 소리질렀다. "도둑이야".')   
#My solution 
print("신씨가 소리질렀다. \"도둑이야\".")
#004 print 기초 화면에 "C:\Windows"를 출력하세요.
print("C:\Windows")
#005 print 탭과 줄바꿈 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
#\t는 탭을 의미하고 \n'은 줄바꿈을 의미합니다.
#My solution
# \t 은 tap이라는 일정 간격을 두는 키의 역할을 코드화 한 것이다. \n은 Enter라는 줄바꿈 키의 역할을 \t와 마찬가지로 코드화 한 것이다.

#006 print 여러 데이터 출력 print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
# 오늘은 일요일

#007 print 기초 print() 함수를 사용하여 다음과 같이 출력하세요. naver;kakao;sk;samsung
print("naver", "kakao", "sk", "samsung", sep=";")
#My solution -> 문제를 잘 봐야한다. 단순히 글자 끝마다의 세미콜론이 아닌 간격 사이에 세미콜론이 들어 갔다./sep = separator
print("naver;kakao;sk;samsung;")

#008 print 기초 print() 함수를 사용하여 다음과 같이 출력하세요. naver/kakao/sk/samsung
print("naver", "kakao", "samsung", sep="/")

#009 print 줄바꿈 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다. print("first");print("second")
print("first", end = "");print("second")

#010 연산 결과 출력 5/3의 결과를 화면에 출력하세요.
print(5/3)