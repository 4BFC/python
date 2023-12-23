N = list(str(input()))
c = ""
for _ in range(97, 122+1):
    c += chr(_)

for _ in range(len(N)):
    if c.index(N[_]):
        print(c.index(N[_]))
    else:
        print(0)
# print(ord('a'), ord('z'))
