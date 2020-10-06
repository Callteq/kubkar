# udpate LEDs
# Mode =1 is to display a lane has finsihe dthe race but not show the finish position
# Mode =2 displays the finish positon for each Lane
def LedDisplay(Lane: number, Position: number, Mode: number):
    global firstKar, LedPos, winnerStrip, haveWinner, secondStrip, thirdStrip, fourthStrip
    if firstKar == 0:
        firstKar = 1
        basic.clear_screen()
    LedPos = (Lane - 1) * 4
    if Mode == 1:
        laneStrip = strip.range(LedPos, 1)
        laneStrip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
        # indicate which lane we have seen finsih the race
        led.plot(Lane, 1)
    else:
        # indicate final positions
        led.plot(Lane, Position)
        if Position == 1:
            winnerStrip = strip.range(LedPos, 4)
            winnerStrip.show_color(neopixel.colors(NeoPixelColors.BLUE))
            haveWinner = 1
        elif Position == 2:
            secondStrip = strip.range(LedPos, 2)
            secondStrip.show_color(neopixel.colors(NeoPixelColors.RED))
        elif Position == 3:
            thirdStrip = strip.range(LedPos, 3)
            thirdStrip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        else:
            fourthStrip = strip.range(LedPos, 4)
            fourthStrip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
# Reset the race

def on_button_pressed_a():
    global thePlace, Lane1Place, Lane2Place, Lane3Place, Lane4Place, Diag, haveWinner, firstKar
    thePlace = 99
    Lane1Place = 0
    Lane2Place = 0
    Lane3Place = 0
    Lane4Place = 0
    Diag = 0
    haveWinner = 0
    firstKar = 0
    # basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    #basic.show_icon(IconNames.SMALL_DIAMOND)
    for index in range(3):
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
        strip.set_pixel_color(4, neopixel.colors(NeoPixelColors.GREEN))
        strip.set_pixel_color(8, neopixel.colors(NeoPixelColors.GREEN))
        strip.set_pixel_color(12, neopixel.colors(NeoPixelColors.GREEN))
        index2 = 0
        while index2 < 4:
            basic.pause(30)
            strip.shift(1)
            strip.show()
            index2 += 1
        index2 = 0
        while index2 < 4:
            basic.pause(100)
            strip.shift(-1)
            strip.show()
            index2 += 1
    index2 = 0
    while index2 < 8:
        basic.pause(50)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        strip.show()
        basic.pause(100)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        index2 += 1
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.clear_screen()
    basic.show_icon(IconNames.HAPPY)
    thePlace = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

# simulate the cars crossing the finish line one Kar on each press of Button B

def on_button_pressed_b():
    global Diag, thePlace, Lane1Place, Lane2Place, Lane3Place, Lane4Place
    Diag = Diag + 1
    if  Lane1Place == 0:
        thePlace = thePlace + 1
        Lane1Place = thePlace
        LedDisplay(1, Lane1Place, 1)
    elif Lane2Place == 0:
        thePlace = thePlace + 1
        Lane2Place = thePlace
        LedDisplay(2, Lane2Place, 1)
    elif Lane3Place == 0:
        thePlace = thePlace + 1
        Lane3Place = thePlace
        LedDisplay(3, Lane3Place, 1)
    elif Lane4Place == 0:
        thePlace = thePlace + 1
        Lane4Place = thePlace
        LedDisplay(4, Lane4Place, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Diag = 0
Lane4Place = 0
Lane3Place = 0
Lane2Place = 0
Lane1Place = 0
thePlace = 0
LedPos = 0
fourthStrip: neopixel.Strip = None
thirdStrip: neopixel.Strip = None
secondStrip: neopixel.Strip = None
winnerStrip: neopixel.Strip = None
strip: neopixel.Strip = None
haveWinner = 0
firstKar = 0
firstKar = 0
haveWinner = 0
firstKar = 0
basic.show_icon(IconNames.NO)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_DOWN)
# Lane 1 Sensor
pins.set_pull(DigitalPin.P8, PinPullMode.PULL_DOWN)
# Lane 2 Sensor
pins.set_pull(DigitalPin.P15, PinPullMode.PULL_DOWN)
# Lane 3 Sensor
pins.set_pull(DigitalPin.P16, PinPullMode.PULL_DOWN)
# Lane 4 Sensor
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
winnerStrip = strip.range(0, 4)
secondStrip = strip.range(4, 4)
thirdStrip = strip.range(8, 4)
fourthStrip = strip.range(12, 4)
strip.show_rainbow(1, 360)
# winnerStrip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
strip.show()

def on_forever():
    global thePlace
    if haveWinner == 1:
        i = 0
        while i < 10:
            basic.pause(100)
            winnerStrip.show_color(neopixel.colors(NeoPixelColors.WHITE))
            basic.pause(100)
            winnerStrip.show_color(neopixel.colors(NeoPixelColors.BLUE))
            winnerStrip.show()
            i += 1
        winnerStrip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        winnerStrip.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
        winnerStrip.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLACK))
        winnerStrip.set_pixel_color(3, neopixel.colors(NeoPixelColors.BLUE))
        winnerStrip.show()
        i = 0
        while i < 24:
            basic.pause(100)
            winnerStrip.rotate(1)
            winnerStrip.show()
            i += 1
    if thePlace == 4:
        basic.pause(1000)
        images.create_big_image("""
            # . # . # . # . # .
            . # . # . # . # . #
            # . # . # . # . # .
            . # . # . # . # . #
            # . # . # . # . # .
            """).scroll_image(1, 50)
        basic.show_leds("""
            . # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        # display final positions
        LedDisplay(1, Lane1Place, 2)
        LedDisplay(2, Lane2Place, 2)
        LedDisplay(3, Lane3Place, 2)
        LedDisplay(4, Lane4Place, 2)
        thePlace = thePlace + 1
basic.forever(on_forever)

# check the track sensors

def on_forever2():
    global thePlace, Lane1Place, Lane2Place, Lane3Place, Lane4Place
    # Lane 1
    if pins.digital_read_pin(DigitalPin.P1) == 1:
        if Lane1Place == 0:
            thePlace = thePlace + 1
            Lane1Place = thePlace
            LedDisplay(1, Lane1Place, 1)
    # Lane 2
    if pins.digital_read_pin(DigitalPin.P8) == 1:
        basic.pause(1000)
        if Lane2Place == 0:
            thePlace = thePlace + 1
            Lane2Place = thePlace
            LedDisplay(2, Lane2Place, 1)
    # Lane 3
    if pins.digital_read_pin(DigitalPin.P15) == 1:
        if Lane3Place == 0:
            thePlace = thePlace + 1
            Lane3Place = thePlace
            LedDisplay(3, Lane3Place, 1)
    # Lane 4
    if pins.digital_read_pin(DigitalPin.P16) == 1:
        if Lane4Place == 0:
            thePlace = thePlace + 1
            Lane4Place = thePlace
            LedDisplay(4, Lane4Place, 1)
basic.forever(on_forever2)
