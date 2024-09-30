import time

# needed for keycodes
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

# my imports
from arcade_hid import ArcadeKeyboard
from buttons import EmptyButton, VolumeButtons, ZoomButtons

print("Hello, CircuitPython!")

keyboard = ArcadeKeyboard()
keyboard.start()

cc = keyboard.get_consumer_control()
k = keyboard.get_keyboard()

zoom = ZoomButtons(k)
volume = VolumeButtons(cc)

encoder = keyboard.init_encoder()
buttons = keyboard.init_buttons()

encoder.set_on_press(volume.mute)
encoder.set_on_turn(volume.up, volume.down)

buttons[0].set_on_press(zoom.toggle_video)        # Top     Red
buttons[1].set_on_press(zoom.start_share)         # Top     Yellow
buttons[2].set_on_press(zoom.copy_invite_link)    # Top     Green
buttons[3].set_on_press(EmptyButton("Button 4"))  # Top     Blue

buttons[4].set_on_press(zoom.toggle_audio)        # Bottom  Red
buttons[5].set_on_press(zoom.pause_share)         # Bottom  Yellow
buttons[6].set_on_press(zoom.raise_hand)          # Bottom  Green
buttons[7].set_on_press(EmptyButton("Button 8"))  # Bottom  Blue

# Flash the lights on startup
for idx in [0, 1, 2, 3, 7, 6, 5, 4]:
    buttons[idx].led.value = True
    time.sleep(0.1)

time.sleep(0.2)

for idx in [0, 1, 2, 3, 7, 6, 5, 4]:
    buttons[idx].led.value = False
    time.sleep(0.1)

print ("Player one, fight!")
while True:
    for button in buttons:
        button.sync()
    encoder.sync()
