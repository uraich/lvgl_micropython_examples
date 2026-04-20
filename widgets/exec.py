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

scr = lv.screen_active()

def set_angle(obj, v):
    obj.set_value(v)

#
# Create an arc which acts as a loader.
#
# Create an Arc
arc = lv.arc(scr)
arc.set_rotation(270)
arc.set_bg_angles(0, 360)
arc.remove_style(None, lv.PART.KNOB)   # Be sure the knob is not displayed
arc.remove_flag(lv.obj.FLAG.CLICKABLE)  #To not allow adjusting by click
arc.center()

a = lv.anim_t()
a.init()
a.set_var(arc)
a.set_duration(1000)
a.set_repeat_count(lv.ANIM_REPEAT_INFINITE)    #Just for the demo
a.set_repeat_delay(500)
a.set_values(0, 100)
a.set_custom_exec_cb(lambda a,val: set_angle(arc,val))
lv.anim_t.start(a)
event_loop()
