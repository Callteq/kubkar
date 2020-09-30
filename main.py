def on_button_pressed_a():
    global Place, Lane1, Lane2, Lane3, Lane4
    Place = 0
    Lane1 = 0
    Lane2 = 0
    Lane3 = 0
    Lane4 = 0
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SMALL_DIAMOND)
input.on_button_pressed(Button.A, on_button_pressed_a)

Lane4 = 0
Lane3 = 0
Lane2 = 0
Lane1 = 0
Place = 0
basic.show_icon(IconNames.NO)
pins.set_pull(DigitalPin.P0, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P8, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P2, PinPullMode.PULL_NONE)

def on_forever():
    global Place, Lane1
    if pins.digital_read_pin(DigitalPin.P1) == 0:
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
basic.forever(on_forever)

def on_forever2():
    global Place, Lane2
    if pins.digital_read_pin(DigitalPin.P2) == 0:
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
basic.forever(on_forever2)

def on_forever3():
    global Place
    if Place == 2:
        images.create_big_image("""
            # . # . # . # . # .
            . # . # . # . # . #
            # . # . # . # . # .
            . # . # . # . # . #
            # . # . # . # . # .
            """).scroll_image(1, 50)
        control.wait_micros(100)
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
