from tkinter import *
root = Tk()
root.title("image 조작하기")
root.geometry("720x450")


#-------------------- image area --------------
#이미지 불러오기
brain = PhotoImage(file="smile.png")
#이미지 위젯 생성
lbl_img = Label(root, image = brain)

#img위치 변수
current_x = 100
current_y = 100

#img 위젯 위치 설정 
lbl_img.place(x = current_x, y = current_y)

def new_pos(x,y) : #x,y
    current_x = x
    current_y = y
    #이미지의 위치가 event 위젯 영역에 침범하지 않기 위한 if문
    if int(x) > 100 :
        lbl_img.place(x = current_x, y = current_y)
        print("check", current_x, current_y)
    else :
        #초과 될 경우 경고문을 활성
        print("Whatch OUT!!")
    

#--------------- 위젯 생성 ---------------
x_lbl = Label(root, text = "input pos(x)")
x_ent = Entry(root, width = 20)


y_lbl = Label(root, text = "input pos(y)")
y_ent = Entry(root, width = 20)

#btn_create
btn = Button(root, text = "변경", command = lambda : new_pos(x_ent.get(), y_ent.get()))#lambda : new_pos(x_ent.get(), y_ent.get())



# ---------------위젯 위치 지정---------------
x_lbl.place(x = 10, y = 20)
x_ent.place(x = 90, y = 20)

y_lbl.place(x = 10, y = 50)
y_ent.place(x = 90, y = 50)

#btn_place
btn.place(x = 10, y = 70)

root.mainloop()
