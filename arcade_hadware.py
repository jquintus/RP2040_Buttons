class PhysicalButton:
    def __init__(self, id, button, led):
        self.id = id
        self.button = button
        self.led = led
        self.button_held = False

    def set_on_press(self, action):
        self.action = action

    def sync(self):
        button_value = self.button.value
        button_held = self.button_held
        if not button_value and not button_held:
            self.button_held = True
            self.led.value = True

            self.action.onPress()
            print (f'Pressed - Button {self.id}')

        if button_value and button_held:
            self.button_held = False
            self.led.value = False
            print (f'Released - Button {self.id}')

class MockLED:
    def __init__(self):
        value = False

class RotaryEncoder:
    def __init__(self, encoder):
        self.encoder = encoder
        self.last_position = encoder.position

    def set_on_turn(self, up, down):
        self.up = up
        self.down = down

    def sync(self):
        position = self.encoder.position
        position_delta = self.last_position - position

        if(position_delta < 0):
            self.last_position = position
            self.up.onPress()
            print(f'up      {self.last_position} - {position_delta}')
        elif(position_delta > 0):
            self.last_position = position
            self.down.onPress()
            print(f'down    {self.last_position} - {position_delta}')

class Knob:
    def __init__(self, id, encoder, button):
        self.encoder = RotaryEncoder(encoder)
        self.button = PhysicalButton(id, button, MockLED())

    def set_on_press(self, action):
        self.button.set_on_press(action)

    def set_on_turn(self, up, down):
        self.encoder.set_on_turn(up, down)

    def sync(self):
        self.button.sync()
        self.encoder.sync()
