H, M = map(int, input().split())
C = int(input())
MC = (M + int(C))
print(f"check : {MC}")
if 60 <= MC:
    H += (int(MC / 60))
    if 60 < MC:
        print("check")
        M = MC % 60
else:
    M = MC
if H == 24:
    H = 0

print(H, M)
# print(int(M / 60))
