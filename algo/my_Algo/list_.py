# sort와 reverse를 사용하는 방법
arr_list = [2, 3, 2, 4]
list_sort = arr_list.sort()
print(list_sort)
for i in range(len(arr_list)):
    print(arr_list.sort())
print(arr_list.sort())
# arr_list.sort()를 프린트하면 안된다. sort()를 적용함으로 arr_list에 바로 적용이 되기 때문이다.
print(arr_list)
arr_list.reverse()  # reverse()또한 마찬가지이다.
print(arr_list)
print()
# 직접 입력했을 때이다.
arr_list = input().split()
arr_list.sort()
print(arr_list)
# for i in range(len(arr_list)):
# print(arr_list.sort())
