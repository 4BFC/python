remain_list = []
for _ in range(10):
    N = int(input())
    if N % 42 not in remain_list:
        remain_list.append(N % 42)
print(len(remain_list))
