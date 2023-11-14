number = input("정수를 입력하세요.->")
#끝의 한자리만 가지고 와서 구문하는 방법
last_char = number[-1]

if last_char in "02468" :
    print("짝")
else : 
    print("홀")
