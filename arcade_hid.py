# Needed to be a bluetooth keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.mouse import Mouse
from adafruit_seesaw import seesaw, rotaryio, digitalio
from adafruit_seesaw.pwmout import PWMOut
import board
import digitalio as board_digitalio
import usb_hid
from arcade_hadware import Knob, PhysicalButton

class ArcadeKeyboard:
    def start(self):
        # Set up the board
        i2c = board.I2C()  # uses board.SCL and board.  SDA

        # set up keyboard and bluethooth

        cc = ConsumerControl(usb_hid.devices)
        k = Keyboard(usb_hid.devices)
        kl = KeyboardLayoutUS(k)
        mouse = Mouse(usb_hid.devices)
        cc = ConsumerControl(usb_hid.devices)

        # private fields
        self.i2c = i2c
        self.k = k
        self.kl = kl
        self.mouse = mouse
        self.cc = cc

    def init_buttons(self):
        def init_button(id, arcade_qt, button_pin, led_pin):
            print("Initializing button...")
            button = digitalio.DigitalIO(arcade_qt, button_pin)
            button.direction = board_digitalio.Direction.INPUT
            button.pull = board_digitalio.Pull.UP

            print("Initializing led...")
            led = digitalio.DigitalIO(arcade_qt, led_pin)

            return PhysicalButton(id, button, led)

        print("Wiring up the buttons")
        arcade_qt_1 = seesaw.Seesaw(self.i2c, addr=0x3A)
        arcade_qt_2 = seesaw.Seesaw(self.i2c, addr=0x3B)

        physical_button_1 = init_button(1, arcade_qt_1, button_pin=2,  led_pin=1)
        physical_button_2 = init_button(2, arcade_qt_1, button_pin=20, led_pin=0)
        physical_button_3 = init_button(3, arcade_qt_1, button_pin=19, led_pin=13)
        physical_button_4 = init_button(4, arcade_qt_1, button_pin=18, led_pin=12)

        physical_button_5 = init_button(5, arcade_qt_2, button_pin=18, led_pin=12)
        physical_button_6 = init_button(6, arcade_qt_2, button_pin=19, led_pin=13)
        physical_button_7 = init_button(7, arcade_qt_2, button_pin=20, led_pin=0)
        physical_button_8 = init_button(8, arcade_qt_2, button_pin=2, led_pin=1)

        return [ physical_button_1,
                 physical_button_2,
                 physical_button_3,
                 physical_button_4,
                 physical_button_5,
                 physical_button_6,
                 physical_button_7,
                 physical_button_8 ]

    def init_encoder(self):
        print("Initializing rotary encoder...")
        i2c = self.i2c

        seesawBoard = seesaw.Seesaw(i2c, addr=0x36)

        seesaw_product = (seesawBoard.get_version() >> 16) & 0xFFFF
        print(f"Found product {seesaw_product}")
        if seesaw_product != 4991:
            print("Wrong firmware loaded?  Expected 4991")

        # Configure seesaw pin used to read knob button presses
        # The internal pull up is enabled to prevent floating input
        seesawBoard.pin_mode(24, seesawBoard.INPUT_PULLUP)
        button = digitalio.DigitalIO(seesawBoard, 24)
        encoder = rotaryio.IncrementalEncoder(seesawBoard)

        return Knob(0, encoder, button)

    def get_keyboard(self):
        return self.k

    def get_consumer_control(self):
        return self.cc
