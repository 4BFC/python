#변수 영역
title = ["작은 것들을 위한 시", "하기나 해"]
singer = ["BTS", "GRAY"]

#리스트 영역
print("곡명과 가수를 지정해봅시다.")
#추가되는 영역
title.append(input("곡명 : "))
singer.append(input("가수 : "))

print("\n곡 목록:", title)
print("가수 목:", singer)
print()
print(f"곡명: {title[0]}, 가수: {singer[0]}")


