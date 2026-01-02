"""I am simulating having a conversation. The topic is how you feel.
"""

# When button A is pressed, you replied good.

def on_button_pressed_a():
    basic.show_string("Good.")
    basic.show_string("How about you?")
    mood_for_bot()
input.on_button_pressed(Button.A, on_button_pressed_a)

def mood_for_bot():
    radio.raise_event(EventBusSource.MICROBIT_ID_ACCELEROMETER,
        EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE)

def on_pin_pressed_p2():
    control.reset()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)


def on_microbit_id_accelerometer_evt_data_update():
    global mood
    # I don't know how robot feels, so I made a condition and it's random.
    mood = Math.random_boolean()
    if mood == True:
        basic.show_string("Good.")
    else:
        basic.show_string("Not good.")
control.on_event(EventBusSource.MICROBIT_ID_ACCELEROMETER,
    EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE,
    on_microbit_id_accelerometer_evt_data_update)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

# When button B is pressed, you replied not good.

def on_button_pressed_b():
    basic.show_string("Not good.")
    basic.show_string("How about you?")
    mood_for_bot()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    radio.send_string("How are you?")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

mood = False
led.set_brightness(Math.round(255 / 2))
radio.set_group(255)