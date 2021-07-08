from digitalio import DigitalInOut,Direction,Pull
import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
kbd = Keyboard(usb_hid.devices)

buttonC = DigitalInOut(board.GP16)
buttonC.direction = Direction.INPUT
buttonC.pull = Pull.DOWN

buttonV = DigitalInOut(board.GP17)
buttonV.direction = Direction.INPUT
buttonV.pull = Pull.DOWN

buttonctrl = DigitalInOut(board.GP18)
buttonctrl.direction = Direction.INPUT
buttonctrl.pull = Pull.DOWN

while True:
    if buttonC.value:
        kbd.press(Keycode.C)
    else:
        kbd.release(Keycode.C)

    if buttonV.value:
        kbd.press(Keycode.V)
    else:
        kbd.release(Keycode.V)
        
    if buttonctrl.value:
        kbd.press(Keycode.CONTROL)
    else:
        kbd.release(Keycode.CONTROL)
        

