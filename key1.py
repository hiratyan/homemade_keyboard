import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

button = DigitalInOut(board.GP16)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

kbd = Keyboard(usb_hid.devices)

firstpress = 0
lastpress = 0

while True:
    if button.value:
        if time.monotonic() - lastpress > 0.8:
            kbd.send(Keycode.C)
            lastpress = time.monotonic()
            if firstpress == 0:
                firstpress = time.monotonic()
        if firstpress !=0 and time.monotonic() - firstpress > 0.8:
            if time.monotonic() - lastpress > 0.03:
                kbd.send(Keycode.C)
                lastpress = time.monotonic()
    else:
        lastpress = 0
        firstpress = 0
    time.sleep(0.001)
    
