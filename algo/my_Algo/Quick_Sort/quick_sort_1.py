def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# 정렬할 리스트를 생성
my_list = [64, 34, 25, 12, 22, 11, 90]

# 퀵 정렬을 사용하여 리스트를 정렬
sorted_list = quick_sort(my_list)

# 정렬된 리스트 출력
print("퀵 정렬 결과:", sorted_list)
