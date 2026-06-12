#pip install pyautogui
from pyautogui import *
from time import *
sleep(1)

while 1:
    #point coordinates (mouse)
    a=position()
    #point color (RGB)
    b=pixel(a[0],a[1])
    if b==(172, 172, 172):
        press('space')