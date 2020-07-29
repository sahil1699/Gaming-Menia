from tkinter import *
import os


def sanke():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'Thesnakegame.py')
    os.system(f'py {file_path}')
##    os.system('python Thesnakegame.py')
def btb():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'ballbrik.py')
    os.system(f'py {file_path}')
    
def fb():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'flapb.py')
    os.system(f'py {file_path}')

def pong():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path,'pong.py')
    os.system(f'py {file_path}')

def games():
    bs = Button(r ,text="Snake Game ", height=2, width=20,command = sanke)
    bs.place(x=70,y=150)

    bs = Button(r ,text="Ball Break Bricks", height=2, width=20,command = btb)
    bs.place(x=300 ,y=150)

    bs = Button(r ,text="Fallpy Bird", height=2, width=20,command = fb)
    bs.place(x=70 ,y= 250)

    bs = Button(r ,text="Pong", height=2, width=20,command = pong)
    bs.place(x=300,y= 250)
    

def maniyawin():
    global r
    r = Tk()
    r.geometry("530x400")

    var = StringVar()
    label = Label( r, textvariable=var, relief=RAISED )

    var.set("THE GAMEING MENIA")
    label.config(width=200)
    label.config(font=("Courier", 35))
    label.pack()

    var2 = StringVar()
    label2 = Label( r, textvariable=var2, relief=RAISED )
    var2.set("Play amazing games and have fun !!")
    label2.config(width=200)
    label2.config(font=("Arial", 15))
    label2.pack()
    
    games()

    

    r.mainloop()

maniyawin()
