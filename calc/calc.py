import tkinter

root = tkinter.Tk()

op1 = tkinter.Entry(root)
op1.grid(row=0, column=0)
btn_add = tkinter.Button(root, text='+')
btn_subtract = tkinter.Button(root, text='-')

tkinter.mainloop()

