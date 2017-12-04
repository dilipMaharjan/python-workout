from tkinter import *

root=Tk()

label_name=Label(root,text="Name:")
entry_name=Entry(root)
label_password=Label(root,text="Password:")
entry_password=Entry(root)
check_button=Checkbutton(root,text="Remember me")
button_sign_in=Button(root,text="Sign In")

label_name.grid(row=0,column=0,sticky="E")
entry_name.grid(row=0,column=1)
label_password.grid(row=1,column=0,sticky="E")
entry_password.grid(row=1,column=1)
check_button.grid(columnspan=2)
button_sign_in.grid(columnspan=2)

root.mainloop()