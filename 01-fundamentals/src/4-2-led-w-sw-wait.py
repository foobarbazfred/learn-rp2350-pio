#
# LED Turn On by Switch
# sample program ID:  4-2
# LED ON by SW , wait by WAIT Instruction

import machine
from machine import Pin
import rp2

SW_GPIO = 0
sw_pin = Pin(SW_GPIO, Pin.IN, Pin.PULL_UP)
LED_GPIO = 1
led_pin = Pin(LED_GPIO, Pin.OUT)

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def sm_inst_led_on_by_sw():
    wait(0, pin, 0)       # wait until pins[0] to L (PUSHED)
    set(pins, 1)          # LED ON
    wait(1, pin, 0)       # wait until pins[0] to H (RELEASED)
    set(pins, 0)          # LED OFF

STATE_MACHINE_ID=0
machine.freq(125_000_000)  # set 125MHz to same RP2040

# create Statemachine and code is nop
sm0 = rp2.StateMachine(STATE_MACHINE_ID, sm_inst_led_on_by_sw, in_base=sw_pin, set_base=led_pin, freq=2000)

# start StateMachine
sm0.active(1)

#
#
#

