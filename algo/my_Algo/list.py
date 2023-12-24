# for문을 사용해서 입력값 받기
# N = list(map(int, input().split()))  # int list 생성
# print(N)

# N = list(input().split())  # str list 생성
# print(N)

# 잘못된 대입 방법
# for _ in range(2):
#     # N = [map(str, input().split())]  # 왜 여기서 추가되지 않는 거 처럼 보이는가.
#     # for문을 돌려가며 값을 새로 생성한다. 즉, N에 새로운 list를 계속해서 할당하는 것이다. 그래서 마지막에 입력한 list만 아래 for문에서 확인이 되는 것이다. 따라서 N을 list처럼 계속 해서 값을 넣기 위해선 append를 사용해야한다.
# print(N)
#     N = list(input().split())
# for _ in range(len(N)):
#     print(N[_])

# N = []
# for _ in range(2):
#     N.append(input())
# print(N) #append를 사용하지 않고대입할 수 잇는 방법은?

# N = []
# for _ in range(2):
#     N = input()  # 이렇게하면 앞전에 list였던 N은 일반 변수로 변경된다.
# print(N)  # append를 사용하지 않고대입할 수 잇는 방법은?

# N = []
# for _ in range(ord('A'), ord('Z')):
#     N.append(chr(_))

# for i in range(len(N)):
#     print(N[i])
