def pio_dump_regs(sm):
    sm.exec("push()")
    isr_val = sm.get()
    print(f'ISR:{isr_val:04x}')
    sm.exec("mov(isr,x)")
    x_val = sm.get()
    print(f'x:{x_val:04x}')
