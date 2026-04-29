# lvgl micropython examples
[LVGL](https://github.com/lvgl) the **l**ight and **v**ersatile embedded **g**raphics **l**ibray comes with extensive documentation and a large number of [example programs](https://lvgl.io/docs/open/examples). LVGL is written in C and programs using it would normally be written in C as well. 
There is however also a Python language binding allowing it to by used with MicroPython. These bindings have been started by A. Gonnen and are now further developed by K. Schlosser. He has substantially improved these bindings. You can find the source code of MicroPython with the lvgl bindings included in the [lvgl_micropython](https://github.com/lvgl-micropython). Unfortunately the number of example programs written for the binding is rather scarse.
It is the objective of this project to port as many of the lvgl C examples to MicroPython as possible.
# An ESP32 board being able to run lvgl_micropython
Recently I bought an ESP32S3 board with a 320x240 LCD display and a touch panel from aliexpress. On their site it is named:
`ESP32-S3 Development Board Wifi Bluetooth Intelligent Display Screen 2.8 Inch TFT Module Touch Screen Type C ES3N28P ES3C28`. It comes with a complete useless user manual giving no programming information at all. I asked the seller for more information but he told me that they had none. With the help of a WEB search engine and chatGPT I was able to figure out that I had bought a LCD Wiki es3n28p board. On the [LCD Wiki page](https://www.lcdwiki.com/2.8inch_ESP32-S3_Display) I found all the information needed, including the pinouts and a circuit diagram. The CPU is a ESP32S3 with 8 MB of PSRAM and 16 MB of octal flash. In addition to the screen and touch pannel it has an audio system (microphone and speaker), a SD card holder, a RGB LED and a few more gadgets.

# Bringing up lvgl_micropython
After cloning lvgl_micropython, I first tried to compile it for Unix, such that I can easily test the programs on my PC. 
The compile command given Kevin's README worked with a flaw and in found the lvgl_micropy_unix in the build folder. I tried a few hello world type applications and everything worked well.
# LVGL on the ES3N28P
The ES3N28P came with a lvgl demo installed in flash. It proved that the board was working, but was useless otherwise. From Kevin's README I figured out that this was the compile command I should use for my system:
`python3 make.py esp32 BOARD=ESP32_GENERIC_S3 BOARD_VARIANT=SPIRAM_OCT DISPLAY=ILI9341 INDEV=FT6x36 PORT=/dev/ttyACM0 deploy`.
I created a simple shell script with the command such that I did not have to retype it at every build attempt.
When running it, the builder.esp32.py build program crashed. The problem was that the script expected the esp-idf python environment in ~/.espressif/python_env/esp-idf-version_env while install.sh in esp-idf install the virtual environment on ~/virtualenvs/esp-idf. I am runner the virtualenvwrapper on my machine. I this the reason? Anyway ... modifying builder/esp32.py allowed me to build the binary. The deploy command however failed. I therefore wrote a flash.sh script with the command (build/lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin is the name of the firmware file).
```
esptool --chip esp32s3 -p /dev/ttyACM0 -b 460800 --before default_reset --after hard_reset write_flash --flash_mode dio 
--flash_size 8MB --flash_freq 80m --erase-all 0x0 /opt/ucc/micros/esp32/lvgl_micropython/build/lvgl_micropy_ESP32_GENERIC_S3-SPIRAM_OCT-8.bin
```
This allowed me to flash my new system.

# Running a hello world application
The es3n28p has plenty of peripherals using plenty of ESP32 pins. I therefore wrote a pin allocation file giving recognizable names to each of the pins. You find it in the esp32 folder with the name hw_es3n28p.py.
Then I wrote a first hello world program, that was supposed to print "Hello World" in black letters on a red screen. This program first initialized SPI with the correct pin numbers and the creates a display_bus adding the data/cmd, chip select and bus frequency specs.
After that, the display object is created specifying horizontal and vertical pixel numbers, backlight pin ...
I followed the main.py from the temp_humidity_micropython_lvgl project, referenced on the lvgl_micropython README. When trying to initialize the display, the program crashed. In contrast to the main.py example program, display.init needs a display type to find the correct initialization data for the ili93341 chip. The init routine uses a None parameter as default, but the file name created, which should point to file with the initialization values (_ili9341_init) does not exist. Giving a type parameter of 1 or 2 helped.
I therefore called `display.init(1)`.
Now the program ran but the screen stayed black.

Looking at the driver code I found that the LCD backlight was switched off by default and must be switched on by the application.
`display.set_backlight(ON)` where ON=1. This switched the backlight on but, I still did not see anything on the screen. 

I figured out, that the flush_cb callback, copying, the graphics from the framebuffer in memory, was never called.
The task_handler was missing and must be called with `th = task_handle.TaskHandler()`. The task_handler is responsible for screen updates and for events coming from the touch panel.
This finally gave me an image on the screen but the colors were not what I expected.
# Colors
There are 3 parameters you must get right to have the correct colors: On my screen I got white instead of black text. This can be corrected with : `display.set_color_inversion(1)`. Then there are screens, which take the rgb color components in this order: r,b,g but there are others which expect b,r,g. This can be adapted with `color_space=lv.COLOR_FORMAT.RGB565` when initializing the display. 
The color is defined in rgb565 format (5 bits red, 6 bits green and 5 bits blue) which is a 16 bit number. To make sure that these 2 bytes are written in the correct order you can set `rgb565_byte_swap=True`, again in the display initalization.

# Header amd trailer files
For any program you write, you will need the same hardware initialization and an endless loop at the end of your program. I extracted these into a header.py and a trailer.py file. Your application must then only provide the GUI code. In order to get a working executable you have to concatenate header.py your_program.py and trailer.py
`cat header.py your_program.py trailer.py > executable.py.


