from unicornhatmini import UnicornHATMini
import time

uh = UnicornHATMini()

def clearLetters():
        uh.clear()

def a57(x,y):
        for i in range(3):
                for j in range(2):
                        uh.set_pixel(x+i+1, y+(4*j), 255, 0, 0)

        for i in range(2):
                for j in range(6):
                        uh.set_pixel(x+(4*i), y+j+1, 255, 0, 0)


        uh.show()
        time.sleep(5)

def a47(x,y,rgb,t=0):
        for i in range(2):
                for j in range(2):
                        uh.set_pixel((x+i+1) % 17, y+(2*j), rgb[0], rgb[1], rgb[2])

        for i in range(2):
                for j in range(6):
                        uh.set_pixel((x+(3*i)) % 17, y+j+1, rgb[0], rgb[1], rgb[2])
        uh.show()

        if t > 0:
                time.sleep(t)
                uh.clear()

def b47(x,y,rgb,t=0):
        for j in range(7):
                uh.set_pixel(x % 17, y+j, rgb[0], rgb[1], rgb[2])

        for i in range(2):
                for j in [0,2,6]:
                        uh.set_pixel((x+i+1) % 17, y+j, rgb[0], rgb[1], rgb[2])

        for j in [1,3,4,5]:
                uh.set_pixel((x+3) % 17,y+j, rgb[0], rgb[1], rgb[2])

        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def c47(x,y,rgb,t=0):
        for j in range(5):
                uh.set_pixel(x % 17, y+j+1, rgb[0], rgb[1], rgb[2])

        for i in range(3):
                for j in range(2):
                        uh.set_pixel((x+i+1) % 17, y+6*j, rgb[0], rgb[1], rgb[2])
                        if i==0:
                                uh.set_pixel((x+3) % 17, y+1+j*4, rgb[0], rgb[1], rgb[2])
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def d47(x,y,rgb,t=0):
        for i in range(3):
                for j in range(2):
                        uh.set_pixel((x+i) % 17,y+j*6,rgb[0],rgb[1],rgb[2])
        for i in range(2):
                for j in range(5):
                        uh.set_pixel((x+i*3) % 17, y+j+1,rgb[0],rgb[1],rgb[2])
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def e47(x,y,rgb,t=0):
        for i in range(4):
                for j in range(2):
                        uh.set_pixel((x+i) % 17,y+j*6,rgb[0],rgb[1],rgb[2])
        
        for i in range(3):
                uh.set_pixel((x+i)%17,y+3,rgb[0],rgb[1],rgb[2])
        
        for j in range(7):
                uh.set_pixel((x) % 17, y+j+1,rgb[0],rgb[1],rgb[2])
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def f47(x,y,rgb,t=0):
        for i in range(4):
                uh.set_pixel((x+i) % 17,y*6,rgb[0],rgb[1],rgb[2])
        
        for i in range(3):
                uh.set_pixel((x+i)%17,y+1*3,rgb[0],rgb[1],rgb[2])
        
        for j in range(6):
                uh.set_pixel((x) % 17, y+j+1,rgb[0],rgb[1],rgb[2])
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def g47(x,y,rgb,t=0):
        for i in range(2):
                for j in range(5):
                        if i!=1 or j!=1:
                                uh.set_pixel((x+3*i) % 17, y+j+1, rgb[0], rgb[1], rgb[2])

        uh.set_pixel(x+2, y+3, rgb[0], rgb[1], rgb[2])

        for i in range(2):
                for j in range(2):
                        uh.set_pixel((x+i+1) % 17, y+6*j, rgb[0], rgb[1], rgb[2])
                        if i==0:
                                uh.set_pixel((x+3) % 17, y+1+j*4, rgb[0], rgb[1], rgb[2])

        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def h47(x,y,rgb,t=0):
        for i in range(3):
                uh.set_pixel((x+i)%17,y+3,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(7):
                        uh.set_pixel((x+i*3) % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def i47(x,y,rgb,t=0):
        for i in range(3):
                for j in range(2):
                        uh.set_pixel((x+i) % 17,y+j*6,rgb[0],rgb[1],rgb[2])
         
        for j in range(5):
                uh.set_pixel((x+1) % 17, y+j+1,rgb[0],rgb[1],rgb[2])
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def j47(x,y,rgb,t=0):
        uh.set_pixel(x % 17,y+5,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                uh.set_pixel((x+i+1)%17,y+6,rgb[0],rgb[1],rgb[2])
        
        for j in range(6):
                uh.set_pixel((x+3) % 17, y+j,rgb[0],rgb[1],rgb[2])
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()
def k47(x,y,rgb,t=0):
        for j in range(7):
                uh.set_pixel(x % 17, y+j, rgb[0], rgb[1], rgb[2])

        uh.set_pixel((x+1)%17, y+3, rgb[0], rgb[1], rgb[2])

        for j in range(5):
                if j != 2:
                        uh.set_pixel((x+2) % 17, y+j+1, rgb[0], rgb[1], rgb[2])
        
        for j in range(2):
                uh.set_pixel((x+3) % 17, y+j*6, rgb[0], rgb[1], rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def l47(x,y,rgb,t=0):
        for i in range(4):
                uh.set_pixel((x+i) % 17,y+6,rgb[0],rgb[1],rgb[2])
        
        for j in range(7):
                uh.set_pixel((x) % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def m47(x,y,rgb,t=0):
        for i in range(2):
                uh.set_pixel((x+i+1)%17,y+1,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(7):
                        uh.set_pixel((x+i*3) % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def n47(x,y,rgb,t=0):
        for i in range(2):
                uh.set_pixel((x+i+1)%17,y+i+2,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(7):
                        uh.set_pixel((x+i*3) % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def o47(x,y,rgb,t=0):
        for i in range(2):
                for j in range(2):
                        uh.set_pixel((x+i+1)%17,y+j*6,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(5):
                        uh.set_pixel((x+i*3) % 17, y+j+1,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def p47(x,y,rgb,t=0):
        for i in range(2):
                for j in range(2):
                        uh.set_pixel((x+i+1)%17,y+j*3,rgb[0],rgb[1],rgb[2])
        
        for j in range(7):
                uh.set_pixel(x % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        for j in range(2):
                uh.set_pixel((x+3) % 17, y+j+1,rgb[0],rgb[1],rgb[2])


        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def q47(x,y,rgb,t=0):
        for i in range(2):
                for j in range(2):
                        uh.set_pixel((x+i+1)%17,y+j*6,rgb[0],rgb[1],rgb[2])

        uh.set_pixel((x+3)%17,y+6,rgb[0],rgb[1],rgb[2])

        uh.set_pixel((x+2)%17,y+5,rgb[0],rgb[1],rgb[2])

        for j in range(5):
                uh.set_pixel(x % 17, y+j+1,rgb[0],rgb[1],rgb[2])
        
        for j in range(4):
                uh.set_pixel((x+3) % 17, y+j+1,rgb[0],rgb[1],rgb[2])


        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def r47(x,y,rgb,t=0):
        for i in range(2):
                for j in range(2):
                        uh.set_pixel((x+i+1) % 17, y+(j*3), rgb[0], rgb[1], rgb[2])

        for i in range(2):
                for j in range(6):
                        if i != 1 or j != 2:
                                uh.set_pixel((x+(3*i)) % 17, y+j+1, rgb[0], rgb[1], rgb[2])
        uh.show()

        if t > 0:
                time.sleep(t)
                uh.clear()

def s47(x,y,rgb,t=0):
        for i in range(2):
                for j in range(3):
                        uh.set_pixel((x+i+1)%17,y+j*3,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(2):
                        uh.set_pixel((x+i*3) % 17, y+1+(j*4),rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                uh.set_pixel((x+i*3) % 17, y+2+(i*2), rgb[0], rgb[1], rgb[2])

        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def t47(x,y,rgb,t=0):
        for i in range(3):
                uh.set_pixel((x+i) % 17,y,rgb[0],rgb[1],rgb[2])
         
        for j in range(6):
                uh.set_pixel((x+1) % 17, y+j+1,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def u47(x,y,rgb,t=0):
        for i in range(2):
                uh.set_pixel((x+i+1)%17,y+6,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(6):
                        uh.set_pixel((x+i*3) % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def v47(x,y,rgb,t=0):
        for i in range(2):
                uh.set_pixel((x+i+1)%17,y+6-i,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(6):
                        if i != 1 or j != 5:
                                uh.set_pixel((x+i*3) % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def w47(x,y,rgb,t=0):
        for i in range(2):
                uh.set_pixel((x+i+1)%17,y+5,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(7):
                        uh.set_pixel((x+i*3) % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def x47(x,y,rgb,t=0):
        for i in range(2):
                uh.set_pixel((x+i+1)%17,y+3,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(7):
                        if j != 3:
                                uh.set_pixel((x+i*3) % 17, y+j,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def y47(x,y,rgb,t=0):
        for i in range(2):
                uh.set_pixel((x+i+1)%17,y+3,rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(3):
                        uh.set_pixel((x+i*3) % 17, y+j,rgb[0],rgb[1],rgb[2])

        for j in range(3):
                uh.set_pixel((x+1) % 17, y+j+4,rgb[0],rgb[1],rgb[2])
        
        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()

def z47(x,y,rgb,t=0):
        for i in range(4):
                for j in range(2):
                        uh.set_pixel((x+i) % 17,y+j*6,rgb[0],rgb[1],rgb[2])
         
        for i in range(2):
                uh.set_pixel((x+i*3) % 17, y+5-(i*4),rgb[0],rgb[1],rgb[2])
        
        for i in range(2):
                for j in range(2):
                        uh.set_pixel((x+1+i) % 17, y+3-i+j, rgb[0], rgb[1], rgb[2])

        uh.show()

        if t>0:
                time.sleep(t)
                uh.clear()


