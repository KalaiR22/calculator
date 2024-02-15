
from tkinter import  *
window = Tk()
window.title('calculator')
window.geometry('570x600+100+200')
window.resizable(False, False)
window.config(bg='#17161b')

cal_equation =''
def show(value):
    global cal_equation
    cal_equation+=value
    label_result.config(text=cal_equation)
label_result = Label(window, width=25, height = 2, text='', font=('arial', 30))
label_result.pack()

def clear():
    global cal_equation
    cal_equation=''
    label_result.config(text=cal_equation)

def calculate():
    global cal_equation
    result = ''
    if cal_equation != "":
        try:
            result= eval(cal_equation)
        except:
            result='Error'
            cal_equation=''
        label_result.config(text=result)





Button(window, text='C', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#3697f5', command= lambda: clear()).place(x=10,y=100)
Button(window, text='/', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('/')).place(x=150,y=100)
Button(window, text='%', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('%')).place(x=290,y=100)
Button(window, text='*', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('*')).place(x=430,y=100)

Button(window, text='7', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('7')).place(x=10,y=200)
Button(window, text='8', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('8')).place(x=150,y=200)
Button(window, text='9', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('9')).place(x=290,y=200)
Button(window, text='-', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('-')).place(x=430,y=200)

Button(window, text='4', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('4')).place(x=10,y=300)
Button(window, text='5', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('5')).place(x=150,y=300)
Button(window, text='6', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('6')).place(x=290,y=300)
Button(window, text='+', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('+')).place(x=430,y=300)

Button(window, text='1', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('1')).place(x=10,y=400)
Button(window, text='2', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('2')).place(x=150,y=400)
Button(window, text='3', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('3')).place(x=290,y=400)
Button(window, text='0', width=11, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('0')).place(x=10,y=500)

Button(window, text='.', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('.')).place(x=290,y=500)
Button(window, text='=', width=5, height=3, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#96B6C5', command=lambda: calculate()).place(x=430,y=400)
window.mainloop()