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

ARCLABEL_TEXT = "I'm on an #FA7C45 ARC#! Centered with #12c2E9 C##8B68E8 O##c471ed L##B654E5 O##C84AB2 R##DB417A F##f64659 U##ff8888 L# feature!\n";

scr.set_style_bg_color(lv.color_black(), lv.PART.MAIN)

arclabel_inner = lv.arclabel(scr)
arclabel_inner.set_size(200, 200)
arclabel_inner.set_style_text_color(lv.color_white(), lv.PART.MAIN)
arclabel_inner.set_text_static(ARCLABEL_TEXT)
arclabel_inner.set_angle_start(180)
arclabel_inner.set_radius(lv.pct(80))
arclabel_inner.set_recolor(True)
arclabel_inner.set_text_vertical_align(lv.arclabel.TEXT_ALIGN.TRAILING)
arclabel_inner.set_dir(lv.arclabel.DIR.COUNTER_CLOCKWISE)
arclabel_inner.set_text_horizontal_align(lv.arclabel.TEXT_ALIGN.CENTER)
arclabel_inner.center()

arclabel_outer = lv.arclabel(scr)
arclabel_outer.set_size(200, 200)
arclabel_outer.set_style_text_letter_space(2, lv.PART.MAIN)
arclabel_outer.set_style_text_color(lv.color_hex(0x888888), lv.PART.MAIN)
arclabel_outer.set_angle_start(-180)
arclabel_outer.set_text_static(ARCLABEL_TEXT)
arclabel_outer.set_radius(lv.pct(100))
arclabel_outer.set_recolor(True)
arclabel_outer.set_text_vertical_align(lv.arclabel.TEXT_ALIGN.LEADING)
arclabel_outer.set_dir(lv.arclabel.DIR.CLOCKWISE)
arclabel_outer.set_text_horizontal_align(lv.arclabel.TEXT_ALIGN.CENTER)
arclabel_outer.center()

arclabel_slogan_1 = lv.arclabel(scr)
arclabel_slogan_1.set_size(300, 200)
arclabel_slogan_1.set_style_text_letter_space(2, lv.PART.MAIN)
arclabel_slogan_1.set_style_text_color(lv.palette_main(lv.PALETTE.AMBER), lv.PART.MAIN)
arclabel_slogan_1.set_text_static("STAY HUNGRY")
arclabel_slogan_1.set_offset(30)
arclabel_slogan_1.set_radius(150)
arclabel_slogan_1.set_recolor(True)
arclabel_slogan_1.set_text_vertical_align(lv.arclabel.TEXT_ALIGN.TRAILING)
arclabel_slogan_1.set_text_horizontal_align(lv.arclabel.TEXT_ALIGN.CENTER)
arclabel_slogan_1.set_dir(lv.arclabel.DIR.COUNTER_CLOCKWISE)
arclabel_slogan_1.center()

arclabel_slogan_2 = lv.arclabel(scr)
arclabel_slogan_2.set_size(300, 200)
arclabel_slogan_2.set_style_text_letter_space(2, lv.PART.MAIN)
arclabel_slogan_2.set_style_text_color(lv.palette_main(lv.PALETTE.AMBER), lv.PART.MAIN)
arclabel_slogan_2.set_text_static("STAY FOOLISH")
arclabel_slogan_2.set_offset(30)
arclabel_slogan_2.set_radius(150)
arclabel_slogan_2.set_angle_start(180)
arclabel_slogan_2.set_recolor(True)
arclabel_slogan_2.set_text_vertical_align(lv.arclabel.TEXT_ALIGN.TRAILING)
arclabel_slogan_2.set_text_horizontal_align(lv.arclabel.TEXT_ALIGN.CENTER)
arclabel_slogan_2.set_dir(lv.arclabel.DIR.COUNTER_CLOCKWISE)
arclabel_slogan_2.center()

arclabel_inner.set_style_text_font(lv.font_montserrat_18, lv.PART.MAIN)
arclabel_outer.set_style_text_font(lv.font_montserrat_18, lv.PART.MAIN)
'''
#if LV_FONT_MONTSERRAT_24
    lv_obj_set_style_text_font(arclabel_slogan_1, &lv_font_montserrat_24, LV_PART_MAIN);
    lv_obj_set_style_text_font(arclabel_slogan_2, &lv_font_montserrat_24, LV_PART_MAIN);
#endif
}

#endif
'''
event_loop()
