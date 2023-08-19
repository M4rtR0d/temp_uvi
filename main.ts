let UVi = 0
let temp = 0
basic.showString("Hello!")
basic.forever(function () {
    temp = input.temperature()
    basic.showNumber(temp)
    basic.pause(1000)
    basic.showLeds(`
        . . . . #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
        `)
    UVi = 0
    basic.showNumber(UVi)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
})
