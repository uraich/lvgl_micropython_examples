#!/opt/bin/lvgl_micropy_unix

from micropython import const
import lcd_bus
import lvgl as lv
import sdl_display
import sdl_pointer
import task_handler
 
# Display configuration
_WIDTH = const(480)
_HEIGHT = const(320)
 
# Create SDL bus and framebuffer
bus = lcd_bus.SDLBus(flags=0)
buf1 = bus.allocate_framebuffer(_WIDTH * _HEIGHT * 3, 0)
 
# Initialize display
display = sdl_display.SDLDisplay(
    data_bus=bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    frame_buffer1=buf1,
    color_space=lv.COLOR_FORMAT.RGB888
)
display.init()
 
# Initialize input device
mouse = sdl_pointer.SDLPointer()
 
# Start task handler for LVGL processing
th = task_handler.TaskHandler(duration=5)
 
# Create UI elements
scrn = lv.screen_active()
scrn.set_style_bg_color(lv.color_hex(0x000000), 0)
 
slider = lv.slider(scrn)
slider.set_size(300, 25)
slider.center()

while True:
    pass
