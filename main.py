def LedDisplay(Lane: number, Position: number):
    global LedPos, range2
    if Position == 1:
        LedPos = (Lane - 1) * 4
        range2 = strip.range(LedPos, 4)
        for index in range(20):
            range2.show_color(neopixel.colors(NeoPixelColors.BLUE))
            control.wait_micros(100)
            range2.show_color(neopixel.colors(NeoPixelColors.WHITE))
            control.wait_micros(100)
            range2.show_color(neopixel.colors(NeoPixelColors.BLUE))
    else:
        LedPos = (Lane - 1) * 4 + Position
        range2 = strip.range(LedPos, 1)
        if Position == 2:
            range2.show_color(neopixel.colors(NeoPixelColors.RED))
        elif Position == 3:
            range2.show_color(neopixel.colors(NeoPixelColors.GREEN))
        else:
            range2.show_color(neopixel.colors(NeoPixelColors.WHITE))
    range2.show()

def on_button_pressed_ab():
    global Place, Lane1, Lane2, Lane3, Lane4
    Place = 99
    Lane1 = 0
    Lane2 = 0
    Lane3 = 0
    Lane4 = 0
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    Place = 0
    basic.show_icon(IconNames.SMALL_DIAMOND)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

Lane4 = 0
Lane3 = 0
Lane2 = 0
Lane1 = 0
Place = 0
range2: neopixel.Strip = None
LedPos = 0
strip: neopixel.Strip = None
basic.show_icon(IconNames.NO)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P8, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P2, PinPullMode.PULL_NONE)
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_NONE)
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
strip.show()

def on_forever():
    global Place, Lane2, Lane3, Lane4
    if input.button_is_pressed(Button.B):
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
            LedDisplay(2, Lane2)
            Place += 1
            Lane3 = Place
            LedDisplay(3, Lane3)
            Place += 1
            Lane4 = Place
            LedDisplay(4, Lane4)
basic.forever(on_forever)

def on_forever2():
    global Place
    if Place == 4:
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
        led.plot(3, Lane3)
        led.plot(4, Lane4)
        Place += 1
basic.forever(on_forever2)

def on_forever3():
    global Place, Lane1
    if input.button_is_pressed(Button.A):
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
            LedDisplay(1, Lane1)
basic.forever(on_forever3)
