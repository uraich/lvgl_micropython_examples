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
        image_data = get_image_data("../../assets/img_skew_strip.png")
    else:
        image_data = get_image_data("images/img_skew_strip.pn")
except:
    print("Could not find img_skew_strip.pn")
    sys.exit()
    
image_data_mv = memoryview(image_data)
img_skew_strip = create_img_dsc(image_data_mv)# Create an image from the png file

def ofs_y_anim(img, v):    
    img.set_offset_y(v)
    # print(img,v)
    
#
# Image styling and offset
#

style = lv.style_t()
style.init()
style.set_bg_color(lv.palette_main(lv.PALETTE.YELLOW))
style.set_bg_opa(lv.OPA.COVER)
style.set_image_recolor_opa(lv.OPA.COVER)
style.set_image_recolor(lv.color_black())

img = lv.image(scr)
img.add_style(style, 0)
img.set_src(img_skew_strip)
img.set_size(150, 100)
img.center()

a = lv.anim_t()
a.init()
a.set_var(img)
a.set_values(0, 100)
a.set_duration(3000)
a.set_reverse_duration(500)
a.set_repeat_count(lv.ANIM_REPEAT_INFINITE)
a.set_custom_exec_cb(lambda a,val: ofs_y_anim(img,val))
lv.anim_t.start(a)

