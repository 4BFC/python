N = input()
n = list(set(N))
print(f"n(x) = {n}")
cnt_list = []
for x in n:
    # n의 요소들을 x값에 담는다. 따라서 cnt_list는 n의 요소의 set 배치 순서대로 나열되어 있다.
    cnt = N.count(x)  # x는 곧 n의 요소이다.
    cnt_list.append(cnt)
print(f"cnt_list(N.count(x)) = {cnt_list}")

if cnt_list.count(max(cnt_list)) > 1:
    # 최대 max값을 count 했을 때 2개 이상 이면 ?이다.
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(f"max_index = {max_index}")
    print(n[max_index])
# print(cnt_list)

# print(cnt_list.count(max(cnt_list)))  # 가장 큰 값을 카운트

# N = [1, 2, 2, 3, 4]
# print(N.count(2))
# print(set(N))
