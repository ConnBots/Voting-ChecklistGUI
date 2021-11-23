from tkinter import *
master = Tk()

def var_states():
   print("Group1: %d,\nGroup2: %d,\nGroup3 %d, \nGroup4 %d" % (var1.get(), var2.get(), var3.get(), var4.get()))

Label(master, text="Group Checklist").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Group1", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Group2", variable=var2).grid(row=2, sticky=W)
var3 = IntVar()
Checkbutton(master, text="Group3", variable=var3).grid(row=3, sticky=W)
var4 = IntVar()
Checkbutton(master, text="Group4", variable=var4).grid(row=4, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=6, sticky=W, pady=4)
mainloop()