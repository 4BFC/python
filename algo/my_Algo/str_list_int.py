# 숫자는 list로 전환을 해줘야한다.
N = list(map(int, input()))
print(N, type(N), type(N[0]))  # N은 list로 반환되고 N[0]인 list요소는 int로 반환된다.
for _ in N:
    print(type(_), end=" ")
print("\n")
# 문자열은 list로 반환되고 구성이되기 때문에 list를 전환할 필요 없다.
N = input()
# 여기에 있는 모든 값들은 str이다. 그렇다면 각 요소들을 int로 전환할 수는 없을까?
# 아마도 int(N[0])이렇게 변환하면 될 것같지만 오류가 난다.
print(N, type(N), type(N[0]))
for _ in N:  # 여기서 _는 str인 것이다. 절대로 int가 아니다 그렇다면 이를 염두하고 코드를 변경하면 아래와 같다.
    print(type(_), end=" ")

print("\n")
for _ in N:
    print(type(int(N[int(_)-1])), end=" ")
print("\n")
#
for _ in range(len(N)):
    print(type(int(N[_])), end=" ")
print("\n")

N = int(input())
for _ in range(N):
    print(_, end=" ")
