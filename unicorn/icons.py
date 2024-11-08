from unicornhatmini import UnicornHATMini
import time

uh = UnicornHATMini()

def clearLetters():
        uh.clear()

def plane(x,y,rgb,t=0):
        for j in range(5):
                uh.set_pixel(x % 17, y+1+j, rgb[0], rgb[1], rgb[2])

        for j in range(3):
                for i in range(10):
                        uh.set_pixel((x+1+i) % 17, y+2+j, rgb[0], rgb[1], rgb[2])

        for i in range(2):
                for j in range(2):
                        uh.set_pixel()

        uh.show()

        if t > 0:
                time.sleep(t)
                uh.clear()