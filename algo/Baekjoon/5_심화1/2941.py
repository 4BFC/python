Alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = "dz=ak"
cnt = []
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
