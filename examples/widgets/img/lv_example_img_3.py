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

def set_angle(img, v):
    img.set_rotation(v)

def set_zoom(img, v):
    img.set_scale(v)


#
# Show transformations (zoom and rotation) using a pivot point.
#

# Now create the actual image
img = lv.image(scr)
img.set_src(img_cogwheel_argb)
img.align(lv.ALIGN.CENTER, 50, 50)
img.set_pivot(0, 0)               # Rotate around the top left corner

a1 = lv.anim_t()
a1.init()
a1.set_var(img)
a1.set_custom_exec_cb(lambda a,val: set_angle(img,val))
a1.set_values(0, 3600)
a1.set_duration(5000)
a1.set_repeat_count(lv.ANIM_REPEAT_INFINITE)
lv.anim_t.start(a1)

a2 = lv.anim_t()
a2.init()
a2.set_var(img)
a2.set_custom_exec_cb(lambda a,val: set_zoom(img,val))
a2.set_values(128, 256)
a2.set_duration(5000)
a2.set_reverse_duration(3000)
a2.set_repeat_count(lv.ANIM_REPEAT_INFINITE)
lv.anim_t.start(a2)


