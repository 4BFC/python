# split을 다시 공부해보자.
import sys
N = int(sys.stdin.readline())
temp = []
for _ in range(N):
    VPS = sys.stdin.readline()
    VPS_list = list(VPS)
    for _ in range(len(VPS_list)):
        if VPS_list[_] == '(':
            temp.append(VPS_list[0])
            VPS_list[_].pop()
        elif temp[0] == '(' and VPS_list[_] == ')':
            temp.append(VPS_list[_])
    print(VPS_list)
    even = VPS_list.count('(')
    odd = VPS_list.count(')')
    if even == odd:
        print("YES")
    else:
        print("NO")
# print(VPS_list.count('('))
# print(VPS_list.count(')'))

# for _ in range(len(VPS_list)):
#     if VPS_list[0] == ')':
#         print("False")
#         break
#     if VPS_list[0] == '(':
#         print(VPS_list.count('('))
#         print(VPS_list.count(')'))

# print(VPS_list[_])
