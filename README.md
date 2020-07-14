# cuddle-vga

TinyFPGABX-powered VGA controller

literally my first verilog/fpga project so if the code looks horrible that'll be why

apio: https://github.com/FPGAwars/apio

## Usage

Grab any arbitrary 80x60 image and run imgformat.py to convert it into a format that verilog likes

Then do:

```bash
apio build
apio upload
```
