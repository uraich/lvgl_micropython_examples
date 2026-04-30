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

class CounterBtn():
    def __init__(self):
        self.cnt = 0
        #
        # Create a button with a label and react on click event.
        #

        btn = lv.button(lv.screen_active())                      # Add a button the current screen
        btn.set_pos(10, 10)                                      # Set its position
        btn.set_size(120, 50)                                    # Set its size
        btn.align(lv.ALIGN.CENTER,0,0)
        btn.add_event_cb(self.btn_event_cb, lv.EVENT.ALL, None)  # Assign a callback to the button
        self.label = lv.label(btn)                               # Add a label to the button
        self.label.set_text("Button")                            # Set the labels text
        self.label.center()
        
    def btn_event_cb(self,e):        
        if e.get_code() == lv.EVENT.CLICKED:
            btn = e.get_target_obj()

            self.cnt += 1
            print(self.cnt)
            # Get the first child of the button which is the label and change its text
            label = btn.get_child(0)
            label.set_text("Button: " + str(self.cnt))

counterBtn = CounterBtn()

event_loop()
