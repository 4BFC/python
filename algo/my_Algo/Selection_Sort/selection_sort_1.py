print("selection_sort");
def selection_sort(arr):
  n = len(arr)        #배열의 길이를 n으로 저장.
  for i in range(n):  #for문을 돌리기 위해 n만틈 반복하는 것.
    min_index = i     #값을 하나씩 min_index에 대입한다.
    print("i = ", i, "/", arr[i])
    for j in range(i+1, n): #i 다음 번째 값에서 부터 n번까지 범위를 지정.
      print("j = ", j, "/", arr[j])
      if arr[j] < arr[min_index]:   #최소 값을 비교한다. 만약 다음 번째 값이 min_index보다 크다면 새로운 min_index를 지정한다.
        min_index = j
      print(arr)
    arr[i], arr[min_index] = arr[min_index], arr[i] #if문의 조건이아니라 for문이 돌때 마다 두 정렬을 스왑해주는 역할이다. 즉, min_index값이 변동이 있을 때 스왑이 수행된다는 것을 알 수 있다.
      
arr = [2,3,5,1,7,0]
selection_sort(arr)
print(arr)