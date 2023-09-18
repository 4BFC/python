def insertion_sort(arr):
    n = len(arr) # 배열의 길이를 저장
    for i in range(1, n): # 배열 길이 5를 기준으로 1에서 5까지의 범위
        #*는 해당 배열의 값
        key = arr[i] # 1,2,9,3,4를 기준으로 key에 값을 저장 (1일 때 *6)
        j = i - 1 # j의 값을 형성
        while j >= 0 and key < arr[j]: #j는 i가 실행되는 값만큼 차감 (i가 1일 때 *6/ j는 0으로 *1)
            # 0 & 6 < 0 => false
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key #i가 1일 때 *6/ j는 0으로 *1/ arr[j + 1]인 arr[1]은 6에서 6이다. 즉, 변화 없음
        print(arr)
    

arr = [1,6,9,3,4]
insertion_sort(arr)
print(arr)