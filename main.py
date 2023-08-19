UVi = 0
temp = 0
basic.show_string("Hello!")

def on_forever():
    global temp, UVi
    temp = input.temperature()
    basic.show_number(temp)
    basic.pause(1000)
    basic.show_leds("""
        . . . . #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
        """)
    UVi = 0
    basic.show_number(UVi)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
basic.forever(on_forever)
