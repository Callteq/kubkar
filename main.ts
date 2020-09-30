function LedDisplay(Lane: number, Position: number) {
    
    if (Position == 1) {
        LedPos = (Lane - 1) * 4
        range2 = strip.range(LedPos, 4)
        for (let index = 0; index < 20; index++) {
            range2.showColor(neopixel.colors(NeoPixelColors.Blue))
            control.waitMicros(100)
            range2.showColor(neopixel.colors(NeoPixelColors.White))
            control.waitMicros(100)
            range2.showColor(neopixel.colors(NeoPixelColors.Blue))
        }
    } else {
        LedPos = (Lane - 1) * 4 + Position
        range2 = strip.range(LedPos, 1)
        if (Position == 2) {
            range2.showColor(neopixel.colors(NeoPixelColors.Red))
        } else if (Position == 3) {
            range2.showColor(neopixel.colors(NeoPixelColors.Green))
        } else {
            range2.showColor(neopixel.colors(NeoPixelColors.White))
        }
        
    }
    
    range2.show()
}

input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Place = 99
    Lane1 = 0
    Lane2 = 0
    Lane3 = 0
    Lane4 = 0
    basic.showIcon(IconNames.Square)
    basic.showIcon(IconNames.SmallSquare)
    Place = 0
    basic.showIcon(IconNames.SmallDiamond)
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
})
let Lane4 = 0
let Lane3 = 0
let Lane2 = 0
let Lane1 = 0
let Place = 0
let range2 : neopixel.Strip = null
let LedPos = 0
let strip : neopixel.Strip = null
basic.showIcon(IconNames.No)
pins.setPull(DigitalPin.P1, PinPullMode.PullNone)
pins.setPull(DigitalPin.P8, PinPullMode.PullNone)
pins.setPull(DigitalPin.P2, PinPullMode.PullNone)
pins.setPull(DigitalPin.P16, PinPullMode.PullNone)
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
strip.show()
basic.forever(function on_forever() {
    
    if (input.buttonIsPressed(Button.B)) {
        if (Lane2 == 0) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . # . . .
                `)
            Place += 1
            Lane2 = Place
            LedDisplay(2, Lane2)
            Place += 1
            Lane3 = Place
            LedDisplay(3, Lane3)
            Place += 1
            Lane4 = Place
            LedDisplay(4, Lane4)
        }
        
    }
    
})
basic.forever(function on_forever2() {
    
    if (Place == 4) {
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
        led.plot(0, Lane1)
        led.plot(1, Lane2)
        led.plot(3, Lane3)
        led.plot(4, Lane4)
        Place += 1
    }
    
})
basic.forever(function on_forever3() {
    
    if (input.buttonIsPressed(Button.A)) {
        if (Lane1 == 0) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                `)
            Place += 1
            Lane1 = Place
            LedDisplay(1, Lane1)
        }
        
    }
    
})
