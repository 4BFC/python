print("bubble_sort");
def bubble_sort(arr):
    n = len(arr) #n에 arr 매개변수의 배열 길이를 답아낸다. 이는 반복문의 기준을 위한 변수이다.
    for i in range(n):  #range()함수를 통해서 해당 반복의 범위를 선정해준다.
        #i번째는 첫번째 점검을 하는 standard이다. 
        print("i = ", i, "/", arr[i])
        #j번째로 넘어가서 디테일한 점검으로 차순을 맞춰가는 것이다.
        for j in range(0, n-i-1): #i를 기준으로 j에서 지정된 범위를 모두 스크롤링하면서 아래 if문 조건을 맞춰본다.
            #-1을 하는 이유는 0부터 시작하기 때문에 len(arr)의 길이를 맞추기 위해서다.
            print("j = ", j, "/", arr[j])
            if arr[j] > arr[j+1]:# 현 j번째와 다음 j번째를 비교한다 이후 해당 조건에 도달하면 현 위치에서 작은 숫자를 앞으로 보내고 큰 숫자는 뒤로 보내는 것이다.
                arr[j], arr[j+1] = arr[j+1], arr[j] #

arr = [2,3,5,1,6,4]
bubble_sort(arr)
print(len(arr))
print(arr)