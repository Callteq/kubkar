# udpate LEDs
# Mode =1 is to display a lane has finsihe dthe race but not show the finish position
# Mode =2 displays the finish positon for each Lane
def LedDisplay(Lane: number, Position: number, Mode: number):
    global firstKar, LedPos, winnerStrip2, haveWinner, secondStrip2, thirdStrip2, fourthStrip2
    if firstKar == 0:
        firstKar = 1
        basic.clear_screen()
    LedPos = (Lane - 1) * 4
    if Mode == 1:
        laneStrip = strip.range(LedPos, 4)
        laneStrip.show_color(neopixel.colors(NeoPixelColors.PURPLE))
        # indicate which lane we have seen finsih the race
        led.plot(Lane, 1)
    else:
        # indicate final positions
        led.plot(Lane, Position)
        if Position == 1:
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            strip.show()
            winnerStrip2 = strip.range(LedPos, 4)
            winnerStrip2.show_color(neopixel.colors(NeoPixelColors.BLUE))
            # triggers the fancy lights for the winner
            haveWinner = 1
        elif Position == 2:
            secondStrip2 = strip.range(LedPos, 2)
            secondStrip2.show_color(neopixel.colors(NeoPixelColors.RED))
            secondStrip2.show()
        elif Position == 3:
            thirdStrip2 = strip.range(LedPos, 3)
            thirdStrip2.show_color(neopixel.colors(NeoPixelColors.GREEN))
            thirdStrip2.show()
        else:
            fourthStrip2 = strip.range(LedPos, 4)
            fourthStrip2.show_color(neopixel.colors(NeoPixelColors.ORANGE))
            fourthStrip2.show()
# Reset the race

def on_button_pressed_a():
    global thePlace, Lane1Place, Lane2Place, Lane3Place, Lane4Place, Diag, haveWinner, firstKar, winnerStrip, secondStrip, thirdStrip, fourthStrip
    thePlace = -2
    Lane1Place = 0
    Lane2Place = 0
    Lane3Place = 0
    Lane4Place = 0
    Diag = 0
    haveWinner = 0
    firstKar = 0
    # basic.show_icon(IconNames.SQUARE)
    # basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    strip.show_color(neopixel.colors(NeoPixelColors.RED))
    strip.show()
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    strip.show()
    basic.pause(500)
    winnerStrip = strip.range(0, 4)
    secondStrip = strip.range(4, 4)
    thirdStrip = strip.range(8, 4)
    fourthStrip = strip.range(12, 4)
    winnerStrip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    secondStrip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    thirdStrip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    fourthStrip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    winnerStrip.show()
    secondStrip.show()
    thirdStrip.show()
    fourthStrip.show()
    winnerStrip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
    secondStrip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
    thirdStrip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
    fourthStrip.set_pixel_color(0, neopixel.colors(NeoPixelColors.GREEN))
    winnerStrip.show()
    secondStrip.show()
    thirdStrip.show()
    fourthStrip.show()
    basic.pause(500)
    for index in range(3):
        index2 = 0
        while index2 < 3:
            winnerStrip.rotate(1)
            secondStrip.rotate(1)
            thirdStrip.rotate(1)
            fourthStrip.rotate(1)
            winnerStrip.show()
            secondStrip.show()
            thirdStrip.show()
            fourthStrip.show()
            basic.pause(50)
            index2 += 1
        index2 = 0
        while index2 < 3:
            winnerStrip.rotate(-1)
            secondStrip.rotate(-1)
            thirdStrip.rotate(-1)
            fourthStrip.rotate(-1)
            winnerStrip.show()
            secondStrip.show()
            thirdStrip.show()
            fourthStrip.show()
            basic.pause(50)
            index2 += 1
    while index2 < 8:
        basic.pause(50)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        strip.show()
        basic.pause(50)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        index2 += 1
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    strip.show()
    basic.clear_screen()
    basic.show_icon(IconNames.HAPPY)
    # we are now waiting for the lane sensors
    thePlace = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    strip.show()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# simulate the cars crossing the finish line one Kar on each press of Button B

def on_button_pressed_b():
    global thePlace, Lane1Place, Lane2Place, Lane3Place, Lane4Place
    if thePlace < 0:
        led.plot(0, 1)
        basic.pause(50)
        led.unplot(0, 1)
    elif Lane1Place == 0:
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

