

#label1 = Label(window, text = "아~ 집에 가고 싶어~")
#label2 = Label(window, text = "언제가지?", font =("궁서체", 30), fg = "blue")
#label3 = Label(window, text = "졸려", bg = "purple", width = 20, height = 5, anchor = SE)

#label1.pack()
#label2.pack()
#label3.pack()

#window.mainloop()

#--------------------------------------------------------
#photo1 = PhotoImage(file = "jeju1.gif")                
#label1 = Label(window, image = photo1)

#photo2 = PhotoImage(file = "jeju7.gif")
#label2 = Label(window, image = photo2)

#label1.pack(side = LEFT)
#label2.pack()
#window.mainloop()

#_----------------------------------------------------------

#button1 = Button(window, text = "파이썬 종료", fg="red", command = quit)

#button1.pack()

#window.mainloop()

#--------------------------------------------

#from tkinter import *
#from tkinter import messagebox

#def myFunc() :
#    messagebox.showinfo("강아지 버튼", "귀여운 강아지네~~~")

#window = Tk()

#photo = PhotoImage(file = "dog2.gif")
#button1 = Button(window, image = photo, command = myFunc)

#button1.pack()
#window.mainloop()

#----------------------------체크버튼---------------

from tkinter import *
from tkinter import messagebox

window = Tk()

def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요")
    else :
        messagebox.showinfo("", "체크버튼이 켜졌어요")
chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack() 
window.mainloop()
