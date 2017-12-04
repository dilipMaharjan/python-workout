from tkinter import *

root=Tk()

label=Label(root,text="Name:")
entry=Entry(root)
check_button=Checkbutton(root,text="Remember me")

label.grid(row=0,column=0)
entry.grid(row=0,column=1)
check_button.grid(columnspan=2)

root.mainloop()