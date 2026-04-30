#!/opt/bin/lvgl_micropy_unix
from micropython import const  # NOQA
import lcd_bus  # NOQA
import time

_WIDTH = const(480)
_HEIGHT = const(320)

bus = lcd_bus.SDLBus(flags=0)

buf1 = bus.allocate_framebuffer(_WIDTH * _HEIGHT * 3, 0)


import lvgl as lv  # NOQA
import sdl_display  # NOQA

def event_loop():
    while lv.screen_active(): # exit when the screen is closed
        time.sleep_ms(5)
        lcd_bus._pump_main_thread()
        
display = sdl_display.SDLDisplay(
    data_bus=bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    color_byte_order=sdl_display.BYTE_ORDER_BGR,
    frame_buffer1=buf1,
    color_space=lv.COLOR_FORMAT.RGB888
)
display.init()

import sdl_pointer
import task_handler

mouse = sdl_pointer.SDLPointer()

# the duration needs to be set to 5 to have a good response from the mouse.
# There is a thread that runs that facilitates double buffering. 
th = task_handler.TaskHandler(duration=5)

scr = lv.screen_active()

from micropython import const
LV_ANIM_OFF = const(0)
bar1 = lv.bar(scr)
bar1.set_size(200, 20)
bar1.center()
bar1.set_value(70, LV_ANIM_OFF)

event_loop()
