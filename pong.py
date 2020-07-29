import pygame
import random

class bot(object):
    wi  =0 
    def __init__(self,start):
        self.pos = start
        
    def moveup(self):
        self.wi =  -1
        
    def movedown(self):
        self.wi =  1
        
        
    def draw(self,surface):
        self.pos += self.wi
        if self.pos <= 101:
            self.pos = 103
        elif self.pos + 100 >= hight - 1:
            self.pos = hight - 101
        pygame.draw.rect(surface, (0,0,0), ((width -25),self.pos,23,100))
        
        

class bord(object):
    wi = 0
    def __init__(self,start):
        self.pos = start
    def move(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_UP]:
                    bt.moveup()
                elif keys[pygame.K_DOWN]:
                    bt.movedown()
                elif keys[pygame.K_a]:
                    self.wi =  -1
                elif keys[pygame.K_z]:
                    self.wi =  1
                else:
                    bt.wi =0 
                    self.wi = 0
        if self.pos <= 101:
            self.pos = 103
        elif self.pos + 100 >= hight - 1:
            self.pos = hight - 101
        
    def draw(self,surface):
        self.pos += self.wi
        pygame.draw.rect(surface, (0,0,0), (2,self.pos,23,100))        
        

class ball(object):
    
    def __init__(self,x = 350,y = random.randint(101,499),xf = -1,yf = -1):
        self.x = x
        self.y = y
        self.xf = xf
        self.yf = yf
        self.sb= 0
        self.sbt = 0
    def reset(self):
        self.x = 400
        self.y = random.randint(101,hight-1)
        self.xf = -1
        self.yf = -1
       
    
    def move(self):
        self.x += self.xf
        self.y += self.yf
        
        if self.y - 10 <= 101:
            self.yf = 1
        elif self.y + 10 >= hight -1:
            self.yf = -1
        elif self.x + 10 >= (width - 26) and (bt.pos < self.y and bt.pos + 100 > self.y):
            self.xf = -1
        elif self.x + 10 >= width:
            self.sb += 1
            self.reset()
        elif self.x -10 <= 25 and (b.pos < self.y and b.pos + 100 > self.y):
            self.xf  = 1
        elif self.x <= 0:
            self.sbt += 1
            self.reset()
        if self.sb == 10 or self.sbt == 10:
            pygame.quit()
        
    def draw(self,surface):
        pygame.draw.circle(surface, (255,0,0),(self.x,self.y), 10)
        
def redrawWindow(surface):
    #global b
    surface.fill((69,139,116))
    pygame.draw.rect(surface, (0,0,0),((width/2 - 3),101,5,400))
    pygame.draw.rect(surface, (0,0,0),(1,97,700,5))
    pygame.draw.rect(surface, (0,0,0),(1,500,700,5))  
    b.draw(surface)
    bt.draw(surface)
    c.draw(surface)

    scoreline(surface)
    pygame.display.update()


    
def scoreline(surface):
    pygame.init()
    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render(str(c.sb), True, (255, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = 150
    textrect.centery = 50
    surface.blit(text, textrect)
    
    ds = basicfont.render(str(c.sbt), True, (255, 0, 0), (255, 255, 255))
    dsrect = ds.get_rect()
    dsrect.centerx = 450
    dsrect.centery = 50
    surface.blit(ds, dsrect)

    bfont = pygame.font.SysFont(None, 25)
    text = bfont.render("Left player play with A and Z. Right player play with up down arow key", True, (255, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = 300
    textrect.centery = 540
    surface.blit(text, textrect)
    
def main():
    global b,bt,c,width,hight,h
    width  = 600
    hight = 500
    h = int(hight/2)
    win = pygame.display.set_mode((width, hight +  80))
    clock = pygame.time.Clock()
    #pygame.draw.rect(win, (0,0,0),(398,1,5,600))  
    b = bord(h)
    bt =  bot(h)
    c = ball()
    while True:
        pygame.time.delay(-100)
        clock.tick(500)
        b.move()
        #bt.move()
        c.move()
        
        redrawWindow(win)
        
main()
