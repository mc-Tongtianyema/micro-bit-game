timer = 0
hand = 0

def on_button_pressed_a():
    global timer
    timer = randint(5, 15)
    basic.show_icon(IconNames.CHESSBOARD)
    while timer > 0:
        timer += -1
        basic.pause(1000)
    basic.show_icon(IconNames.SKULL)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global hand
    hand = randint(1, 3)
    if hand == 1:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    elif hand == 2:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
