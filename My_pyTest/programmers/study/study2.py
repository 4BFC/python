t1 = (0,1,2,3,4,5,6,7,8,9)
print(t1[0:10:2]) #tuple
l1 = list(t1[0:10:2]) #list
print(l1) #2배수
del(l1[0]) #0을 삭제
print(l1)
l1.append(10)
tmp = [] #list
for a in l1 :
  print(a)
  tmp.append(a)
print(tmp)
#print(t1.index(2))

s1 = "hello, my name is Kim"
s1_p = s1.split(' ')
print(s1_p, len(s1_p), type(s1_p[0]))
