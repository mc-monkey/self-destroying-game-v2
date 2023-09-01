def on_button_pressed_a():
    turtle.turn_left()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("END")
    basic.show_string("RESTART BEFORE ITS TOO LATE")
    for index in range(1e+26):
        turtle.set_speed(1)
        turtle.home()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    turtle.turn_right()
input.on_button_pressed(Button.B, on_button_pressed_b)

music.play(music.string_playable("A B C5 C5 G F E E ", 120),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)
basic.show_string("START")

def on_forever():
    turtle.pen(TurtlePenMode.DOWN)
    basic.pause(1000)
    turtle.forward(1)
basic.forever(on_forever)
