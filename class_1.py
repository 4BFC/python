# print("hi")
# a = 10
# b = 5
# print("check\t")
# print( a + b)
# a_b = [b]
# print(a_b)
# s = "korean"
# print(s);

# print(1,2,3)
# int Num;
# input('1을 입력하세요')
# if(Num == 1)
# {print("hi")}

print("\n\t김왼손_1~15강\n")

my_int = 1
memory = my_int + 100
print("*ready","\n",
my_int + my_int,"\n",
#my_int * 100
memory,"\n",
)

my_float = 0.34
My_bool = True
print("*Numeric","\n",
my_float,"\n",
type(my_float),"\n",
type(my_int),"\n",
type(My_bool),"\n",
My_bool,"\n",
)

my_List = []
my_List = [1,2,3]
students = ['a', 'b','c']
print("*List\n",
students,"\n",
)
for std in students : print(std)

import random
print(random.choice(students))
students.append('aa')
print(students)

students[0] = "dd"
print(students)

print(
"\ntuple : 값변경을 못함","\n",
"Dictionary : '김왼손' : '남' _ 이런 식으로 표기\n",
float(my_int),"\n"
,str(my_int),'\n'
,type(str(my_int))
)

my_str = "Coding"

print(my_str,"\n",
list(my_str),"\n")

my_str = "김씨가족"
my_str = 'Change'
my_str = """hi
my
name"""

print("string\n",
my_str,"\n")

my_str = 'My name is %s' % 'Dong Woo'

print("Formatting : %\d \n",
my_str,"\n",
'%d %d' % (1,2),"\n",
'%f' % 3.14 , "\n\n",
"\'{}\'.format() : Mathod(Funtion)\n\n",
'My name is {}'.format('kim Woo'),"\n",
'{} * {} = {}'.format(2, 3, 2*3),"\n"
'{1} * {0} = {2}'.format(2, 3, 2*3),"\n"#주소=>{1},{0},{2} : 2, ,3, 2*3 : 
)

my_name = "김동우 집이다."
print("Indexing : 주소, 위치\n",
my_name[4],"\n",
my_name[-1]
)


