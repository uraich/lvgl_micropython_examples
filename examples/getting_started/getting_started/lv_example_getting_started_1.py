#
# Hello world label
# Set the screen background color and place a centered label.
# 
#  Sets the active screen's background color, creates a label with the text
#  `Hello world`, sets the screen's text color to white, and centers the
#  label on the screen.
#

scr.set_style_bg_color(lv.color_hex(0x003a57), 0)

# Create a white label, set its text and align it to the center
label = lv.label(scr)
label.set_text("Hello world")
label.set_style_text_color(lv.color_hex(0xffffff), lv.PART.MAIN)
scr.set_style_bg_opa(lv.OPA.COVER,0)
label.align(lv.ALIGN.CENTER, 0, 0)
