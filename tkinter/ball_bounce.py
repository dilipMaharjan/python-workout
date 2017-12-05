from tkinter import *
import time
import random


root=Tk()

root.title("Bounce")
root.resizable(0,0)
root.wm_attributes('-topmost',1)

canvas=Canvas(root,width=500,height=500,bd=0,highlightthickness=0)
canvas.pack()
canvas.update()

class Ball:
    def __init__(self,paddle,canvas, color):
        self.paddle=paddle
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        start=[-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.bottom_collision=False

    def paddle_collision(self,ball_pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if ball_pos[2]>=paddle_pos[0] and ball_pos[0]<=paddle_pos[2]:
            if ball_pos[3]>=paddle_pos[1] and ball_pos[3]<=paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.bottom_collision=True
            canvas.create_text(245,100,text="Game Over")
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        if self.paddle_collision(pos)==True:
            self.y=-3

class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()

        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)

        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0

    def turn_left(self,evnt):
        self.x=-2

    def turn_right(self,evnt):
        self.x=2

paddle=Paddle(canvas,'blue')
ball=Ball(paddle,canvas,'red')

while 2<3:
    if not ball.bottom_collision:
        ball.draw()
        paddle.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)

root.mainloop()