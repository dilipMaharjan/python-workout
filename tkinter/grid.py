from tkinter import * 

root=Tk()
label_hello=Label(root,text="Hello")
label_hi=Label(root,text="Hi")
label_ok=Label(root,text="Ok")
label_hello.grid(row=0,column=0)
label_hi.grid(row=0,column=1)
label_ok.grid(row=1,column=1)

root.mainloop()
