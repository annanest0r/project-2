def on_gesture_eight_g():
    global time
    time = input.running_time()
    time += 1
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_gesture_six_g():
    global elasped, speed
    elasped = input.running_time() - time
    elasped = Math.idiv(elasped, 1000)
    speed = 40 / elasped
    basic.show_number(speed)
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

speed = 0
elasped = 0
time = 0
logging = False
datalogger.set_column_titles("x")

def on_forever():
    serial.write_value("m/s", speed)
    basic.pause(100)
basic.forever(on_forever)

def on_every_interval():
    if True:
        datalogger.log(datalogger.create_cv("x", speed))
loops.every_interval(100, on_every_interval)
