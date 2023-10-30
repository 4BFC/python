rainbow = ["빨","주","노","초","파,","남","보"]
print("원본 ==>", rainbow, "\n")

del rainbow[0]
print("del을 이용한 삭제 ==>", rainbow, "\n")

rainbow.remove("주")
print("remvoe을 이용한 삭제 ==>", rainbow, "\n")

rainbow.pop()
print("pop을 이용한 삭제 ==>", rainbow, "\n")

rainbow.clear()
print("clear를 이용한 삭제 ==>", rainbow, "\n")
