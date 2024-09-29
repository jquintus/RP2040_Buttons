import time

# needed for keycodes
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

# my imports
from arcade_hid import ArcadeKeyboard
from buttons import LambdaButton, EmptyButton, KeyComboButton, VolumeButton

print("Hello, CircuitPython!")

keyboard = ArcadeKeyboard()
keyboard.start()

cc = keyboard.get_consumer_control()
k = keyboard.get_keyboard()

# zoom = ZoomButtons("zoom", k)
# volume = VolumeButtons("volume", cc)

encoder = keyboard.init_encoder()
buttons = keyboard.init_buttons()

encoder.set_on_press(EmptyButton("Button 0"))
encoder.set_on_turn(EmptyButton("Up"), EmptyButton("Down"))

buttons[0].set_on_press(EmptyButton("Button 1"))
buttons[1].set_on_press(EmptyButton("Button 2"))
buttons[2].set_on_press(EmptyButton("Button 3"))
buttons[3].set_on_press(EmptyButton("Button 4"))
buttons[4].set_on_press(EmptyButton("Button 5"))
buttons[5].set_on_press(EmptyButton("Button 6"))
buttons[6].set_on_press(EmptyButton("Button 7"))
buttons[7].set_on_press(EmptyButton("Button 8"))

print ("Player one, fight!")
while True:
    for button in buttons:
        button.sync()
    encoder.sync()
