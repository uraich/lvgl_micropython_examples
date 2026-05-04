from platform import platform
import sys

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

img1 = lv.image(scr)
img1.set_src(img_cogwheel_argb)
img1.align(lv.ALIGN.CENTER, 0, -20)
img1.set_size(200, 200)

img2 = lv.image(scr)
img2.set_src(lv.SYMBOL.OK + "Accept")
img2.align_to(img1, lv.ALIGN.OUT_BOTTOM_MID, 0, 20)
