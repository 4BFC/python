n = 'ObjectOrientedProgramming1 3.0 A+'
Alp = []
cnt = []  # 추가된 cnt 리스트 변수
exit_cnt = []
ex = []
# 알파벳 생성기
for _ in range(ord('a'), ord('z')+1):
    Alp.append(chr(_))
for i in Alp:  # Alp의 element를 i로 반환
    if i in n:  # i(n)가 n에 있는지 확인하는 조건문
        print(f"count : {i} : {n.count(i)}", end=" ")
        exit_cnt.append(i)
        cnt.append(n.count(i))
    else:  # i(n)에 없는 알파벳들
        print(f"except : {i} : {Alp.index(i)}", end=" ")
        ex.append(Alp[Alp.index(i)])  # 없는 알파벳들을 Alp리스트 index로 저장

print()
print()
print(Alp)
print(f"exit list is : {exit_cnt}")
print(f" cnt list is : {cnt}")
print(f"except list is : {ex}")
