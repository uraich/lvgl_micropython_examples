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
## Bringing up LVGL
First I downloaded Kevin Schlosser's [lvgl MicroPython](https://github.com/lvgl-micropython/lvgl_micropython) LVGL MicroPython bindings from github. Already before receiving the board I tried to compile the Unix version of it and I wrote some hello world type applications to test things.
The command: `python3 make.py unix DISPLAY=sdl_display INDEV=sdl_pointer` did what was needed and I found **lvgl_micropy_unix** which is the binary executable on my Ubuntu machine. All this was completely painless and my hello world apps worked almost immediately.
## LVGL on the esp3n28p
Following the README of Kevin's github repository I figured out that this should be the command to compile lvgl MicroPython for my board:

python3 make.py esp32 BOARD=ESP32_GENERIC_S3 BOARD_VARIANT=SPIRAM_OCT DISPLAY=ILI9341 INDEV=FT6x36 PORT=/dev/ttyACM0 deploy

and I put this command into a shell script such that I do not have to re-type it at every attempt to build the system.
When rrunning the script it crashed. The script expects the esp-idf python environment in:
~/.espressif/python_env/idf-version_env/bin but mine was in ~.virtualenvs. I have the virtualenvwrapper running on my machine and this is where the install.sh script installed its python environment on my machine. So... I modified builder/esp32.py correspondingly.
With this modification the build was successful but the program crashed when trying to flash the board. The binary is called
build/lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin

With this command I was able to flash:
esptool --chip esp32s3 -p /dev/ttyACM0 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio --flash_siz
e 8MB --flash_freq 80m --erase-all 0x0 /opt/ucc/micros/esp32/lvgl_micropython/build/lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin

Once the system was running it was time to try the hello world app on the board instead of running it in Ubuntu. First I tried a program (literaly _hello world_), print hello world on the screen. I tried to follow the structure of temp_humidity_micropython_lvgl project referenced on Kevin's github page.
# A Hello World program
I already told you about all the peripherals on the board. In order to not re-write code for all the differen pin numbers I created a pin definition file that I could include into my lvgl apps giving understandable names to each of the pins.

The screen is controlled by an ILI9341V driver chip running on 4 channel SPI

