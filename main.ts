// When button A is pressed, you replied good.
input.onButtonPressed(Button.A, function () {
    basic.showString("Good.")
    basic.showString("How about you?")
    mood_for_bot()
})
function mood_for_bot () {
    radio.raiseEvent(
    EventBusSource.MICROBIT_ID_ACCELEROMETER,
    EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE
    )
}
input.onPinPressed(TouchPin.P2, function () {
    control.reset()
})
/**
 * I am simulating having a conversation. The topic is how you feel.
 */
control.onEvent(EventBusSource.MICROBIT_ID_ACCELEROMETER, EventBusValue.MICROBIT_ACCELEROMETER_EVT_DATA_UPDATE, function () {
    // I don't know how robot feels, so I made a condition and it's random.
    mood = Math.randomBoolean()
    if (mood == true) {
        basic.showString("Good.")
    } else {
        basic.showString("Not good.")
    }
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
// When button B is pressed, you replied not good.
input.onButtonPressed(Button.B, function () {
    basic.showString("Not good.")
    basic.showString("How about you?")
    mood_for_bot()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendString("How are you?")
})
let mood = false
led.setBrightness(Math.round(255 / 2))
radio.setGroup(255)
