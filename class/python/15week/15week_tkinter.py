from tkinter import *
root = Tk()

root.title("위젯배치")

def command_test (a) :
    print(f"this is {a} button")
img = PhotoImage(file = 'cat.gif')
btn1 = Button(root, text ="버튼배치1", command = lambda : command_test(1)) #command를 추가해볼 
btn2 = Button(root, text ="버튼배치2", command = lambda : command_test(2)) #이미지로 변환 해보기
btn3 = Button(root, text ="버튼배치3", command = lambda : command_test(3))
btn4 = Button(root, image = img , command = lambda : command_test('img'))
'''
btn1.pack(side=LEFT, padx = 20, pady = 30)
btn2.pack(side=LEFT, padx = 20, pady = 30)
btn3.pack(side=LEFT, padx = 20, pady = 30)
'''

btn1.pack(side=LEFT, ipadx = 20, ipady = 30)
btn2.pack(side=LEFT, ipadx = 20, ipady = 30)
btn3.pack(side=LEFT, ipadx = 20, ipady = 30)
btn4.pack(side=LEFT, ipadx = 20, ipady = 30)
#btn4.place(x=15,y=50)

root.mainloop()
 
