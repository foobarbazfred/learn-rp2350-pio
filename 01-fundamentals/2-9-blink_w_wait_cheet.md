# GPIOのPinを1/0繰り返すプログラム(WAIT付き）

先ほどのプログラムではPIO内のステートマシンでWAITループを回していました。これはあくまでもご参考ですが、２つのステートマシンを交互に使って点滅させる例を示します。コード量が増えるばかりで、プログラム自体の意味はありませんが、２つのステートマシンを使って共通のGPIOを操作する例を示します。

### ON専用、OFF専用の２つのステートマシンを交互に動かす例

ソースコード：[2-1-led-blink.py](src/2-1-led-blink.py)

コード抜粋
```
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
    print('state of gpio', led_pin.value())
    print('state of sm0', sm0.active())
    # run sm1 for off and stop
    print('sm1 to active, led off')
    sm1.active(1)
    time.sleep(1)
    sm1.active(0)
    time.sleep(1)
    print('state of gpio', led_pin.value())
    print('state of sm1', sm1.active())

```

### プログラムの説明
- 本プログラムでは２つのステートマシンを交互に使ってLEDを点滅させます。
- ステートマシン０はLEDを点灯させる専用のプログラムであり、ステートマシン１はLEDを消灯させる専用のプログラムです
- MicroPythonから、ステートマシン０を起動、停止させてLEDを点灯、次にステートマシン１を起動、停止させてLEDを消灯します
- どれぐらいの間点灯させるかはMicroPythonのループ内でtime.sleep()関数で待ちを発生させて制御しています

これだけ長いコードを書くぐらいなら、わざわざPIOを使わずとも、MicroPythonだけで、led_pin.blink() でLEDの点滅が実現できますが、PIOの使い方ご参考という目的で掲載しています


