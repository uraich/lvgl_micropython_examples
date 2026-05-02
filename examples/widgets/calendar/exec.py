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

def event_handler(evt,cal):
    code = evt.get_code()

    if code == lv.EVENT.VALUE_CHANGED:
        print(type(cal))
        date = lv.calendar_date_t()
        cal.get_pressed_date(date)
        print("Clicked date: {:02d}.{:02d}.{:02d}".format(date.day, date.month, date.year))
        
calendar = lv.calendar(scr)
calendar.set_size(200, 200)
calendar.align(lv.ALIGN.CENTER, 0, 20)
calendar.add_event_cb(lambda e: event_handler(e,calendar), lv.EVENT.ALL, None)

calendar.set_today_date(2021, 2, 23)
calendar.set_month_shown(2021, 2)

# Highlight a few days
highlighted_days=[]
for i in range(3):
    highlighted_days.append(lv.calendar_date_t())

highlighted_days[0].year=2021
highlighted_days[0].month=2
highlighted_days[0].day=6

highlighted_days[1].year=2021
highlighted_days[1].month=2
highlighted_days[1].day=11

highlighted_days[2].year=2022
highlighted_days[2].month=2
highlighted_days[2].day=22

calendar.set_highlighted_dates(highlighted_days, 3)

try:
    calendar.add_header_dropdown()
except:
    calendar.add_header_arrow()


event_loop()
