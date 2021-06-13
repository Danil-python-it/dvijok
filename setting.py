from pygame import *
import random

class PLAYER(sprite.Sprite):

    def __init__(self,x_coor,y_coor,width,height,image_list,Window,HorizontX=1000,HorizontY=800,step=5):
        super().__init__()
        self.rect = Rect(x_coor,y_coor,width,height)
        self.image_list = image_list
        self.body = transform.scale(self.image_list["body"],(self.rect.width,self.rect.height))
        self.stepX = self.stepY = self.setting_step = step  
        self.type_animation = None
        self.WIDTH = HorizontX
        self.HEIGHT = HorizontY
        self.window = Window
        self.stutus_flip = False
        self.num_body = self.timer = 0

    def update(self):
        going = key.get_pressed()
    
        if going[K_RSHIFT] and self.stepX == self.setting_step and self.stepY == self.setting_step and going[K_RCTRL] == 0:
            self.stepX *= 2
            self.stepY *= 2
        
        if going[K_RCTRL] and self.stepX == self.setting_step and self.stepY == self.setting_step and going[K_RSHIFT] == 0:
            self.stepX = int(self.stepX*0.5)
            self.stepY = int(self.stepY*0.5)

        if going[K_RSHIFT] == 0 and going[K_RCTRL] == 0:
            self.stepX = self.setting_step
            self.stepY = self.setting_step



        if going[K_UP] and self.rect.y > 0 and going[K_DOWN] == 0:
            self.rect.y -= self.stepY
            if self.type_animation == None or self.type_animation != "walking_up":
                self.num_body = 0
                self.type_animation = "walking_up"
        if going[K_DOWN] and self.rect.bottom < self.HEIGHT and going[K_UP] == 0: 
            self.rect.y += self.stepY
            if self.type_animation == None or self.type_animation != "walking_down":
                self.num_body = 0
                self.type_animation = "walking_down"
        if going[K_LEFT] and self.rect.x > 0 and going[K_RIGHT] == 0:
            self.rect.x -= self.stepX

            if self.type_animation == None or self.type_animation != "walking_left":
                self.num_body = 0
                self.type_animation = "walking_left"
                self.stutus_flip = True
        if going[K_RIGHT] and self.rect.right < self.WIDTH and going[K_LEFT] == 0:
            self.rect.x += self.stepX

            if self.type_animation == None or self.type_animation != "walking_right":
                self.num_body = 0
                self.type_animation = "walking_right"
                self.stutus_flip = False

        if self.timer != 0:
            self.timer -= 1

        if going[K_UP] == 0 and going[K_RIGHT] == 0 and going[K_LEFT] == 0 and going[K_DOWN] == 0:
            self.body = transform.scale(self.image_list["body"],(self.rect.width,self.rect.height))
            self.type_animation = None
            self.num_body = 0
            if self.stutus_flip == True:

                self.body = transform.flip(self.body,True,False)
        if self.type_animation != None and self.timer == 0:
            self.body = transform.scale(self.image_list[self.type_animation][self.num_body],(self.rect.width,self.rect.height))
            if self.num_body != len(self.image_list[self.type_animation])-1:
                self.num_body += 1
            else:
                self.num_body = 0
            if self.stutus_flip == True:
                self.body = transform.flip(self.body,True,False)
            self.timer = 2
        
        
        self.window.blit(self.body,(self.rect.x,self.rect.y))

def Quit():
    for i in event.get():
        if i.type == QUIT:
            quit()

