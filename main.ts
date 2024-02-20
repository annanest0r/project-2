input.onGesture(Gesture.EightG, function on_gesture_eight_g() {
    
    time = input.runningTime()
    time += 1
})
input.onGesture(Gesture.SixG, function on_gesture_six_g() {
    
    elasped = input.runningTime() - time
    elasped = Math.idiv(elasped, 1000)
    speed = 40 / elasped
    basic.showNumber(speed)
})
let speed = 0
let elasped = 0
let time = 0
let logging = false
datalogger.setColumnTitles("x")
basic.forever(function on_forever() {
    serial.writeValue("m/s", speed)
    basic.pause(100)
})
loops.everyInterval(100, function on_every_interval() {
    if (true) {
        datalogger.log(datalogger.createCV("x", speed))
    }
    
})
