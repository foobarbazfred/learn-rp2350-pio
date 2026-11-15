#
# test program blink LED with wait loop
#
# program ID:  1-3
# LED Blink without wait
#


import machine
from machine import Pin
import rp2

machine.freq(125_000_000)  # set 125MHz to same RP2040

STATE_MACHINE_ID=0
LED_GPIO = 1
led_pin = Pin(LED_GPIO, Pin.OUT)

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def sm_inst_blink_w_wait():
    set(pins, 1)             # PIN1 <- 1 LED ON
    # wait for 32 loops
    set(x, 0x1f)
    label('wait_loop_1')
    nop()
    jmp(x_dec, 'wait_loop_1')
    set(pins, 0)             # PIN1 <- 0
    # wait for 32 loops
    set(x, 0x1f)
    label('wait_loop_2')
    nop()
    jmp(x_dec, 'wait_loop_2')

sm_0 = rp2.StateMachine(STATE_MACHINE_ID, sm_inst_blink_w_wait, freq=2_000, set_base=led_pin)

#
# start StateMachine
#
sm_0.active(1)

#
#
#
