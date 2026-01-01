def mood_for_bot():
    radio.raise_event(EventBusSource.MICROBIT_ID_ACCELEROMETER,
        EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE)

def on_button_pressed_a():
    basic.show_string("Good.")
    basic.show_string("How about you?")
    mood_for_bot()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_microbit_id_accelerometer_evt_data_update():
    global mood
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

def on_button_pressed_b():
    basic.show_string("Not good.")
    basic.show_string("How about you?")
    mood_for_bot()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    control.reset()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

mood = False
radio.set_group(Math.round(255 / 2))