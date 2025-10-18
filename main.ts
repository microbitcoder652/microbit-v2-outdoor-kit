input.onButtonPressed(Button.A, function on_button_pressed_a() {
    for (let index = 0; index < 1; index++) {
        music.play(music.stringPlayable("G B A G C5 B A B ", 120), music.PlaybackMode.InBackground)
        basic.showIcon(IconNames.Heart)
        basic.pause(500)
        basic.showIcon(IconNames.SmallHeart)
        basic.pause(500)
        basic.showNumber(input.temperature())
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    for (let countdown_numbers = 0; countdown_numbers < 3; countdown_numbers++) {
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
        basic.showNumber(3 - countdown_numbers)
    }
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.InBackground)
    basic.showString("GO!")
    steps = 0
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    steps += 1
    basic.showNumber(steps)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    record.setMicGain(record.AudioLevels.Medium)
    record.startRecording(record.BlockingState.Blocking)
    if (true) {
        record.playAudio(record.BlockingState.Blocking)
    }
    
})
let steps = 0
music.setBuiltInSpeakerEnabled(true)
music.play(music.stringPlayable("G B A G C5 B A B ", 120), music.PlaybackMode.InBackground)
basic.showString("Hello")
