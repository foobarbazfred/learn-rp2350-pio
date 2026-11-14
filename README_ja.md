# PIOを理解する
PIO(Programmable I/O)を理解して使いこなせるための解説をまとめたリポジトリです。

PIOは強力なハードユニットです。PIOを例えるなら、アセンブラプログラミングしかできない小さなマイコン(正確にはステートマシン)がマイコン(RP2350に複数内蔵されているようなものです。使える命令は、IN/OUT/SHIFT等、＃＃命令と限られますが、ステートマシンの動作クロックは最大150MHzです。アセンブラでプログラムを書きますので、遅延なしに１命令１クロックで動作します。
RP2350の場合、ステートマシンが12個入っています(ですので、RP2350の中に、小さなマイコンが12個入っているようなものです)。


# PIO参考資料

2021/5/16 時点で MicroPython ドキュメントに公開されている関連仕様は以下です。
- StateMachine コンストラクタ https://micropython-docs-ja.readthedocs.io/ja/latest/library/rp2.StateMachine.html#class-statemachine-access-to-the-rp2040-s-programmable-i-o-interface
- PIO クラス https://micropython-docs-ja.readthedocs.io/ja/latest/library/rp2.PIO.html
- PIO アセンブラ (asm_pio) https://micropython-docs-ja.readthedocs.io/ja/latest/library/rp2.html?highlight=pio_asm#pio-related-functions
- PIO アセンブリ言語命令 https://micropython-docs-ja.readthedocs.io/ja/latest/library/rp2.html#pio-assembly-language-instructions
- PIO サンプルコード(公式) https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio
- RP2350 仕様概要 https://www.raspberrypi.com/documentation/microcontrollers/microcontroller-chips.html#rp2350
- RP2350 Data Sheet https://pip.raspberrypi.com/documents/RP-008373-DS
