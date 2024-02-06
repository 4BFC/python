import heapq
# heapify


def heap_sort(arr):
    heap = []
    for element in arr:
        heapq.heappush(heap, element)
        print(heap)
    # print(heap)
    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))
        print(sorted_arr)
    return sorted_arr


arr = [5, 3, 8, 4, 2, 7, 10, 1]
sorted_arr = heap_sort(arr)
print(sorted_arr)
