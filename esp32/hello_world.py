# hello_world.py: Basic example do demonstrate the use of the ili9341 driver
# Copyright (c) U.Raich, 26.4.2026
# This program is part of the IoT course at the University of Cape Coast, Ghana
#

import sys
from time import sleep_ms
from machine import Pin,Signal,SPI
import lcd_bus
import ili9341
import lvgl as lv
from micropython import const

import machine
try:
    from hw_es3n28p import *
except:
    print("Please make sure hw_es3n28p.py has been uploaded to /lib")
    sys.exit()

lv.init()

# display settings
_WIDTH = const(320)
_HEIGHT = const(480)
_HOST   = const(1)
_LCD_FREQ = const(40000000)
ON = const(1)
OFF = const(0)

# -------------------------
# SPI BUS
# -------------------------
spi_bus = SPI.Bus(
    host=_HOST,
    mosi=SPI_MOSI,
    miso=SPI_MISO,
    sck =SPI_SCK
)

display_bus = lcd_bus.SPIBus(
    spi_bus=spi_bus,
    freq=_LCD_FREQ,
    dc= LCD_DC,
    cs= LCD_CS,
)

# -------------------------
# DISPLAY DRIVER
# -------------------------
display = ili9341.ILI9341(
    data_bus=display_bus,
    display_width=240,
    display_height=320,
    reset_pin=None,
    backlight_pin=LCD_BL,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order= ili9341.BYTE_ORDER_BGR,    # <--- or _RGB to correct color issues
    rgb565_byte_swap=True
)
display.set_color_inversion(1)
display.set_power(True)
display.init(type=2)
display.set_rotation(lv.DISPLAY_ROTATION._90)
display.set_backlight(ON)
print("display: ",display)
print("Display initialized")

print("Backlight: ",display.get_backlight())
def event_loop():
    while lv.screen_active(): # exit when the screen is closed
        sleep_ms(5)
        lv.task_handler()
        # lcd_bus._pump_main_thread()
        
scrn = lv.screen_active()
scrn.set_style_bg_color(lv.color_hex(0xff0000), 0)
ddisp = lv.display_get_default()

# Create a white label, set its text and align it to the center
label = lv.label(scrn)
label.set_text("Hello world")
label.set_style_text_color(lv.color_hex(0x000000), lv.PART.MAIN)
scrn.set_style_bg_opa(lv.OPA.COVER,0)
label.align(lv.ALIGN.CENTER, 0, 0)

while True:
    try:
        sleep_ms(100)
    except KeyboardInterrupt:
        break
    
