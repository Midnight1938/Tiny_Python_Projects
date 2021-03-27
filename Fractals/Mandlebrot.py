from PIL import Image
import time
import pygame
import keyboard
from time import sleep


start_time = time.time()


pygame.init()


# 1000*500 = 500 000

xS = 1000  # x-size
yS = 500  # y-size

img = Image.new("RGB", (xS, yS), "White")
win = pygame.display.set_mode((xS, yS))

myfont = pygame.font.SysFont('Comic Sans MS', 14)

zoom = 0.005
camX = 0
camY = 0


def generator():
    vList = []  # list of values

    for i in range(0, xS):
        for j in range(0, yS):
            val = complex(((i-(xS/2)-camX)*zoom), ((j-(yS/2)-camY)*zoom))
            global iter2
            iter2 = 40
            if zoom < 0.0003125:
                iter2 = 40 + 0.0003125/zoom
            z = 0
            d = 0
            n = 0  # number of iterations before escape
            for k in range(0, int(iter2)):
                d = complex(z**2) + val**1.4
                z = d
                if z.real > 2 or z.real < -2:
                    break
                n += 1
            color = (255*n)/iter2
            img.putpixel((i, j), (0, int(color), int(color)))
            # if color <= 128:
            # img.putpixel((i,j),(0,128,128))
            # else:
            # img.putpixel((i,j),(0,int(color),int(color)))
    print(zoom)
    print(camX, camY)


# print(vList[0])
generator()

while True:
    img.save("MandBrot.png")
    bg = pygame.image.load("MandBrot.png")
    win.blit(bg, (0, 0))
    try:
        if keyboard.is_pressed("up"):
            sleep(0.1)
            zoom = zoom/2
            camX = camX*2
            camY = camY*2
            print("PRESSED")
            generator()
            print("DONE")
        else:
            pass
    except:
        pass
    try:
        if keyboard.is_pressed("down"):
            sleep(0.1)
            zoom = zoom*2
            camX = camX/2
            camY = camY/2
            print("PRESSED")
            generator()
            print("DONE")
        else:
            pass
    except:
        pass
    try:
        if keyboard.is_pressed("a"):
            sleep(0.1)
            camX += 200  # *(0.005/zoom)
            print("PRESSED")
            generator()
            print("DONE")
        else:
            pass
    except:
        pass
    try:
        if keyboard.is_pressed("d"):
            sleep(0.1)
            camX -= 200  # *(0.005/zoom)
            print("PRESSED")
            generator()
            print("DONE")
        else:
            pass
    except:
        pass
    try:
        if keyboard.is_pressed("w"):
            sleep(0.1)
            camY += 200  # *(0.005/zoom)
            print("PRESSED")
            generator()
            print("DONE")
        else:
            pass
    except:
        pass
    try:
        if keyboard.is_pressed("s"):
            sleep(0.1)
            camY -= 200  # *(0.005/zoom)
            print("PRESSED")
            generator()
            print("DONE")
        else:
            pass
    except:
        pass
    textFoc = myfont.render('Iterations: '+str(iter2), False, (255, 255, 255))
    win.blit(textFoc, (0, 1*14))
    pygame.event.get()
    pygame.display.update()  # Updates visualisator
    win.fill((0, 0, 0))


print("--- %s seconds ---" % (time.time() - start_time))
input()
