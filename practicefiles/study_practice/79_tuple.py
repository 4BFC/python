#tuple
t1 = (0);
t2 = (1,);
t3 = (1,2,3);
t4 = 1,2,3
t5 = ('a','b',('ab','cd'));
print(t5);
#del t5[0];

r_t = (1,2,3,4,8,9);
#r_t[0] = 12;
r_t = r_t[1:]; #1에서부터. 2,3,4,8,9
r_t = r_t[0:4]; #2,3,4,8
print(r_t);

#dic
dic = {'name':'py','phone':'0119993323','birth':'1118'};
a = {1:'hi'};
print(a);
a = {'a':[1,2,3]};
print(a);

a ={1:'a'};
a[2] = 'b';
a['name'] = 'pey';
a[3] = [1,2,3];
del a[1]
print(a);
print(a['name'])
print(dic.keys());
for k in dic.keys(): #반복문
    print(k);

print(list(dic.keys()));
print(dic.values());
print(dic.items());
print('name' in a);
