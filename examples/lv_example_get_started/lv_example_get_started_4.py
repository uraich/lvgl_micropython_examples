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


def slider_event_cb(e):
    slider = e.get_target_obj()

    # Refresh the text
    label.set_text(str(slider.get_value()))

#
# Create a slider and write its value on a label.
#

# Create a slider in the center of the display
slider = lv.slider(lv.screen_active())
slider.set_width(200)                                              # Set the width
slider.center()                                                    # Align to the center of the parent (screen)
slider.add_event_cb(slider_event_cb, lv.EVENT.VALUE_CHANGED, None) # Assign an event function

# Create a label above the slider
label = lv.label(lv.screen_active())
label.set_text("0")
label.align_to(slider, lv.ALIGN.OUT_TOP_MID, 0, -15)               # Align below the slider

event_loop()
