from tkinter import *
root=Frame()
root.pack()
d = {"Ajay": 123, "Amit": 747, "Tina": 586, "Dino": 767, "RIYA": 212, "Fatehi": 787, "Gujar": 111,
     "Hash": 888}

w1 = Label(root, text="Name will display :")
w1.pack(side="bottom")
w2 = Label(root, text="Phone Number will display:")
w2.pack(side="top")


def List(event):
    L1 = lst.get(ACTIVE)
    print(L1)
    ph = d.get(L1)
    global w1, w2
    w1.config(text=L1)
    w2.config(text=ph)
lst = Listbox(root)
lst.config(selectmode=EXTENDED)
sbar = Scrollbar(root)
sbar.config(command=lst.yview)
lst.config(yscrollcommand=sbar.set)
sbar.pack(side=RIGHT, fill=Y)
lst.pack(side=LEFT, expand=YES, fill=BOTH)

lst.bind('<Double-1>', List)

for k, v in d.items():
    lst.insert('end', k)




root.mainloop()
