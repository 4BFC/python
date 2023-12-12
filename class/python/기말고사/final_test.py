from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("사칙연산")
root.geometry("500x150")

#함수 생성
def calculate_add(x,y) :    #더하기 함수
    if x != "" and y != "" :    #entry a,b중 입력되었을 때만 값을 계산하는 조건문
        answer = int(x) + int(y)
        result.configure(text = "[결과 값] " + str(answer))
        print(str(answer))
    else :
        result.configure(text = "[결과 값]  정수를 정확하게 입력하세요")
        print("다시입력하세요")
def calculate_min(x,y) :    #빼기 함수
    if x != "" and y != "" : #entry a,b중 입력되었을 때만 값을 계산하는 조건문
        answer = int(x) - int(y)
        result.configure(text = "[결과 값] " + str(answer))
        print(str(answer))
    else :
        result.configure(text = "[결과 값]  정수를 정확하게 입력하세요")
        print("다시입력하세요")
def calculate_mul(x,y) :    #곱하기 함수
    if x != "" and y != "" : #entry a,b중 입력되었을 때만 값을 계산하는 조건문
        answer = int(x) * int(y)
        result.configure(text = "[결과 값] " + str(answer))
        print(str(answer))
    else :
        result.configure(text = "[결과 값]  정수를 정확하게 입력하세요")
        print("다시입력하세요")
def calculate_div(x,y) :    #나누기 함수
    if x != "" and y != "" : #entry a,b중 입력되었을 때만 값을 계산하는 조건문
        if(y == '0') : #매개변수 y가 0일 경우 아래 messagebox함수를 실행시킨다.
            result.configure(text = "[결과 값] ")
            messagebox.showinfo("알람","0으로 나눌 수 없습니다.")
            print("0으로 나눌 수 없습니다.")
        else :
            answer = int(x) / int(y)
            result.configure(text = "[결과 값] " + str(answer)) 
            print(str(answer))
    else :
        result.configure(text = "[결과 값]  정수를 정확하게 입력하세요")
        print("다시입력하세요")

#위젯 생성하는 영
#entry
ent_num_a = Entry(root)
ent_num_b = Entry(root)
#button 배열로 설정하기
btn = ["더하기(+)","빼   기(-)","곱하기(*)","나누기(/)"]
#각 버튼의 함수를 불러올 때 작성한 함수들의 매개변수를 설정하기 위해서 lambda식을 이용해서 매개벼수를 설정할 수 있게 했다.
btn_add = Button(root,text=btn[0], command = lambda : calculate_add(ent_num_a.get(),ent_num_b.get()))
btn_min = Button(root,text=btn[1], command = lambda : calculate_min(ent_num_a.get(),ent_num_b.get()))
btn_mul = Button(root,text=btn[2], command = lambda : calculate_mul(ent_num_a.get(),ent_num_b.get()))
btn_div = Button(root,text=btn[3], command = lambda : calculate_div(ent_num_a.get(),ent_num_b.get()))
#label
integer_num_a = Label(root,text = "정수1")
integer_num_b = Label(root,text = "정수2")
notice = Label(root,text = "두 정수를 입력 후 4개의 연산자 중 하나를 클릭하세요.")
result = Label(root,text = "[결과 값]  ", fg="blue")

#위젯 배치하는 영역 : 각기 렌더링이 되는 순서대로 배치해야 한다.

#entry_label
integer_num_a.place(x=50,y=10)
integer_num_b.place(x=220,y=10)
#entry
ent_num_a.place(x=10,y=50)
ent_num_b.place(x=170,y=50)
#button
btn_add.place(x=330,y=10)
btn_min.place(x=400,y=10)
btn_mul.place(x=330,y=40)
btn_div.place(x=400,y=40)

#intro_label
notice.place(x=10,y=80)
result.place(x=10,y=100)

root.mainloop()
