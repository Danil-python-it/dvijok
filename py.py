from pygame import *
import setting

Width = 1000
Height = 800

window = display.set_mode((Width,Height))
display.set_caption("iluzor")
clock = time.Clock()
FPS = 60
Game = True
all_angry = list()

SMERT = {
    "body":image.load("png/walking3.1.png"),
    "walking_right":[image.load("png/смерть/в право/walking4.1.png"),image.load("png/смерть/в право/walking4.2.png"),image.load("png/смерть/в право/walking4.3.png"),image.load("png/смерть/в право/walking4.4.png")],
    "walking_left":[image.load("png/смерть/в право/walking4.1.png"),image.load("png/смерть/в право/walking4.2.png"),image.load("png/смерть/в право/walking4.3.png"),image.load("png/смерть/в право/walking4.4.png")],
    "walking_up":[image.load("png/смерть/в вверх/walking2.1.png"),image.load("png/смерть/в вверх/walking2.2.png"),image.load("png/смерть/в вверх/walking2.3.png"),image.load("png/смерть/в вверх/walking2.4.png")],
    "walking_down":[image.load("png/смерть/в низ/walking3.1.png"),image.load("png/смерть/в низ/walking3.2.png"),image.load("png/смерть/в низ/walking3.3.png"),image.load("png/смерть/в низ/walking3.4.png")],
}
smert = setting.PLAYER(200,200,100,100,SMERT,window,Width,Height)
angry = setting.angry(500,100,400,100,100,SMERT,window)
angry2 = setting.angry(100,100,400,100,100,SMERT,window)
all_angry.append(angry)
all_angry.append(angry2)



while Game:
    setting.Quit()

    window.fill((255,255,255))
    smert.update()
    setting.colli(smert,all_angry)
    for i in all_angry:
        i.update()
    display.update()
    clock.tick(FPS)