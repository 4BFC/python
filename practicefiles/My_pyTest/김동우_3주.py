title = input("==> 관람하고 싶은 영화 제목을 입력하세요:")
num = int(input("==> 몇명이 관람한요??"))
price = int(input("==> 1인당 관람료는 얼마인가요?"))

print("예매하신 영화 %s을(를) %d명이 관람할 경우 관람료는 %d원입니다." %(title, num, (num*price)))
print(f"예매하신 영화 {title}을(를) {num}명이 관람할 경우 관람료는 {num*price}원입니다.")
