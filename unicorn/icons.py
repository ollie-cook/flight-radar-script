from unicornhatmini import UnicornHATMini
import time

uh = UnicornHATMini()

def clearLetters():
        uh.clear()

def plane(x,y,rgb,t=0):
        for j in range(4):
                uh.set_pixel(x % 17, y+j, rgb[0], rgb[1], rgb[2])

        for i in range(2):
                for j in range(6):
                        uh.set_pixel((x+(3*i)) % 17, y+j+1, rgb[0], rgb[1], rgb[2])
        uh.show()

        if t > 0:
                time.sleep(t)
                uh.clear()