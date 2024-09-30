from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

class LambdaButton:
    def __init__(self, name, func):
        self.name = name
        self.onPressFunc = func

    def onPress(self):
        print(f"Pressed - {self.name}")
        self.onPressFunc()

class EmptyButton:
    def __init__(self, name):
        self.name = name

    def onPress(self):
        print(f"Pressed - {self.name}")
        print("nothing to do")

class KeyComboButton:
    def __init__(self, name, keyboard, *keycodes):
        self.name = name
        self.keyboard = keyboard
        self.keycodes = keycodes

    def onPress(self):
        print(f"Pressed - {self.name}")
        for keycode in self.keycodes:
            print(f"Pressing Keycode {keycode}")
            self.keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, keycode)

class VolumeButton:
    def __init__(self, name, consumerControl, volumeCommand):
        self.name = name
        self.consumerControl = consumerControl
        self.cmd = volumeCommand

    def onPress(self):
        print(f"Pressed - {self.name}")
        cc = self.consumerControl
        cmd = self.cmd
        cc.send(cmd)

class VolumeButtons:
    def __init__(self, cc):
        self.mute = VolumeButton("Volume Mute", cc, ConsumerControlCode.MUTE)
        self.down = VolumeButton("Volume Down", cc, ConsumerControlCode.VOLUME_DECREMENT)
        self.up   = VolumeButton("Volume Up",   cc, ConsumerControlCode.VOLUME_INCREMENT)

class ZoomButtons:
    def __init__(self, k):
        self.raise_hand       = KeyComboButton("Zoom: raise/lower hand", k, Keycode.F8)
        self.copy_invite_link = KeyComboButton("Zoom: Copy Invite Link", k, Keycode.F4)
        self.toggle_video     = KeyComboButton("Zoom: Toggle Video",     k, Keycode.F1)
        self.toggle_audio     = KeyComboButton("Zoom: Toggle Audio",     k, Keycode.F6)
        self.pause_share      = KeyComboButton("Zoom: Pause Share",      k, Keycode.F7)
        self.start_share      = KeyComboButton("Zoom: Share",            k, Keycode.F2)

class OBS_Buttons:
    def __init__(self, k):
        self.transition              = KeyComboButton("OBS: Transition",               k, Keycode.F10)
        self.screen_shot             = KeyComboButton("OBS: Screen Shot Output",       k, Keycode.F9)
        self.toggle_virtual_camera   = KeyComboButton("OBS: Toggle Virtual Camera",    k, Keycode.F12)
        self.switch_to_default_scene = KeyComboButton("OBS: Switch to Default Scene",  k, Keycode.F11, Keycode.F10)
