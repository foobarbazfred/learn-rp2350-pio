#
# tracer
# trace program for PIO Execution
# trace program by IRQ and 
#
# ProgramID: 2-99-trace.py
#

import micropython
import machine
from machine import Pin
import rp2


STATE_MACHINE_ID = 11   # max SM Number in RP2040 
machine.freq(125_000_000)  # set 125MHz to same RP2040

def intr_handler(sm):
    micropython.schedule(pio_trace, sm)


from machine import mem16
PIO0_BASE = 0x50_200_000
SM0_INSTR = 0x0d8
SM0_ADDR = 0x0d4

def pio_trace(sm):

    sm0_ctrl_addr = PIO0_BASE  + 0
    sm0_pc_addr = PIO0_BASE  + SM0_ADDR
    sm0_instr_addr = PIO0_BASE  + SM0_INSTR

    pc = mem16[sm0_pc_addr]
    inst = mem16[sm0_instr_addr]
    if mem16[sm0_ctrl_addr] & 0x01 :
        print(f'PC: {pc:02d}, INST: {inst:04x} (RUN)')
    else:
        print(f'PC: {pc:02d}, INST: {inst:04x} (STOPPED)')

@rp2.asm_pio()
def sm_inst_periodic_irq():
    irq(3)

# 
# create Statemachine and code is nop
sm_11 = rp2.StateMachine(STATE_MACHINE_ID, sm_inst_periodic_irq, freq=2000)
sm_11.irq(intr_handler)

# start trace (auto stop)

import time
def start_trace(auto_stop=True):
    sm_11.active(1)
    if auto_stop:
        time.sleep(2)
        sm_11.active(0)
        print('trace is stopped')


start_trace()
#
#
#

# stop trace
# sm_11.active(0)

#
#
#

