function LedDisplay (Lane: number, Position: number, Mode: number) {
    // indicate which lane
    led.plot(Lane, 1)
    LedPos = (Lane - 1) * 4
    if (Mode == 1) {
        laneStrip = strip.range(LedPos, 1)
        laneStrip.showColor(neopixel.colors(NeoPixelColors.Purple))
    } else {
        laneStrip = strip.range(LedPos, 4)
        if (Position == 1) {
            laneStrip.showColor(neopixel.colors(NeoPixelColors.Blue))
            winnerStrip = strip.range(LedPos, 4)
            winnerStrip.showColor(neopixel.colors(NeoPixelColors.Blue))
            haveWinner = 1
        } else if (Position == 2) {
            laneStrip.showColor(neopixel.colors(NeoPixelColors.Red))
        } else if (Position == 3) {
            laneStrip.showColor(neopixel.colors(NeoPixelColors.Green))
        } else {
            laneStrip.showColor(neopixel.colors(NeoPixelColors.White))
        }
    }
    laneStrip.show()
}
// Reset the race
input.onButtonPressed(Button.A, function () {
    // initiialise
    thePlace = 99
    Lane1Place = 0
    Lane2Place = 0
    Lane3Place = 0
    Lane4Place = 0
    Diag = 0
    haveWinner = 0
    basic.showIcon(IconNames.Square)
    basic.showIcon(IconNames.SmallSquare)
    thePlace = 0
    basic.showIcon(IconNames.SmallDiamond)
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
})
// simulate the cars crossing the finsih line one ach press of Button B
input.onButtonPressed(Button.B, function () {
    Diag = Diag + 1
    if (Diag == 1) {
        thePlace = thePlace + 1
        Lane1Place = thePlace
        LedDisplay(1, Lane1Place, 1)
    } else if (Diag == 2) {
        thePlace = thePlace + 1
        Lane2Place = thePlace
        LedDisplay(2, Lane2Place, 1)
    } else if (Diag == 3) {
        thePlace = thePlace + 1
        Lane3Place = thePlace
        LedDisplay(3, Lane3Place, 1)
    } else if (Diag == 4) {
        thePlace = thePlace + 1
        Lane4Place = thePlace
        LedDisplay(4, Lane4Place, 1)
    }
})
let Diag = 0
let Lane4Place = 0
let Lane3Place = 0
let Lane2Place = 0
let Lane1Place = 0
let thePlace = 0
let winnerStrip: neopixel.Strip = null
let laneStrip: neopixel.Strip = null
let LedPos = 0
let strip: neopixel.Strip = null
let haveWinner = 0
haveWinner = 0
basic.showIcon(IconNames.No)
pins.setPull(DigitalPin.P1, PinPullMode.PullNone)
pins.setPull(DigitalPin.P8, PinPullMode.PullNone)
pins.setPull(DigitalPin.P2, PinPullMode.PullNone)
pins.setPull(DigitalPin.P16, PinPullMode.PullNone)
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
strip.show()
basic.forever(function () {
    if (haveWinner == 1) {
        basic.pause(50)
        winnerStrip.showColor(neopixel.colors(NeoPixelColors.Red))
        basic.pause(50)
    }
})
// wait until we have all 4 cars across the finish line
basic.forever(function () {
    if (thePlace == 4) {
        images.createBigImage(`
            # . # . # . # . # .
            . # . # . # . # . #
            # . # . # . # . # .
            . # . # . # . # . #
            # . # . # . # . # .
            `).scrollImage(1, 50)
        control.waitMicros(100)
        basic.showLeds(`
            # # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        LedDisplay(1, Lane1Place, 2)
        LedDisplay(2, Lane2Place, 2)
        LedDisplay(3, Lane3Place, 2)
        LedDisplay(4, Lane4Place, 2)
        thePlace = thePlace + 1
    }
})
