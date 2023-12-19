import random

n = int(input())

# 코인 정답
x_range = []  # 데이터
for _ in range(n):
    if n >= 0:
        x = int((random.random())*10)
        x_range.append(x)
        print(x_range)
    else:
        print("Error")

# find_x_range = []
# check = True
# while (check):
#     for _ in range(100):
#         find_x = int((random.random())*10)
#         find_x_range.append(find_x)
#         # print(find_x_range)
#         print(x_range)
#         if x_range == find_x_range:
#             check = False
#             print("Find it!")
#         else:
#             print("Fail")
#             break
