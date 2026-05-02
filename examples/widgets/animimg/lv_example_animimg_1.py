from platform import platform
# Three-frame animated image
# Cycle three frames on a centered animated image widget.
# 
# An `lv_animimg` is centered on the active screen and receives an
# array of three `lv_image_dsc_t` descriptors through
# `lv_animimg_set_src`. `lv_animimg_set_duration` sets one full cycle
# to 2000 ms, `lv_animimg_set_repeat_count` uses
# `LV_ANIM_REPEAT_INFINITE`, and `lv_animimg_start` kicks the
# animation off.
 
def get_image_data(filename):
    with open(filename, 'rb') as f:
        imgdata = f.read()

    return imgdata
    
def create_img_dsc(imgdata):
    imgdsc = lv.image_dsc_t({'data_size':len(imgdata), 'data':imgdata})
    return imgdsc
    
anim_imgs = [None]*3
if "Linux" in platform():
    image_data = get_image_data("../../assets/animimg001.png")
else:
    image_data = get_image_data("images/animimg001.png")

image_data_mv = memoryview(image_data)
img_dsc = create_img_dsc(image_data_mv)
anim_imgs[0] =  img_dsc

if "Linux" in platform():
    image_data = get_image_data("../../assets/animimg002.png")
else:
    image_data = get_image_data("images/animimg002.png")
    
image_data_mv = memoryview(image_data)
img_dsc = create_img_dsc(image_data_mv)
anim_imgs[1] =  img_dsc

if "Linux" in platform():
    image_data = get_image_data("../../assets/animimg003.png")
else:
    image_data = get_image_data("images/animimg003.png")
    
image_data_mv = memoryview(image_data)
img_dsc = create_img_dsc(image_data_mv)
anim_imgs[2] =  img_dsc

animimg0 = lv.animimg(scr)
animimg0.center()
animimg0.set_src(anim_imgs, 3)
animimg0.set_duration(2000)
animimg0.set_repeat_count(lv.ANIM_REPEAT_INFINITE)
animimg0.start()
