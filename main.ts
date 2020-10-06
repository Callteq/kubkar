// udpate LEDs
// Mode =1 is to display a lane has finsihe dthe race but not show the finish position
// Mode =2 displays the finish positon for each Lane
function LedDisplay (Lane: number, Position: number, Mode: number) {
    let laneStrip: neopixel.Strip;
if (firstKar == 0) {
        firstKar = 1
        basic.clearScreen()
    }
    LedPos = (Lane - 1) * 4
    if (Mode == 1) {
        laneStrip = strip.range(LedPos, 1)
        laneStrip.showColor(neopixel.colors(NeoPixelColors.Purple))
        // indicate which lane we have seen finsih the race
        led.plot(Lane, 1)
    } else {
        // indicate final positions
        led.plot(Lane, Position)
        if (Position == 1) {
            winnerStrip = strip.range(LedPos, 4)
            winnerStrip.showColor(neopixel.colors(NeoPixelColors.Blue))
            haveWinner = 1
        } else if (Position == 2) {
            secondStrip = strip.range(LedPos, 2)
            secondStrip.showColor(neopixel.colors(NeoPixelColors.Red))
        } else if (Position == 3) {
            thirdStrip = strip.range(LedPos, 3)
            thirdStrip.showColor(neopixel.colors(NeoPixelColors.Green))
        } else {
            fourthStrip = strip.range(LedPos, 4)
            fourthStrip.showColor(neopixel.colors(NeoPixelColors.Orange))
        }
    }
}
// Reset the race
input.onButtonPressed(Button.A, function () {
    let index2: number;
thePlace = 99
    Lane1Place = 0
    Lane2Place = 0
    Lane3Place = 0
    Lane4Place = 0
    Diag = 0
    haveWinner = 0
    firstKar = 0
    // basic.show_icon(IconNames.SQUARE)
    basic.showIcon(IconNames.SmallSquare)
    // basic.show_icon(IconNames.SMALL_DIAMOND)
    for (let index = 0; index < 3; index++) {
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
        strip.setPixelColor(4, neopixel.colors(NeoPixelColors.Green))
        strip.setPixelColor(8, neopixel.colors(NeoPixelColors.Green))
        strip.setPixelColor(12, neopixel.colors(NeoPixelColors.Green))
        index2 = 0
        while (index2 < 4) {
            basic.pause(30)
            strip.shift(1)
            strip.show()
            index2 += 1
        }
        index2 = 0
        while (index2 < 4) {
            basic.pause(100)
            strip.shift(-1)
            strip.show()
            index2 += 1
        }
    }
    index2 = 0
    while (index2 < 8) {
        basic.pause(50)
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        strip.show()
        basic.pause(100)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        strip.show()
        index2 += 1
    }
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
    thePlace = 0
})
// simulate the cars crossing the finish line one Kar on each press of Button B
input.onButtonPressed(Button.B, function () {
    Diag = Diag + 1
    if (Lane1Place == 0) {
        thePlace = thePlace + 1
        Lane1Place = thePlace
        LedDisplay(1, Lane1Place, 1)
    } else if (Lane2Place == 0) {
        thePlace = thePlace + 1
        Lane2Place = thePlace
        LedDisplay(2, Lane2Place, 1)
    } else if (Lane3Place == 0) {
        thePlace = thePlace + 1
        Lane3Place = thePlace
        LedDisplay(3, Lane3Place, 1)
    } else if (Lane4Place == 0) {
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
let LedPos = 0
let fourthStrip: neopixel.Strip = null
let thirdStrip: neopixel.Strip = null
let secondStrip: neopixel.Strip = null
let winnerStrip: neopixel.Strip = null
let strip: neopixel.Strip = null
let haveWinner = 0
let firstKar = 0
firstKar = 0
haveWinner = 0
firstKar = 0
basic.showIcon(IconNames.No)
pins.setPull(DigitalPin.P1, PinPullMode.PullDown)
// Lane 1 Sensor
pins.setPull(DigitalPin.P8, PinPullMode.PullDown)
// Lane 2 Sensor
pins.setPull(DigitalPin.P15, PinPullMode.PullDown)
// Lane 3 Sensor
pins.setPull(DigitalPin.P16, PinPullMode.PullDown)
// Lane 4 Sensor
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
winnerStrip = strip.range(0, 4)
secondStrip = strip.range(4, 4)
thirdStrip = strip.range(8, 4)
fourthStrip = strip.range(12, 4)
strip.showRainbow(1, 360)
// winnerStrip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
strip.show()
basic.forever(function () {
    let i: number;
if (haveWinner == 1) {
        i = 0
        while (i < 10) {
            basic.pause(100)
            winnerStrip.showColor(neopixel.colors(NeoPixelColors.White))
            basic.pause(100)
            winnerStrip.showColor(neopixel.colors(NeoPixelColors.Blue))
            winnerStrip.show()
            i += 1
        }
        winnerStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
        winnerStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
        winnerStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
        winnerStrip.setPixelColor(3, neopixel.colors(NeoPixelColors.Blue))
        winnerStrip.show()
        i = 0
        while (i < 24) {
            basic.pause(100)
            winnerStrip.rotate(1)
            winnerStrip.show()
            i += 1
        }
    }
    if (thePlace == 4) {
        basic.pause(1000)
        images.createBigImage(`
            # . # . # . # . # .
            . # . # . # . # . #
            # . # . # . # . # .
            . # . # . # . # . #
            # . # . # . # . # .
            `).scrollImage(1, 50)
        basic.showLeds(`
            . # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        // display final positions
        LedDisplay(1, Lane1Place, 2)
        LedDisplay(2, Lane2Place, 2)
        LedDisplay(3, Lane3Place, 2)
        LedDisplay(4, Lane4Place, 2)
        thePlace = thePlace + 1
    }
})
// check the track sensors
basic.forever(function () {
    // Lane 1
    if (pins.digitalReadPin(DigitalPin.P1) == 1) {
        if (Lane1Place == 0) {
            thePlace = thePlace + 1
            Lane1Place = thePlace
            LedDisplay(1, Lane1Place, 1)
        }
    }
    // Lane 2
    if (pins.digitalReadPin(DigitalPin.P8) == 1) {
        basic.pause(1000)
        if (Lane2Place == 0) {
            thePlace = thePlace + 1
            Lane2Place = thePlace
            LedDisplay(2, Lane2Place, 1)
        }
    }
    // Lane 3
    if (pins.digitalReadPin(DigitalPin.P15) == 1) {
        if (Lane3Place == 0) {
            thePlace = thePlace + 1
            Lane3Place = thePlace
            LedDisplay(3, Lane3Place, 1)
        }
    }
    // Lane 4
    if (pins.digitalReadPin(DigitalPin.P16) == 1) {
        if (Lane4Place == 0) {
            thePlace = thePlace + 1
            Lane4Place = thePlace
            LedDisplay(4, Lane4Place, 1)
        }
    }
})
