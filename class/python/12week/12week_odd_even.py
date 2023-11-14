number = input("정수를 입력하세요.->")
#끝의 한자리만 가지고 와서 구문하는 방법
last_char = number[-1]

last_num = int(last_char)

if last_num == 0 \
   or last_num == 2 \
   or last_num == 4 \
   or last_num == 6 \
   or last_num == 8 :
    print("짝수 입니다.")
else :
    print("홀수 입니다.")
