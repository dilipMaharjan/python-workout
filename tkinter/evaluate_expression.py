from tkinter import *

root=Tk()

def evaluate(event):
    data=express_text_box.get()
    label_ans.configure(text='Answer:'+str(eval(data)))

label=Label(root,text="Enter expression")
express_text_box=Entry(root)
label_ans=Label(root)


express_text_box.bind('<Return>',evaluate)
label.pack()
express_text_box.pack()
label_ans.pack()

root.mainloop()