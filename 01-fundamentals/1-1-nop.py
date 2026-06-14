#
#
# asm_pio .... assemble and make code of PIO program
# only NOP
# sample program ID:  1-1

#
import machine
import rp2

@rp2.asm_pio()
def sm_inst_nop():
    nop()
#    nop()

STATE_MACHINE_ID=0

machine.freq(125_000_000)  # set 125MHz to same RP2040

# create Statemachine and code is nop
sm0 = rp2.StateMachine(STATE_MACHINE_ID, sm_inst_nop, freq=2000)

# start StateMachine
sm0.active(1)

#
#
#
