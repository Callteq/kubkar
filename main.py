def LedDisplay(Lane: number, Position: number):
    global LedPos, range2
    LedPos = (Lane - 1) * 4
    range2 = strip.range(LedPos, Position)
    if Position == 1:
        range2.show_color(neopixel.colors(NeoPixelColors.BLUE))
    elif Position == 2:
        range2.show_color(neopixel.colors(NeoPixelColors.RED))
    elif Position == 3:
        range2.show_color(neopixel.colors(NeoPixelColors.GREEN))
    else:
        range2.show_color(neopixel.colors(NeoPixelColors.WHITE))
    range2.show()

def on_button_pressed_ab():
    global Place, Lane1, Lane2, Lane3, Lane4
    Place = 0
    Lane1 = 0
    Lane2 = 0
    Lane3 = 0
    Lane4 = 0
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SMALL_DIAMOND)
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
strip = neopixel.create(DigitalPin.P0, 8, NeoPixelMode.RGB)
L1 = strip.range(0, 3)
L2 = strip.range(4, 7)
L3 = strip.range(8, 11)
L4 = strip.range(12, 15)
strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
strip.show()

def on_forever():
    global Place, Lane2
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
basic.forever(on_forever)

def on_forever2():
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
