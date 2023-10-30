price, money, change = 0, 0, 0
c5000s, c1000s, c500s, c100s = 0, 0, 0, 0

#돈과 음료수 가격 입력
money = int(input("지불한 돈을 입력 : "))
price = int(input("구입할 음료수 가격 입력 : "))

#잔돈 계산 
change = money - price
#5000원 계산식도 넣어서 출력해보자.
c5000s = change // 5000 #5천원 반환 값.
change %= 5000  #change  = change % 5000 -> 5000원을 나누기하고 나머지의 값을 change에 대입을 하는 것이다.
c1000s = change // 1000 # 2
change %= 1000 #900
c500s = change // 500 # 1
change %= 500 # 400
c100s = change // 100 #4
'''
print("myTest : ", org)
'''
print("거스름돈은", money - price, "원 입니다.")
print("5000원 수 =>",c5000s)
print("1000원 수 =>",c1000s)
print("500원 수 =>",c500s)
print("100원 수 =>",c100s)

