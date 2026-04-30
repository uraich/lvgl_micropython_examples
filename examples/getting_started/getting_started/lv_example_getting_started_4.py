 # Slider with live value label
 # Mirror a slider's value into a label anchored above it.
 #
 # A 200 px wide slider is centered on the active screen with a label placed
 # 15 px above it via `lv_obj_align_to` and `LV_ALIGN_OUT_TOP_MID`. An
 # `LV_EVENT_VALUE_CHANGED` callback reads `lv_slider_get_value` and rewrites
 # the label text, re-aligning it after each update.

def slider_event_cb(evt):
    slider = evt.get_target_obj()
    # Refresh the text
    value = lv.slider.get_value(slider)   # correct way
    label.set_text(str(value))            # must be string

#
# Create a slider and write its value on a label.
#
            
# Create a slider in the center of the display
slider = lv.slider(scr)
slider.set_width(200)                                              # Set the width
slider.center()                                                    # Align to the center of the parent (screen)
# slider.set_exec_cb(lambda a,val: slider_event_cb(slider,val)) # Assign an event function
slider.add_event_cb(slider_event_cb,lv.EVENT.VALUE_CHANGED,None)
# Create a label below the slider
label = lv.label(scr)
label.set_text("0")
label.align_to(slider, lv.ALIGN.OUT_TOP_MID, 0, -15)               # Align below the slider


