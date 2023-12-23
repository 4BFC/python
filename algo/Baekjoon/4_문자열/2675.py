R = int(input())

for _ in range(R):
    S = input().split()
    for _ in range(len(S[1])):
        print(S[1][_] * int(S[0]), end="")
    print()

# print(len(S[1]))
# print(S, S[1][0])
# for _ in R:
#     for _ in range(len(S[1])):
#         P = S[1][_] * int(S[0])
# print(P)
