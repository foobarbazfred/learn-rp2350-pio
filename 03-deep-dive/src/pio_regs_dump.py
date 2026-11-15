def pio_dump_regs(sm):
    sm.exec("pull()")
    isr_val = sm.get()
    print(f'ISR:{isr_val:04x}')
