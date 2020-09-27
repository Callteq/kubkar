Place = 0
Lane1 = 0
Lane2 = 0
Lane3 = 0
Lane4 = 0
Finished = 0

def on_gesture_shake():
    global Place, Lane1, Lane2, Lane3, Lane4, Finished
    Place = 0
    Lane1 = 0
    Lane2 = 0
    Lane3 = 0
    Lane4 = 0
    basic.show_icon(IconNames.HEART)
    Finished = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global Place, Lane2
    if pins.digital_read_pin(DigitalPin.P1) == 1:
        if Lane2 == 0:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . # . . .
                """)
            Place += 1
            Lane2 = Place
basic.forever(on_forever)

def on_forever2():
    global Place, Lane1
    if pins.digital_read_pin(DigitalPin.P0) == 1:
        if Lane1 == 0:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                """)
            Place += 1
            Lane1 = Place
basic.forever(on_forever2)

def on_forever3():
    global Place
    if Place == 2:
        basic.show_icon(IconNames.CHESSBOARD)
        control.wait_micros(10000)
        basic.show_leds("""
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        led.plot(0, Lane1)
        led.plot(1, Lane2)
        Place += 1
basic.forever(on_forever3)
