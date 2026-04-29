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

#
# Create styles from scratch for buttons.
#
style_btn =  lv.style_t()
style_btn_red = lv.style_t()
style_btn_pressed = lv.style_t()

# Create a simple button style
style_btn.init()
style_btn.set_radius(10)
style_btn.set_bg_opa(lv.OPA.COVER)
style_btn.set_bg_color(lv.palette_lighten(lv.PALETTE.GREY, 3))
style_btn.set_bg_grad_color(lv.palette_main(lv.PALETTE.GREY))
style_btn.set_bg_grad_dir(lv.GRAD_DIR.VER)

# Add a border
style_btn.set_border_color(lv.color_white())
style_btn.set_border_opa(lv.OPA._70)
style_btn.set_border_width(2)

# Set the text style
style_btn.set_text_color(lv.color_white())

# Create a red style. Change only some colors.
style_btn_red.init()
style_btn_red.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
style_btn_red.set_bg_grad_color(lv.palette_lighten(lv.PALETTE.BLUE, 2))

# Create a style for the pressed state.
style_btn_pressed.init()
style_btn_pressed.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
style_btn_pressed.set_bg_grad_color(lv.palette_darken(lv.PALETTE.BLUE, 3))

# Create a button and use the new styles
btn = lv.button(lv.screen_active())         # Add a button the current screen
# Remove the styles coming from the theme
# Note that size and position are also stored as style properties
# so lv_obj_remove_style_all will remove the set size and position too
btn.remove_style_all()                      # Remove the styles coming from the theme
btn.set_pos(10, 10)                         # Set its position
btn.set_size(120, 50)                       # Set its size
btn.add_style(style_btn, 0)
btn.add_style(style_btn_pressed, lv.STATE.PRESSED)

label = lv.label(btn)                       # Add a label to the button
label.set_text("Button")                    # Set the labels text
label.center()

# Create a slider in the center of the display
slider = lv.slider(lv.screen_active())
slider.set_width(200)                                              # Set the width
slider.center()                                                    # Align to the center of the parent (screen)

# Create another button and use the red style too
btn2 = lv.button(lv.screen_active())
btn2.remove_style_all()                     # Remove the styles coming from the theme
btn2.set_pos(10, 80)                        # Set its position
btn2.set_size(120, 50)                      # Set its size
btn2.add_style(style_btn, 0)
btn2.add_style(style_btn_red, 0)
btn2.add_style(style_btn_pressed, lv.STATE.PRESSED)
btn2.set_style_radius(lv.RADIUS_CIRCLE, 0)  # Add a local style

label = lv.label(btn2)                      # Add a label to the button
label.set_text("Button 2")                  # Set the labels text
label.center()

event_loop()
