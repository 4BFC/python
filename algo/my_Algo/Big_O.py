#O(1)
def getFirstElement(arr) : 
  return arr[0]

#O(log n) = 이진탐색
#연산 수행 능력이 i*2로 줄어들면서 연산 수행 그래프가 완만해진다.
def log_counter(n):
    loop_count = 0
    i = 2
    for i in range(2, n + 1, i * 2):
        loop_count += 1
    return loop_count

print(log_counter(16))

#O(n) - Linear Time
#선형 시간 복잡도, 인풋증가에 비례
def count_Characters(str) :
    count = 0
    for char in str :
      count += 1
    return count
print(count_Characters("김동우우우"))

#O(n^2) - Quadratic Time
#2차 시간 복잡도, 인풋의 증가 시 n의 제곱 비율로 증가
#반복문 2개가 중첩될 때

def build_matrix(arr):
    matrix = []
    for i in range(len(arr)):
        matrix.append([])
        for j in range(len(arr[i])):
            matrix[i].append(arr[i][j])
    return matrix
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = build_matrix(arr)
for row in result :
    print(row)

#O(n!)
#팩토리얼 시간 복잡도, 가장 느린 연산

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 예시: 팩토리얼 계산
n = 5
result = factorial(n)
print(f"{n}의 팩토리얼은 {result}입니다.")
