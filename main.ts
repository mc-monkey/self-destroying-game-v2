input.onButtonPressed(Button.A, function on_button_pressed_a() {
    turtle.turnLeft()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString("END")
    basic.showString("RESTART BEFORE ITS TOO LATE")
    for (let index = 0; index < 1e+26; index++) {
        turtle.setSpeed(1)
        turtle.home()
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    turtle.turnRight()
})
music.play(music.stringPlayable("A B C5 C5 G F E E ", 120), music.PlaybackMode.LoopingInBackground)
basic.showString("START")
basic.forever(function on_forever() {
    turtle.pen(TurtlePenMode.Down)
    basic.pause(1000)
    turtle.forward(1)
})
