price, money, change = 0, 0, 0
c1000s, c500s, c100s = 0, 0, 0

#돈과 음료수 가격 입력
money = int(input("지불한 돈을 입력 : "))
price = int(input("구입할 음료수 가격 입력 : "))

change_org = money - price
change = money - price
org = change

c1000s = change // 1000 # 2
change %= 1000 #900
c500s = change // 500 # 1
change %= 500 # 400
c100s = change // 100 #4

print("myTest : ", org)
print("거스름돈은", money - price, "원 입니다.")
#print("거스름돈은", money - price, "원 입니다.")
print("1000원 수 =>",c1000s)
print("500원 수 =>",c500s)
print("100원 수 =>",c100s)
