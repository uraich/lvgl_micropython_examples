# header.py: This is the the initialization of the display and touch panel
# driver, as well as lvgl itself. It is needed for all esp32 lvgl_micropython
# programs
# I extracted this code and put it into a separate file.
# In your application you then only need the code that handles the GUI
# There is also a file trailer.py creating an endless loop, avoiding the the
# program stops.
# In order to get a working lvgl program you must prepend this code to
# you GUI code and put the trailer at the end:
# cat header.py guiCode.py trailer.py > executable.py

import sys
from time import sleep_ms
from machine import Pin,Signal,SPI
import lcd_bus
import ili9341

import i2c  # NOQA
import task_handler  # NOQA
import ft6x36  # NOQA
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
ON=const(1)
OFF=const(0)
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

# switch the backlight on
display.set_backlight(ON)
print("display: ",display)

print("Display initialized")
print("Backlight: ",display.get_backlight())

# -------------------------
# TOUCH DRIVER
# -------------------------

i2c_bus = i2c.I2C.Bus(host=0, scl=SCL, sda=SDA, freq=TS_FREQ, use_locks=False)
touch_dev = i2c.I2C.Device(bus=i2c_bus, dev_id=ft6x36.I2C_ADDR, reg_bits=ft6x36.BITS)

indev = ft6x36.FT6x36(touch_dev)

# display.set_rotation(lv.DISPLAY_ROTATION._90)        
scr = lv.screen_active()
scr.set_style_bg_color(lv.color_hex(0x000000), 0)
ddisp = lv.display_get_default()

from micropython import const
LV_ANIM_OFF = const(0)
bar1 = lv.bar(scr)
bar1.set_size(200, 20)
bar1.center()
bar1.set_value(70, LV_ANIM_OFF)

import task_handler
th = task_handler.TaskHandler()
while True:
    try:
        sleep_ms(100)
    except KeyboardInterrupt:
        break
