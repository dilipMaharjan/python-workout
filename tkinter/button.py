from tkinter import Tk,Button

root=Tk()
root.geometry('500x500')
# def print_name():
#     print('Dilip')def print_name():
#     print('Dilip')

# command executes the function
# button=Button(root,text="Click me",fg="Blue",command=print_name)

def print_name(event):
    print(event)

button=Button(root,text="Click me",fg="Blue")

'''
first argument is the button event,
<Button-1> is right click,
<Button-2> is middle cursor click,
<Button-3> is the left click
'''

button.bind('<Button-1>',print_name)
button.bind('<Button-2>',print_name)
button.bind('<Button-3>',print_name)
button.pack()

# binding arrow keys
root.bind('<Left>',print_name)
root.bind('<Right>',print_name)
root.bind('<Up>',print_name)
root.bind('<Down>',print_name)

root.mainloop()