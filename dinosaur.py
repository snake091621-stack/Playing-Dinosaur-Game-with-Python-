from pyautogui import *
from time import *

sleep(1)

while 1:
    a=position()
    b=pixel(a[0],a[1])
    
    if b==(172, 172, 172):
        press('space')
