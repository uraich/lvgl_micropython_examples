# lvgl_micropython_examples
lvgl examples ported from C to MicroPython
This repository will provide an as complete as possible collection of lvgl programs for MicroPython.
It has just been started und is very much work in progress
In order to run the programs on unix you must combine header.py followed by the progran, followed by footer.py. At the top of header.py you can see, how you can make the programs executable. In my case the lvgl MicroPython Unix images resides in /opt/bin. Just make the combined program executable and you can easily run it.
## The background
Recently I bought, from aliexpress, an esp32s3 board with a 320x240 LCD screen, a touch panel, audio devices: microphone and speaker, a microSD connector and a few more gadgets on board. It comes with a PDF manual, which is ratheer useless. When asking the seller about programming information, he told me that he had none. On the aliexpress sitte, the module is sold under the name:
`ESP32-S3 Development Board Wifi Bluetooth Intelligent Display Screen 2.8 Inch TFT Module Touch Screen Type C ES3N28P ES3C28`.
Searches on the WEB with the help of chatGPT allowed me to identify the module as a [LCD Wiki ES3N28P]( https://www.lcdwiki.com/2.8inch_ESP32-S3_Display) and you can find the circuit diagram, pinout description, a (much more useful) user manual and a few more things.

Since the board has a resonably sized screen and a capacitive touch panel, it should be able to run the lvgl MicroPython kernel. Having 8 MB of octal PSRAM and 16 MB of flash, the resources should be largely sufficient.
# Bringing up LVGL
I 
