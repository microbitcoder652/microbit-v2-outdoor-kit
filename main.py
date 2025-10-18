def on_button_pressed_a():
    for index in range(1):
        music.play(music.string_playable("G B A G C5 B A B ", 120),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_icon(IconNames.HEART)
        basic.pause(500)
        basic.show_icon(IconNames.SMALL_HEART)
        basic.pause(500)
        basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global steps
    for countdown_numbers in range(3):
        music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_number(3 - countdown_numbers)
    music.play(music.tone_playable(392, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_string("GO!")
    steps = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global steps
    steps += 1
    basic.show_number(steps)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    record.set_mic_gain(record.AudioLevels.MEDIUM)
    record.start_recording(record.BlockingState.BLOCKING)
    if True:
        record.play_audio(record.BlockingState.BLOCKING)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

steps = 0
music.set_built_in_speaker_enabled(True)
music.play(music.string_playable("G B A G C5 B A B ", 120),
    music.PlaybackMode.IN_BACKGROUND)
basic.show_string("Hello")
