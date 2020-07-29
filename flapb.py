import pygame
import random
import os
from tkinter import *

os.environ['SDL_VIDEO_CENTERED'] = "True"

pygame.font.init()

win_width = 500
win_heigth  = 700

bird_imgs = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
             pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
bg_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

stat_font = pygame.font.SysFont("comicsans", 50)


class Bird:
    imgs  =  bird_imgs
    max_rotation = 25
    rot_vel = 20
    animation_time = 5

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count =  0
        self.vel =0
        self.height = self.y
        self.img_count = 0
        self.img = self.imgs[0]
    def jump(self):
        self.vel = -7.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d =  self.vel * self.tick_count + 1.5  * self.tick_count**2

        if d >= 16:
            d = 16
        if d < 0:
            d -= 4
        
        self.y = self.y + d
        if d < 0 or self.y < self.height + 50 :
            if self.tilt < self.max_rotation :
                self.tilt = self.max_rotation
        else:
            if self.tilt > -90:
                self.tilt -= self.rot_vel
                
    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.animation_time:
            self.img = self.imgs[0]
        elif self.img_count < self.animation_time*2:
            self.img = self.imgs[1]
        elif self.img_count < self.animation_time*3:
            self.img = self.imgs[2]
        elif self.img_count < self.animation_time*4:
            self.img = self.imgs[1] 
        elif self.img_count < self.animation_time*4 + 1:
            self.img = self.imgs[0]
            self.img_count = 0
           
        if self.tilt <= -80:
            self.img = self.imgs[1]
            self.img_count = self.animation_time * 2
            
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Pipe:
    
    gap = 200
    vel = 5

    def __init__(self,x):
        self.x = x
        self.heigth = 0
        self.gap = 200
        self.top = 0
        self.bottom = 0
        self.pipe_top =  pygame.transform.flip(pipe_img, False, True)
        self.pipe_bottom =  pipe_img
        
        self.passed = False
        self.set_height()
        
    def set_height(self):
        self.heigth = random.randrange(50, 350)
        self.top = self.heigth -  self.pipe_top.get_height()
        self.bottom = self.heigth + self.gap

    def move(self):
        self.x -= self.vel

    def draw(self,win):
        win.blit(self.pipe_top,(self.x, self.top))
        win.blit(self.pipe_bottom,(self.x, self.bottom))

    def collide(self, bird):
        bird_mask  = bird.get_mask()
        top_mask =  pygame.mask.from_surface(self.pipe_top)
        bottom_mask =  pygame.mask.from_surface(self.pipe_bottom)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        if bird.y > 600:
            return True
        return False

    
class Base:
    vel = 5
    width = base_img.get_width()
    img = base_img

    def __init__(self,y):
        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def move(self):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if self.x1 + self.width < 0 :
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0 :
            self.x2 = self.x1 + self.width
            
    def draw (self,win):
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))
        
def pause(t,tx,s):
    
    lt = '%s \n your score is %d'% (t,s)
  
    def restart():
        root.destroy()
        main()
        
    def exit():
        pygame.quit()
        root.destroy()
        
        
    root = Tk()
    
    root.geometry("200x250")
    l = Label(root, text = lt)
    #b = Button(root, text="Resume", height=2, width=20,command=res,state = tx)
    r = Button(root, text="Restart", height=2, width=20,command=restart)
    e = Button(root, text="Exit", height=2, width=20,command=exit)

    l.place(x=18, y=10)
    #b.place(x=20, y=50)
    r.place(x=20, y=100)
    e.place(x=20, y=150)

    root.mainloop()        
    
    
def draw_window(win, bird, pipes, base,score):
    win.blit(bg_img,(0,0))
    for pipe in pipes:
        pipe.draw(win)
    text = stat_font.render("Score: "+ str(score),1,(255,255,255))
    win.blit(text, (win_width -10 - text.get_width(), 10))
    base.draw(win)
    bird.draw(win)
    pygame.display.update()

def main():
    bird = Bird(230,250)
    base = Base(630)
    pipes = [Pipe(700)] 
    win = pygame.display.set_mode((win_width,win_heigth))
    clock = pygame.time.Clock()
    score = 0
    
    run = True
    while run:
        clock.tick(25)
        
        bird.move()
        rem = []
        add_pipe = False
        for pipe in pipes:
            if pipe.collide(bird):
                pause('You Lost','disabled',score)
                pygame.quit()
                
            if pipe.x + pipe.pipe_top.get_width()< 0 :
                rem.append(pipe)
                
            if not pipe.passed and pipe.x <bird.x:
                pipe.passed = True
                add_pipe = True
                
            pipe.move()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()  
        
        keys = pygame.key.get_pressed()

        for key in keys:
            if keys[pygame.K_SPACE]:
                bird.jump()
            if keys[pygame.K_p]:
                pause('Game Paused','normal',score)
        
        
        
           
        if add_pipe:
            score += 1
            pipes.append(Pipe(700))


        

        
        for r in rem :
            pipes.remove(r)
        if bird.y + bird.img.get_height() > 630:
            pass
        
        base.move()
        draw_window(win, bird,pipes,base,score)
        
    pygame.quit()
    quit()

main()


