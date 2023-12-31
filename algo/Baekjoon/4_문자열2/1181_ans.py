# n = ['but', 'i', 'wont', 'hesitate', 'no', 'more',
#      'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
# n = []

# for i in range(n):
#     n.append(input())

# n.sort()  # 괄호 안에 아무 값도 넣지 않으면 알파벳 순서대로 정렬을 해 준다.
# print(n)
# n.sort(key=len)  # 문자열 길이 순으로 정렬.
# print(n)
# # for i in n:
# #     print(i)

n = ['but', 'i', 'wont', 'hesitate', 'no', 'more',
     'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
set_lst = set(n)  # set으로 변환해서 중복값을 제거
print(type(set_lst))
n = list(set_lst)  # 다시 list로 변환
# n.sort()
n.sort(key=len)

for i in n:
    print(i)
