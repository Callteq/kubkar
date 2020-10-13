//  udpate LEDs
//  Mode =1 is to display a lane has finsihe dthe race but not show the finish position
//  Mode =2 displays the finish positon for each Lane
function LedDisplay(Lane: number, Position: number, Mode: number) {
    let laneStrip: neopixel.Strip;
    
    if (firstKar == 0) {
        firstKar = 1
        basic.clearScreen()
    }
    
    LedPos = (Lane - 1) * 4
    if (Mode == 1) {
        laneStrip = strip.range(LedPos, 4)
        laneStrip.showColor(neopixel.colors(NeoPixelColors.Purple))
        //  indicate which lane we have seen finsih the race
        led.plot(Lane, 1)
    } else {
        //  indicate final positions
        led.plot(Lane, Position)
        if (Position == 1) {
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
            strip.show()
            winnerStrip2 = strip.range(LedPos, 4)
            winnerStrip2.showColor(neopixel.colors(NeoPixelColors.Blue))
            //  triggers the fancy lights for the winner
            haveWinner = 1
        } else if (Position == 2) {
            secondStrip2 = strip.range(LedPos, 2)
            secondStrip2.showColor(neopixel.colors(NeoPixelColors.Red))
            secondStrip2.show()
        } else if (Position == 3) {
            thirdStrip2 = strip.range(LedPos, 3)
            thirdStrip2.showColor(neopixel.colors(NeoPixelColors.Green))
            thirdStrip2.show()
        } else {
            fourthStrip2 = strip.range(LedPos, 4)
            fourthStrip2.showColor(neopixel.colors(NeoPixelColors.Orange))
            fourthStrip2.show()
        }
        
    }
    
}

