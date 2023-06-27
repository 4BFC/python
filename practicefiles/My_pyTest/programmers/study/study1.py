from cgi import print_directory


dic = {'name':'pay','phone':'01','birth':'100'}
dic['name'] = 'key'

print(dic.values())
print(dic.keys())
print(dic)
print(dic.items())
print(dic.get('birth'))

li_st = [1,2,3,4]
li_st.append(12)
print(li_st[:2])
print(li_st)
print(li_st in [1])

a = {}
print(type(a))

a = set([1,2,3])
print(a)