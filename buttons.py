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

class KeyComboWithCtrlAltShiftButton:
    def __init__(self, name, keyboard, *keycodes):
        self.name = name
        self.keyboard = keyboard
        self.keycodes = keycodes

    def onPress(self):
        print(f"Pressed - {self.name}")
        for keycode in self.keycodes:
            print(f"Pressing Keycode {keycode}")
            self.keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.ALT, keycode)

class KeyComboWithCtrlShiftButton:
    def __init__(self, name, keyboard, *keycodes):
        self.name = name
        self.keyboard = keyboard
        self.keycodes = keycodes

    def onPress(self):
        print(f"Pressed - {self.name}")
        for keycode in self.keycodes:
            print(f"Pressing Keycode {keycode}")
            self.keyboard.send(Keycode.CONTROL, Keycode.SHIFT, keycode)

class MediaButton:
    def __init__(self, name, consumerControl, mediaCommand):
        self.name = name
        self.consumerControl = consumerControl
        self.cmd = mediaCommand

    def onPress(self):
        print(f"Pressed - {self.name}")
        cc = self.consumerControl
        cmd = self.cmd
        cc.send(cmd)

class VolumeButtons:
    def __init__(self, cc):
        self.mute = MediaButton("Volume Mute", cc, ConsumerControlCode.MUTE)
        self.down = MediaButton("Volume Down", cc, ConsumerControlCode.VOLUME_DECREMENT)
        self.up   = MediaButton("Volume Up",   cc, ConsumerControlCode.VOLUME_INCREMENT)

class MonitorButtons:
    def __init__(self, cc):
        self.increase_brightness = MediaButton("Increase Monitor Brightness", cc, ConsumerControlCode.BRIGHTNESS_INCREMENT)  # Increase the monitor brightness
        self.decrease_brightness = MediaButton("Decrease Monitor Brightness", cc, ConsumerControlCode.BRIGHTNESS_DECREMENT)  # Decrease the monitor brightness

class MediaButtons:
    def __init__(self, cc):
        self.eject        = MediaButton("Eject", cc, ConsumerControlCode.EJECT)                       # No impact when using Spotify
        self.fast_forward = MediaButton("Fast Forward", cc, ConsumerControlCode.FAST_FORWARD)         # Jump ahead 5 seconds
        self.play         = MediaButton("Play", cc, ConsumerControlCode.PLAY_PAUSE)                   # Play or Pause
        self.record       = MediaButton("Record", cc, ConsumerControlCode.RECORD)                     # No impact when using Spotify
        self.rewind       = MediaButton("Rewind", cc, ConsumerControlCode.REWIND)                     # No impact when using Spotify
        self.next         = MediaButton("Next", cc, ConsumerControlCode.SCAN_NEXT_TRACK)              # Skip to Next Track
        self.previous     = MediaButton("Previous", cc, ConsumerControlCode.SCAN_PREVIOUS_TRACK)      # Go to previous track
        self.stop         = MediaButton("Stop", cc, ConsumerControlCode.STOP)                         # Stop. Unlike Pause, this will not start playing again if pressed a second time

class ZoomButtons:
    def __init__(self, k):
        self.raise_hand       = KeyComboWithCtrlAltShiftButton("Zoom: raise/lower hand", k, Keycode.F8)
        self.copy_invite_link = KeyComboWithCtrlAltShiftButton("Zoom: Copy Invite Link", k, Keycode.F4)
        self.toggle_video     = KeyComboWithCtrlAltShiftButton("Zoom: Toggle Video",     k, Keycode.F1)
        self.toggle_audio     = KeyComboWithCtrlAltShiftButton("Zoom: Toggle Audio",     k, Keycode.F6)
        self.pause_share      = KeyComboWithCtrlAltShiftButton("Zoom: Pause Share",      k, Keycode.F7)
        self.start_share      = KeyComboWithCtrlAltShiftButton("Zoom: Share",            k, Keycode.F2)

class OBS_Buttons:
    def __init__(self, k):
        self.transition              = KeyComboWithCtrlAltShiftButton("OBS: Transition",               k, Keycode.F10)
        self.screen_shot             = KeyComboWithCtrlAltShiftButton("OBS: Screen Shot Output",       k, Keycode.F9)
        self.toggle_virtual_camera   = KeyComboWithCtrlAltShiftButton("OBS: Toggle Virtual Camera",    k, Keycode.F12)
        self.switch_to_default_scene = KeyComboWithCtrlAltShiftButton("OBS: Switch to Default Scene",  k, Keycode.F11, Keycode.F10)

class WebStormButtons:
    def __init__(self, k):
        self.run       = KeyComboWithCtrlShiftButton("Run",  k, Keycode.R)
        self.debug     = KeyComboWithCtrlShiftButton("Debug",k, Keycode.D)