def ledFlag():
    global winnerStrip2
    winnerStrip2 = strip.range(0, 16)
    winnerStrip2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    winnerStrip2.set_pixel_color(0, neopixel.colors(NeoPixelColors.WHITE))
    winnerStrip2.set_pixel_color(2, neopixel.colors(NeoPixelColors.WHITE))
    winnerStrip2.set_pixel_color(5, neopixel.colors(NeoPixelColors.WHITE))
    winnerStrip2.set_pixel_color(7, neopixel.colors(NeoPixelColors.WHITE))
    winnerStrip2.set_pixel_color(8, neopixel.colors(NeoPixelColors.WHITE))
    winnerStrip2.set_pixel_color(10, neopixel.colors(NeoPixelColors.WHITE))
    winnerStrip2.set_pixel_color(13, neopixel.colors(NeoPixelColors.WHITE))
    winnerStrip2.set_pixel_color(15, neopixel.colors(NeoPixelColors.WHITE))
    winnerStrip2.show()
    basic.pause(500)
    index3 = 0
    while index3 < 16:
        winnerStrip2.rotate(4)
        winnerStrip2.show()
        basic.pause(50)
        winnerStrip2.rotate(-4)
        winnerStrip2.show()
        basic.pause(50)
        index3 += 1
    basic.pause(500)
    winnerStrip2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    winnerStrip2.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
    winnerStrip2.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLUE))
    winnerStrip2.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLUE))
    winnerStrip2.set_pixel_color(3, neopixel.colors(NeoPixelColors.BLUE))
    index3 = 0
    while index3 < 16:
        winnerStrip2.rotate(4)
        winnerStrip2.show()
        basic.pause(100)
        index3 += 1
    winnerStrip2.show_color(neopixel.colors(NeoPixelColors.BLACK))
"""

globals

"""
fourthStrip: neopixel.Strip = None
thirdStrip: neopixel.Strip = None
secondStrip: neopixel.Strip = None
winnerStrip: neopixel.Strip = None
Diag = 0
Lane4Place = 0
Lane3Place = 0
Lane2Place = 0
Lane1Place = 0
haveWinner = 0
LedPos = 0
fourthStrip2: neopixel.Strip = None
thirdStrip2: neopixel.Strip = None
secondStrip2: neopixel.Strip = None
strip: neopixel.Strip = None
firstKar = 0
winnerStrip2: neopixel.Strip = None
thePlace = -1
firstKar = 0
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
strip = neopixel.create(DigitalPin.P0, 16, NeoPixelMode.RGB)
winnerStrip2 = strip.range(0, 4)
secondStrip2 = strip.range(4, 4)
thirdStrip2 = strip.range(8, 4)
fourthStrip2 = strip.range(12, 4)
strip.show_rainbow(1, 360)
strip.show()

def on_forever():
    global thePlace
    if haveWinner == 1:
        i = 0
        while i < 10:
            # if we are "resetting" breakout of the winner flashing loops
            if thePlace == -2:
                break
            basic.pause(200)
            winnerStrip2.show_color(neopixel.colors(NeoPixelColors.WHITE))
            basic.pause(50)
            winnerStrip2.show_color(neopixel.colors(NeoPixelColors.BLUE))
            winnerStrip2.show()
            i += 1
        winnerStrip2.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        winnerStrip2.set_pixel_color(1, neopixel.colors(NeoPixelColors.BLACK))
        winnerStrip2.set_pixel_color(2, neopixel.colors(NeoPixelColors.BLACK))
        winnerStrip2.set_pixel_color(3, neopixel.colors(NeoPixelColors.BLUE))
        winnerStrip2.show()
        i = 0
        while i < 24:
            if thePlace == -2:
                break
            basic.pause(100)
            winnerStrip2.rotate(1)
            winnerStrip2.show()
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
        ledFlag()
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
        # wait for the next race to be started
        thePlace = -1
basic.forever(on_forever)

# check the track sensors

def on_forever2():
    global thePlace, Lane1Place, Lane2Place, Lane3Place, Lane4Place
    # wait until we are ready to race again
    if thePlace < 0:
        led.plot(0, 0)
        basic.pause(50)
        led.unplot(0, 0)
    else:
        # Lane 1
        if pins.digital_read_pin(DigitalPin.P1) == 1:
            if Lane1Place == 0:
                thePlace = thePlace + 1
                Lane1Place = thePlace
                LedDisplay(1, Lane1Place, 1)
        # Lane 2
        if pins.digital_read_pin(DigitalPin.P8) == 1:
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
