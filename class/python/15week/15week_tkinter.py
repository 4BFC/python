from tkinter import *
root = Tk()

root.title("위젯배치")

btn1 = Button(root, text ="버튼배치1") #이미지로 변환 해보기
btn2 = Button(root, text ="버튼배치2")
btn3 = Button(root, text ="버튼배치3")
'''
btn1.pack(side=LEFT, padx = 20, pady = 30)
btn2.pack(side=LEFT, padx = 20, pady = 30)
btn3.pack(side=LEFT, padx = 20, pady = 30)
'''


btn1.pack(side=LEFT, ipadx = 20, ipady = 30)
btn2.pack(side=LEFT, ipadx = 20, ipady = 30)
btn3.pack(side=LEFT, ipadx = 20, ipady = 30)

root.mainloop()
