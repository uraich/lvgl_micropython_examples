from platform import platform
from micropython import const
import sys

LV_ANIM_OFF = const(0)
LV_ANIM_ON  = const(1)

def get_image_data(filename):
    with open(filename, 'rb') as f:
        imgdata = f.read()

    return imgdata
    
def create_img_dsc(imgdata):
    imgdsc = lv.image_dsc_t({'data_size':len(imgdata), 'data':imgdata})
    return imgdsc

# Use a custom image as down icon and flip it when the list is opened
try:
    if "Linux" in platform():
        image_data = get_image_data("../../assets/img_cogwheel_argb.png")
    else:
        image_data = get_image_data("images/img_cogwheel_argb.png")
except:
    print("Could not find img_cogwheel_argb.png")
    sys.exit()
    
image_data_mv = memoryview(image_data)
img_cogwheel_argb = create_img_dsc(image_data_mv)# Create an image from the png file

def create_slider(color):
    slider = lv.slider(scr)
    slider.set_range(0, 255)
    slider.set_size(10, 200);
    slider.set_style_bg_color(color, lv.PART.KNOB);
    slider.set_style_bg_color(color.darken(lv.OPA._40), lv.PART.INDICATOR)
    slider.add_event_cb(slider_event_cb, lv.EVENT.VALUE_CHANGED, None)
    return slider

def slider_event_cb(e):
    # Recolor the image based on the sliders' values
    color  = lv.color_make(red_slider.get_value(), green_slider.get_value(), blue_slider.get_value())
    intense = intense_slider.get_value()
    img1.set_style_image_recolor_opa(intense, 0)
    img1.set_style_image_recolor(color, 0)
    
#
# Demonstrate runtime image re-coloring
#
# Create 4 sliders to adjust RGB color and re-color intensity
red_slider = create_slider(lv.palette_main(lv.PALETTE.RED))
green_slider = create_slider(lv.palette_main(lv.PALETTE.GREEN))
blue_slider = create_slider(lv.palette_main(lv.PALETTE.BLUE))
intense_slider = create_slider(lv.palette_main(lv.PALETTE.GREY))

red_slider.set_value(lv.OPA._20, LV_ANIM_OFF)
green_slider.set_value(lv.OPA._90, LV_ANIM_OFF)
blue_slider.set_value(lv.OPA._60, LV_ANIM_OFF)
intense_slider.set_value(lv.OPA._50, LV_ANIM_OFF)

red_slider.align(lv.ALIGN.LEFT_MID, 25, 0)
green_slider.align_to(red_slider, lv.ALIGN.OUT_RIGHT_MID, 25, 0)
blue_slider.align_to(green_slider, lv.ALIGN.OUT_RIGHT_MID, 25, 0)
intense_slider.align_to(blue_slider, lv.ALIGN.OUT_RIGHT_MID, 25, 0)

# Now create the actual image
img1 = lv.image(scr)
img1.set_src(img_cogwheel_argb)
img1.align(lv.ALIGN.RIGHT_MID, -20, 0)

#lv.obj_send_event(intense_slider, lv.EVENT.VALUE_CHANGED, None)
intense_slider.send_event(lv.EVENT.VALUE_CHANGED, None)





