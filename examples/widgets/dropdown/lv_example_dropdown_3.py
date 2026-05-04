from platform import platform
def get_image_data(filename):
    with open(filename, 'rb') as f:
        imgdata = f.read()

    return imgdata
    
def create_img_dsc(imgdata):
    imgdsc = lv.image_dsc_t({'data_size':len(imgdata), 'data':imgdata})
    return imgdsc
    
def event_cb(e):
    dropdown = e.get_target_obj()
    dropdown.get_selected_str(dropdown, buf, sizeof(buf));
    print("'%s' is selected", buf);


#
# Create a menu from a drop-down list and show some drop-down list features and styling
#
# Create a drop down list
dropdown = lv.dropdown(scr)
dropdown.align(lv.ALIGN.TOP_LEFT, 10, 10)
dropdown.set_options("New project\n"
                        "New file\n"
                        "Save\n"
                        "Save as ...\n"
                        "Open project\n"
                        "Recent projects\n"
                        "Preferences\n"
                        "Exit")

# Set a fixed text to display on the button of the drop-down list
dropdown.set_text("Menu")

# Use a custom image as down icon and flip it when the list is opened
if "Linux" in platform():
    image_data = get_image_data("../../assets/img_caret_down.png")
else:
    image_data = get_image_data("images/animimg002.png")

image_data_mv = memoryview(image_data)
img_caret_down = create_img_dsc(image_data_mv)

# LV_IMAGE_DECLARE(img_caret_down);
dropdown.set_symbol(img_caret_down)
dropdown.set_style_transform_rotation(1800, lv.PART.INDICATOR | lv.STATE.CHECKED)

# In a menu we don't need to show the last clicked item
dropdown.set_selected_highlight(False)

dropdown.add_event_cb(event_cb, lv.EVENT.VALUE_CHANGED, None)
