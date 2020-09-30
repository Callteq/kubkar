input.onButtonPressed(Button.A, function () {
    Place = 0
    Lane1 = 0
    Lane2 = 0
    Lane3 = 0
    Lane4 = 0
    basic.showIcon(IconNames.Square)
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.SmallDiamond)
})
let Lane4 = 0
let Lane3 = 0
let Lane2 = 0
let Lane1 = 0
let Place = 0
basic.showIcon(IconNames.No)
pins.setPull(DigitalPin.P0, PinPullMode.PullNone)
pins.setPull(DigitalPin.P1, PinPullMode.PullNone)
pins.setPull(DigitalPin.P8, PinPullMode.PullNone)
pins.setPull(DigitalPin.P2, PinPullMode.PullNone)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P1) == 0) {
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
        }
    }
})
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P2) == 0) {
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
        }
    }
})
basic.forever(function () {
    if (Place == 2) {
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
        Place += 1
    }
})
