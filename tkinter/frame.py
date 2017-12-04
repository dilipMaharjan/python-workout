from tkinter import *

root=Tk()

# initialize frame
top_frame=Frame(root)

# add to window
top_frame.pack()

button_top =Button(top_frame,text="Click me",fg="Red")
button_top.pack(side=LEFT)

button_top1 =Button(top_frame,text="Click me",fg="Red")
button_top1.pack(side=LEFT)

bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)

button_bottom =Button(bottom_frame,text="Click me",fg="Purple")
button_bottom.pack()

root.mainloop()