//  Reset the race
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let index2: number;
    
    thePlace = -2
    Lane1Place = 0
    Lane2Place = 0
    Lane3Place = 0
    Lane4Place = 0
    Diag = 0
    haveWinner = 0
    firstKar = 0
    //  basic.show_icon(IconNames.SQUARE)
    //  basic.show_icon(IconNames.SMALL_SQUARE)
    basic.showIcon(IconNames.SmallDiamond)
    strip.showColor(neopixel.colors(NeoPixelColors.Red))
    strip.show()
    basic.pause(500)
    strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
    strip.show()
    basic.pause(500)
    winnerStrip = strip.range(0, 4)
    secondStrip = strip.range(4, 4)
    thirdStrip = strip.range(8, 4)
    fourthStrip = strip.range(12, 4)
    winnerStrip.showColor(neopixel.colors(NeoPixelColors.Black))
    secondStrip.showColor(neopixel.colors(NeoPixelColors.Black))
    thirdStrip.showColor(neopixel.colors(NeoPixelColors.Black))
    fourthStrip.showColor(neopixel.colors(NeoPixelColors.Black))
    winnerStrip.show()
    secondStrip.show()
    thirdStrip.show()
    fourthStrip.show()
    winnerStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
    secondStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
    thirdStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
    fourthStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Green))
    winnerStrip.show()
    secondStrip.show()
    thirdStrip.show()
    fourthStrip.show()
    basic.pause(500)
    for (let index = 0; index < 3; index++) {
        index2 = 0
        while (index2 < 3) {
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
        }
        index2 = 0
        while (index2 < 3) {
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
        }
    }
    while (index2 < 8) {
        basic.pause(50)
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        strip.show()
        basic.pause(50)
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        strip.show()
        index2 += 1
    }
    strip.showColor(neopixel.colors(NeoPixelColors.Green))
    strip.show()
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
    //  we are now waiting for the lane sensors
    thePlace = 0
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
    strip.show()
})
//  simulate the cars crossing the finish line one Kar on each press of Button B
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (thePlace < 0) {
        led.plot(0, 1)
        basic.pause(50)
        led.unplot(0, 1)
    } else if (Lane1Place == 0) {
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
function ledFlag() {
    
    winnerStrip2 = strip.range(0, 16)
    winnerStrip2.showColor(neopixel.colors(NeoPixelColors.Black))
    winnerStrip2.setPixelColor(0, neopixel.colors(NeoPixelColors.White))
    winnerStrip2.setPixelColor(2, neopixel.colors(NeoPixelColors.White))
    winnerStrip2.setPixelColor(5, neopixel.colors(NeoPixelColors.White))
    winnerStrip2.setPixelColor(7, neopixel.colors(NeoPixelColors.White))
    winnerStrip2.setPixelColor(8, neopixel.colors(NeoPixelColors.White))
    winnerStrip2.setPixelColor(10, neopixel.colors(NeoPixelColors.White))
    winnerStrip2.setPixelColor(13, neopixel.colors(NeoPixelColors.White))
    winnerStrip2.setPixelColor(15, neopixel.colors(NeoPixelColors.White))
    winnerStrip2.show()
    basic.pause(500)
    let index3 = 0
    while (index3 < 16) {
        winnerStrip2.rotate(4)
        winnerStrip2.show()
        basic.pause(50)
        winnerStrip2.rotate(-4)
        winnerStrip2.show()
        basic.pause(50)
        index3 += 1
    }
    basic.pause(500)
    winnerStrip2.showColor(neopixel.colors(NeoPixelColors.Black))
    winnerStrip2.setPixelColor(0, neopixel.colors(NeoPixelColors.Blue))
    winnerStrip2.setPixelColor(1, neopixel.colors(NeoPixelColors.Blue))
    winnerStrip2.setPixelColor(2, neopixel.colors(NeoPixelColors.Blue))
    winnerStrip2.setPixelColor(3, neopixel.colors(NeoPixelColors.Blue))
    index3 = 0
    while (index3 < 16) {
        winnerStrip2.rotate(4)
        winnerStrip2.show()
        basic.pause(100)
        index3 += 1
    }
    winnerStrip2.showColor(neopixel.colors(NeoPixelColors.Black))
}

/** globals */
let fourthStrip : neopixel.Strip = null
let thirdStrip : neopixel.Strip = null
let secondStrip : neopixel.Strip = null
let winnerStrip : neopixel.Strip = null
let Diag = 0
let Lane4Place = 0
let Lane3Place = 0
let Lane2Place = 0
let Lane1Place = 0
let haveWinner = 0
let LedPos = 0
let fourthStrip2 : neopixel.Strip = null
let thirdStrip2 : neopixel.Strip = null
let secondStrip2 : neopixel.Strip = null
let strip : neopixel.Strip = null
let firstKar = 0
let winnerStrip2 : neopixel.Strip = null
let thePlace = -1
firstKar = 0
firstKar = 0
basic.showIcon(IconNames.No)
pins.setPull(DigitalPin.P1, PinPullMode.PullDown)
//  Lane 1 Sensor
pins.setPull(DigitalPin.P8, PinPullMode.PullDown)
//  Lane 2 Sensor
pins.setPull(DigitalPin.P15, PinPullMode.PullDown)
//  Lane 3 Sensor
pins.setPull(DigitalPin.P16, PinPullMode.PullDown)
//  Lane 4 Sensor
strip = neopixel.create(DigitalPin.P0, 16, NeoPixelMode.RGB)
winnerStrip2 = strip.range(0, 4)
secondStrip2 = strip.range(4, 4)
thirdStrip2 = strip.range(8, 4)
fourthStrip2 = strip.range(12, 4)
strip.showRainbow(1, 360)
strip.show()
basic.forever(function on_forever() {
    let i: number;
    
    if (haveWinner == 1) {
        i = 0
        while (i < 10) {
            //  if we are "resetting" breakout of the winner flashing loops
            if (thePlace == -2) {
                break
            }
            
            basic.pause(200)
            winnerStrip2.showColor(neopixel.colors(NeoPixelColors.White))
            basic.pause(50)
            winnerStrip2.showColor(neopixel.colors(NeoPixelColors.Blue))
            winnerStrip2.show()
            i += 1
        }
        winnerStrip2.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
        winnerStrip2.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
        winnerStrip2.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
        winnerStrip2.setPixelColor(3, neopixel.colors(NeoPixelColors.Blue))
        winnerStrip2.show()
        i = 0
        while (i < 24) {
            if (thePlace == -2) {
                break
            }
            
            basic.pause(100)
            winnerStrip2.rotate(1)
            winnerStrip2.show()
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
        ledFlag()
        basic.showLeds(`
            . # # # #
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        //  display final positions
        LedDisplay(1, Lane1Place, 2)
        LedDisplay(2, Lane2Place, 2)
        LedDisplay(3, Lane3Place, 2)
        LedDisplay(4, Lane4Place, 2)
        //  wait for the next race to be started
        thePlace = -1
    }
    
})
//  check the track sensors
basic.forever(function on_forever2() {
    
    //  wait until we are ready to race again
    if (thePlace < 0) {
        led.plot(0, 0)
        basic.pause(50)
        led.unplot(0, 0)
    } else {
        //  Lane 1
        if (pins.digitalReadPin(DigitalPin.P1) == 1) {
            if (Lane1Place == 0) {
                thePlace = thePlace + 1
                Lane1Place = thePlace
                LedDisplay(1, Lane1Place, 1)
            }
            
        }
        
        //  Lane 2
        if (pins.digitalReadPin(DigitalPin.P8) == 1) {
            if (Lane2Place == 0) {
                thePlace = thePlace + 1
                Lane2Place = thePlace
                LedDisplay(2, Lane2Place, 1)
            }
            
        }
        
        //  Lane 3
        if (pins.digitalReadPin(DigitalPin.P15) == 1) {
            if (Lane3Place == 0) {
                thePlace = thePlace + 1
                Lane3Place = thePlace
                LedDisplay(3, Lane3Place, 1)
            }
            
        }
        
        //  Lane 4
        if (pins.digitalReadPin(DigitalPin.P16) == 1) {
            if (Lane4Place == 0) {
                thePlace = thePlace + 1
                Lane4Place = thePlace
                LedDisplay(4, Lane4Place, 1)
            }
            
        }
        
    }
    
})
