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
    set(pins, 1)             # PIN1 <- 1
    mov(x, y)                 # x <- y (0x0300)
    label('wait_loop_0')
    jmp(x_dec, 'wait_loop_0') # while x--
    set(pins, 0)             # PIN1 <- 0
    mov(x, y)                 # x <- y (0x0300)
    label('wait_loop_1')
    jmp(x_dec, 'wait_loop_1') # while x--

sm_0 = rp2.StateMachine(STATE_MACHINE_ID, sm_inst_blink_w_wait, freq=2_000, set_base=led_pin)


#
#  set value to scratch register [x] or [y] 
#
def set_to_scratch_reg(sm, x_or_y, val):
    sm.put(val)
    sm.exec("pull()")
    sm.exec(f"mov({x_or_y}, osr)")

set_to_scratch_reg(sm_0, 'y', 0x0300)


#
# start StateMachine
#
sm_0.active(1)


