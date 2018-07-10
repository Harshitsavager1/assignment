#question_1
from tkinter import *

root = Tk()
root.geometry('600x500')
root.title('''Harshit''')
w = Label(root, text="Hello World",font='BOLD')
w.pack()

button = Button (root, text="EXIT", command=root.destroy)
button.pack(side=BOTTOM)
root.mainloop()


#question_2
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
top.title('''Harshit''')
top.configure(background='#708090')

def hello():
   messagebox.showinfo('''That's true''', "You look precious when you smile buddy :P")

B1 = Button(top, text = "Click it", bg='#a52a2a',fg='white',command = hello)
B1.place(x = 50,y = 50)
B1.pack(fill='both')
top.mainloop()


#question_3
from tkinter import *
r=Tk()
r.title('Harshit')
r.configure(background='#708090')
r.geometry('500x500')
l1= Label(r, text='''Click the above button & i'll change:p''', bg = '#ffa07a')

def change():
    l1.config(text='''I told you i'll change :D''', bg = '#8470ff')
b = Button(r, text= 'Click',bg='#0000ff',fg='black',command=change)
b.pack(fill='both')
l1.pack()


button=Button(r, text='exit', command=r.destroy, bg='grey', fg='white')
button.pack(side="bottom", fill='both', expand=False)




r.mainloop()


#question_4
def ptext():
    global e
    string = e.get() 
    print(string)   

from tkinter import *
root = Tk()
root.geometry('600x500')
root.title('Harshit')
e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='Click to print',command=ptext)
b.pack(side='bottom')
root.mainloop()

