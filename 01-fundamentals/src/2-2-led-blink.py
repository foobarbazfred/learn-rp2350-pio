#
# asm_pio .... assemble and make code of PIO program
# LED Blink without wait
# use 2 StateMachine and switch execute
# sample program ID:  2-2

import time
import machine
from machine import Pin
import rp2

LED_GPIO = 1
led_pin = Pin(LED_GPIO, Pin.OUT)

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def sm_inst_on():
    set(pins, 1)

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def sm_inst_off():
    set(pins, 0)


STATE_MACHINE_ID_ON=0
STATE_MACHINE_ID_OFF=1

machine.freq(125_000_000)  # set 125MHz to same RP2040

# create Statemachine for LED ON
sm0 = rp2.StateMachine(STATE_MACHINE_ID_ON, sm_inst_on, set_base=led_pin, freq=2000)

# create Statemachine for LED OFF
sm1 = rp2.StateMachine(STATE_MACHINE_ID_OFF, sm_inst_off, set_base=led_pin, freq=2000)

# start and stop StateMachine
while True:
    # run sm0 for on and stop
    print('sm0 to active, led on')
    sm0.active(1)
    time.sleep(1)
    sm0.active(0)
    time.sleep(1)
    print('state of gpio', led.pin.value())
    print('state of sm0', sm0.active())
    # run sm1 for off and stop
    print('sm1 to active, led off')
    sm1.active(1)
    time.sleep(1)
    sm1.active(0)
    time.sleep(1)
    print('state of gpio', led.pin.value())
    print('state of sm1', sm1.active())
