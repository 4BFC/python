#중괄호
#key : value로 이루어져 있다.

#딕녀너리 쌍 추가
customer = {}
customer['name'] = '김사랑'
customer['job'] = '회사원'
customer['phone'] = '010-0000-1111'
print(customer)

#딕셔너리 요소 제
customer = {}
customer['name'] = '김사랑'
customer['job'] = '회사원'
customer['phone'] = '010-0000-1111'
print("원본 ==>",customer)
del customer['job']
print("삭제 후 ==>",customer)
customer['job'] = '학생'
print("변경  후 ==>",customer)
