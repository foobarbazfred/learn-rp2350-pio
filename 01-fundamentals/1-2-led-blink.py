#
#
# asm_pio .... assemble and make code of PIO program
# LED Blink without wait
# sample program ID:  1-2

#

import machine
from machine import Pin
import rp2

LED_GPIO = 1


led_pin = Pin(LED_GPIO, Pin.OUT)

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def sm_inst_blink():
    set(pins, 1)
    set(pins, 0)

STATE_MACHINE_ID=0

machine.freq(125_000_000)  # set 125MHz to same RP2040

# create Statemachine and code is nop
sm0 = rp2.StateMachine(STATE_MACHINE_ID, sm_inst_blink, set_base=led_pin, freq=2000)

# start StateMachine
sm0.active(1)

#
#
#



# sm0.exec("set(pins,1)")
# sm0.exec("set(pins,0)")