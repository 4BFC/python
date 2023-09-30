print("bubble_sort")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]

a = ["test"]
bubble_sort(a)
print(a)
'''
print(a)

def bubble_sort(arr):
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
'''
