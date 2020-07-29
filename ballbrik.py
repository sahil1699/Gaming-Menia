import pygame
from tkinter import *
import math
import os

os.environ['SDL_VIDEO_CENTERED'] = "True"


PAUSE = False

class bord(object):
    
    def __init__(self,start):
        self.pos = start
        self.wi = 0
        
        
    def move(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.wi =  -1
                elif keys[pygame.K_RIGHT]:
                    self.wi =  1
                elif keys[pygame.K_p]:
                    bal.xf = 0
                    bal.yf = 0
                    PAUSE  = True
                    pause('Game Paused','normal')
                    break
                else:
                    self.wi = 0
        if self.pos <= 1:
            self.pos = 1
        elif self.pos + 100 >= 499:
            self.pos = 399
            
    def ballonbord(self,p):
        if self.pos < p and (self.pos + 100) >p:
            return 1
        else :
            return 0
        
    def draw(self,surface):
        self.pos += self.wi
        pygame.draw.rect(surface, (0,0,0), (self.pos,476,100,23))
    
class brick(object):
    w = 500
    rows = 20
    cols = 10
    l =[]
    def __init__(self):
        for i in range(13):
            a = []
            for j in range(10):
                a.append(1)
            self.l.append(a)
##        for i in range(7):
##            a = []
##            for j in range(10):
##                a.append(0)
##            self.l.append(a)
	
    def destroy(self,ball):
        
        if int((ball.y -16)/25) < 13 and self.l[int((ball.y -16)/25)][int(ball.x/50)] == 1:
            self.l[int((ball.y -16)/25)][int(ball.x/50)] = 0
            
        elif int(ball.y/25)<13 and self.l[int(ball.y/25)][int((ball.x+16)/50)] == 1:
            self.l[int(ball.y/25)][int((ball.x+16)/50)] = 0
            
        elif int((ball.y + 16)/25) <13 and self.l[int((ball.y + 16)/25)][int(ball.x/50)] == 1:
            self.l[int((ball.y + 16)/25)][int(ball.x/50)] = 0

        elif int(ball.y/25) <  13 and self.l[int(ball.y/25)][int((ball.x-16)/50)] == 1:
            self.l[int(ball.y/25)][int((ball.x-16)/50)] =0
            
    def draw(self,surface):
        
        widthbw = self.w // self.cols
        hightbw = self.w // self.rows
        for i in range(10):
            for j in range(13):
                if self.l[j][i] == 1:
                    pygame.draw.rect(surface, (0,0,255), (i*widthbw+1,j*hightbw+1, widthbw-2, hightbw-2))
            

class ball(object):
    def __init__(self,x=250,y=460,xf = -1,yf = -1):
        self.x = x
        self.y = y
        self.xf = xf
        self.yf = yf
        
    def motion(self):
        self.x += self.xf
        self.y += self.yf
        ic = int (self.x/50)
        ir = int (self.y/25)
        

        if not PAUSE :
        
            if int(self.y/25)< 13 and (brick.l[int(self.y/25)][int((self.x-16)/50)]) or self.x - 16 <= 0 :
                self.xf = 1
                return 1
            elif int((self.y -16)/25) <  13 and (brick.l[int((self.y -16)/25)][int(self.x/50)]):
                self.yf = 1
                return 1
            elif int(self.y/25)<13 and  brick.l[int(self.y/25)][int((self.x+16)/50)] or self.x + 16 >= 499:
                self.xf = -1
                return 1
            elif int((self.y + 16)/25) < 13 and brick.l[int((self.y + 16)/25)][int(self.x/50)]:                
                self.yf = -1
                return 1
            elif self.y + 16 >= 490:
                f = bo.ballonbord(self.x)
                if f == 1:
                    self.yf = -1
                    return 1
                else: return 0
            elif self.y >550:
                return 0
            
    def draw(self,surface):
        pygame.draw.circle(surface, (255,0,0),(self.x,self.y), 16)

'''       
    def leftstrick(self):
        self.xf = 1

    def rightstrick(self):
        self.xf = -1

    def upstrick(self):
        self.yf = 1
        
    def downstrick(self):
        self.yf = -1
'''    
        
def redrawwin(surface):
    global width,br,bo,bal
    surface.fill((255,255,255))
    br.draw(surface)
    bo.draw(surface)
    bal.draw(surface)
    drawpause(surface)
    pygame.display.update()

##def message_box(subject, content = "uii"):
##    root = tk.Tk()
##    root.attributes("-topmost", True)
##    root.withdraw()
##    messagebox.showinfo(subject, content)
##    try:
##        root.destroy()
##    except:
##        pass
    
def reset():
    global br,bo, bal
    for i in range(13):
        for j in range(10):
            br.l[i][j] = 1
       
    br=brick()
    
    bo = bord(201)
    bal = ball()
    

def pause(t,tx):
    
    
    def res():
        root.destroy()
        PAUSE  = False
        main()
        
        
    def restart():
        PAUSE  = False
        root.destroy()
        reset()
        
        
    def exit():
        pygame.quit()
        root.destroy()
        
        
    root = Tk()
    
    root.geometry("200x250")
    #l = Label(root, text = lt)
    b = Button(root, text="Resume", height=2, width=20,command=res,state = tx)
    r = Button(root, text="Restart", height=2, width=20,command=restart)
    e = Button(root, text="Exit", height=2, width=20,command=exit)

    #l.place(x=18, y=10)
    b.place(x=20, y=50)
    r.place(x=20, y=100)
    e.place(x=20, y=150)

    root.mainloop()


def drawpause(surface):
    pygame.init()
    basicfont = pygame.font.SysFont(None, 48)
    
    text = basicfont.render("Press 'P' to pause", True, (255, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = 250
    textrect.centery = 520
    surface.blit(text, textrect)




def main():
    global width,br,bo,bal
    width = 500
    win  = pygame.display.set_mode((width, width + 40))
    
    br = brick()
    bo = bord(201)
    bal = ball()
    clock = pygame.time.Clock()
    r = 1
    stop = True
    while stop:
        pygame.time.delay(-10)
        clock.tick(150)
        bo.move()
        r = bal.motion()
        br.destroy(bal)
        if r == 0:
            PAUSE = True
            pause('You Lost','disabled')
            
            
            
            

        redrawwin(win)
        
main()        
