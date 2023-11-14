number = input("정수를 입력하세요.->")
#끝의 한자리만 가지고 와서 구문하는 방법

last_num = int(number[-1])
even_list = [0,2,4,6,8]
odd_list = [1,3,5,7,9]

if last_num in even_list :
    print("짝")
if last_num in odd_list :
    print("홀")
