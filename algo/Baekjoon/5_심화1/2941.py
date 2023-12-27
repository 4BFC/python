# 무엇이 어떻게 이루어 졌는지 생각해 볼 필요가 있다. 기준을 잘 찾아야 함..
Alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = "dz=ak"
cnt = []
# 작은거에서 부터 큰걸로
for i in N:
    print(f"{i} : ")
    for ii in Alp:
        if ii in N:
            print(f"in is => {ii}")
            print(f"ii => {ii}")
            cnt.append(N.count(ii))
            # cnt += 1
        else:
            print("None")
        # print(N.count(i))
        # print(N.count(ii))

print(cnt)
print(set(cnt))
print(sum(set(cnt)))
