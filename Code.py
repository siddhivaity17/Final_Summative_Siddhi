from machine import Pin, TouchPad, PWM
import time
import neopixel

my_touch_pin = TouchPad(Pin(4))

buzzer1 = Pin(22, Pin.OUT)

my_neo = neopixel.NeoPixel(Pin(33), 16)

pb = Pin(25,Pin.IN,Pin.PULL_UP)
in1 = Pin(27,Pin.OUT)
in2 = Pin(5,Pin.OUT)
in3 = Pin(19,Pin.OUT)
in4 = Pin(12,Pin.OUT)
seq = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

count =0

while True:
    
    touch_pin_values = my_touch_pin.read()
    if touch_pin_values < 300:
         buzzer1.value(1)
         print(touch_pin_values)
         time.sleep(0.2)
    else:
        buzzer1.value(0)
        print(touch_pin_values)
        if touch_pin_values > 300:
            for _ in range(2000):
                touch_pin_values = my_touch_pin.read()
                if touch_pin_values < 300:
                    break
                    print("heeh")
                for step in seq:
                    touch_pin_values = my_touch_pin.read()
                    in1.value(step[0])
                    in2.value(step[1])
                    in3.value(step[2])
                    in4.value(step[3])
                    time.sleep(0.005)
                    touch_pin_values = my_touch_pin.read()
                    print(touch_pin_values)
                    if touch_pin_values < 300:
                        break
                         
                    val = pb.value()
                    if val ==0:
                        while True:
                            for i in range (0,16):
                                my_neo[i] = (0, 0, 255)
                                my_neo.write()
                                time.sleep(0.1)
                            for i in range (0,16):
                                my_neo[i] = (0,0,0)
                                time.sleep(0.1)
                                my_neo.write()
