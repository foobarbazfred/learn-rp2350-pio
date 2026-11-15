#
# LED Turn On by Switch
# sample program ID:  4-1

import machine
from machine import Pin
import rp2

SW_GPIO = 0
sw_pin = Pin(SW_GPIO, Pin.IN, Pin.PULLDOWN)
LED_GPIO = 1
led_pin = Pin(LED_GPIO, Pin.OUT)

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def sm_inst_led_on_by_sw():
    mov(x, pins)
    mov(pins, x)

STATE_MACHINE_ID=0
machine.freq(125_000_000)  # set 125MHz to same RP2040

# create Statemachine and code is nop
sm0 = rp2.StateMachine(STATE_MACHINE_ID, sm_inst_blink, in_base=sw_pin, out_base=led_pin, freq=2000)

# start StateMachine
sm0.active(1)

#
#
#