class angry(sprite.Sprite):
    def __init__(self,x_coor,y_coor,distantion,width,height,image_list,Window,X_or_Y=None,HorizontX=1000,HorizontY=800,step=5):
        super().__init__()
        self.rect = Rect(x_coor,y_coor,width,height)
        self.image_list = image_list
        self.body = transform.scale(self.image_list["body"],(self.rect.width,self.rect.height))
        self.step = step
        self.window = Window
        self.Width = HorizontX
        self.Height = HorizontY
        self.stutus_point = self.going = True
        self.rect_diapozon = Rect(self.rect.x-self.rect.width,self.rect.y-self.rect.height,self.rect.width*3,self.rect.height*3)
        self.stutus_attack = self.stutus_flip = False
        self.distantion1 = self.distantion2 = distantion
        self.X_or_Y = X_or_Y
        if self.X_or_Y == None:
            if random.randint(1,2) == 1:
                self.X_or_Y = True
                print(7)
            else: 
                self.X_or_Y = False
                print(6)

        self.type_animation = None
        self.timer = self.num_body = 0 
        self.stutus_xitbox = -1


    def update(self):
        going = key.get_pressed()
        if going[K_F1]:
            self.stutus_xitbox = True
        if going[K_F2]:
            self.stutus_xitbox = False
        if self.stutus_xitbox == 1:
            draw.rect(self.window,(0,0,0),self.rect_diapozon)
        
        if self.stutus_attack == False:
            if self.X_or_Y == True:
                if self.going == True and self.distantion1 != self.step:
                    self.rect.x += self.step
                    self.distantion1 -= self.step
                    self.type_animation = "walking_right"
                    self.stutus_flip = False

                elif self.going == False and self.distantion1 != self.step:
                    self.rect.x -= self.step
                    self.distantion1 -= self.step
                    self.type_animation = "walking_left"
                    self.stutus_flip = True

                if self.rect.x < 0 and self.going == False:
                    self.going = True
                    self.distantion1 = self.distantion2

                if self.rect.right > self.Width and self.going == True:
                    self.going = False
                    self.distantion1 = self.distantion2


            elif self.X_or_Y == False:
                if self.going == True and self.distantion1 != self.step:
                    self.rect.y += self.step
                    self.distantion1 -= self.step
                    self.type_animation = "walking_down"
                elif self.going == False and self.distantion1 != self.step:
                    self.rect.y -= self.step
                    self.distantion1 -= self.step
                    self.type_animation = "walking_up"
                

                if self.rect.y < 0 and self.going == False:
                    self.going = True
                    self.distantion1 = self.distantion2

                if self.rect.bottom > self.Height and self.going == True:
                    self.going = False
                    self.distantion1 = self.distantion2
            
        if self.distantion1 == self.step:
            if self.going == True:self.going=False
            elif self.going == False:self.going=True
            self.distantion1 = self.distantion2
            self.num_body = 0
        if self.type_animation == None:
            self.body = transform.scale(self.image_list["body"],(self.rect.width,self.rect.height))

        if self.timer != 0:
            self.timer -= 1

        if self.type_animation != None and self.timer == 0:
            self.body = transform.scale(self.image_list[self.type_animation][self.num_body],(self.rect.width,self.rect.height))
            if self.num_body != len(self.image_list[self.type_animation])-1:
                self.num_body += 1
            else:
                self.num_body = 0
            if self.stutus_flip == True:
                self.body = transform.flip(self.body,True,False)
            self.timer = 2

        self.rect_diapozon = Rect(self.rect.x-self.rect.width,self.rect.y-self.rect.height,self.rect.width*3,self.rect.height*3)
        self.window.blit(self.body,(self.rect.x,self.rect.y))

def colli(player,angry_list):
    for i in angry_list:
        going = key.get_pressed()
        if going[K_RCTRL] == 0:
            if i.rect_diapozon.colliderect(player.rect):
                i.stutus_attack = True
            elif i.rect_diapozon.colliderect(player.rect) == 0 and i.stutus_attack == True:
                i.stutus_attack = False
                if i.type_animation == "walking_right" or i.type_animation == "walking_left":
                    i.X_or_Y = True
                elif i.type_animation == "walking_up" or i.type_animation == "walking_down":
                    i.X_or_Y = False
        else:
            if i.rect.colliderect(player.rect):
                i.stutus_attack = True
            elif i.rect.colliderect(player.rect) == 0 and i.stutus_attack == True:
                i.stutus_attack = False
                if i.type_animation == "walking_right" or i.type_animation == "walking_left":
                    i.X_or_Y = True
                elif i.type_animation == "walking_up" or i.type_animation == "walking_down":
                    i.X_or_Y = False
        if i.stutus_attack == True:

            if i.rect.x < player.rect.x:
                i.rect.x += i.step
                i.type_animation = "walking_right"
                i.stutus_flip = False

            if i.rect.x > player.rect.x :
                i.rect.x -= i.step
                i.type_animation = "walking_left"
                i.stutus_flip = True

            if i.rect.y < player.rect.y:
                i.rect.y += i.step
                if i.rect.x == player.rect.x:
                    i.type_animation = "walking_down"

            if i.rect.y > player.rect.y:
                i.rect.y -= i.step
                if i.rect.x == player.rect.x:
                    i.type_animation = "walking_up"
            if going[K_a]:
                print(i.rect.x,player.rect.x)
    


