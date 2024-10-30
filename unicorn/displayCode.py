from unicornhatmini import UnicornHATMini
from .letters import a47
from .letters import b47
from .letters import c47
from .letters import d47
from .letters import e47
from .letters import f47
from .letters import g47
from .letters import h47
from .letters import i47
from .letters import j47
from .letters import k47
from .letters import l47
from .letters import m47
from .letters import n47
from .letters import o47
from .letters import p47
from .letters import q47
from .letters import r47
from .letters import s47
from .letters import t47
from .letters import u47
from .letters import v47
from .letters import w47
from .letters import x47
from .letters import y47
from .letters import z47
from .letters import clearLetters
from .icons import plane
import time

uh = UnicornHATMini()

uh.set_brightness(0.3)

def displayCode(str, x):
        i = 0
        for char in str:
                displayLetter(char,i,x)
                i = i+1
        time.sleep(0.5)
        clearLetters()

def displayLetter(char,i,x):
        if char == 'A':
                a47(x+5*i,0,[255,0,0])
        elif char == 'B':
                b47(x+5*i,0,[255,0,0])
        elif char == 'C':
                c47(x+5*i,0,[255,0,0])
        elif char == 'D':
                d47(x+5*i,0,[255,0,0])
        elif char == 'E':
                e47(x+5*i,0,[255,0,0])
        elif char == 'F':
                f47(x+5*i,0,[255,0,0])
        elif char == 'G':
                g47(x+5*i,0,[255,0,0])
        elif char == 'H':
                h47(x+5*i,0,[255,0,0])
        elif char == 'I':
                i47(x+5*i,0,[255,0,0])
        elif char == 'J':
                j47(x+5*i,0,[255,0,0])
        elif char == 'K':
                k47(x+5*i,0,[255,0,0])
        elif char == 'L':
                l47(x+5*i,0,[255,0,0])
        elif char == 'M':
                m47(x+5*i,0,[255,0,0])
        elif char == 'N':
                n47(x+5*i,0,[255,0,0])
        elif char == 'O':
                o47(x+5*i,0,[255,0,0])
        elif char == 'P':
                p47(x+5*i,0,[255,0,0])
        elif char == 'Q':
                q47(x+5*i,0,[255,0,0])
        elif char == 'R':
                r47(x+5*i,0,[255,0,0])
        elif char == 'S':
                s47(x+5*i,0,[255,0,0])
        elif char == 'T':
                t47(x+5*i,0,[255,0,0])
        elif char == 'U':
                u47(x+5*i,0,[255,0,0])
        elif char == 'V':
                v47(x+5*i,0,[255,0,0])
        elif char == 'W':
                w47(x+5*i,0,[255,0,0])
        elif char == 'X':
                x47(x+5*i,0,[255,0,0])
        elif char == 'Y':
                y47(x+5*i,0,[255,0,0])
        elif char == 'Z':
                z47(x+5*i,0,[255,0,0])
        else:
                a47(x+5*i,0,[255,0,0])

def displayIcon(icon):
        if icon == 'plane':
                plane(0,0,[255,0,0])
