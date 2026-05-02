global active_index_1, active_index_2
active_index_1 = 0
active_index_2 = 0

def radio_event_handler(e,cb_no):
    
    global active_index_1, active_index_2
    print("checkbox number: ",cb_no)
    cont = lv.obj.__cast__(e.get_current_target())
    act_cb = e.get_target_obj()
    
    if cb_no == 1:
        old_cb = cont.get_child(active_index_1)
    else:
        old_cb = cont.get_child(active_index_2)
        
    # Do nothing if the container was clicked
    if act_cb == cont:
        return

    old_cb.remove_state(lv.STATE.CHECKED)   # Uncheck the previous radio button
    act_cb.add_state(lv.STATE.CHECKED)      # Check the current radio button

    if cb_no == 1:
        active_index_1 = act_cb.get_index()
    else:
        active_index_2 = act_cb.get_index()

    print("Selected radio buttons: {:d}, {:d}".format(active_index_1, active_index_2))


def radiobutton_create(parent, txt):
    obj = lv.checkbox(parent)
    obj.set_text(txt)
    obj.add_flag(lv.obj.FLAG.EVENT_BUBBLE);
    obj.add_style(style_radio, lv.PART.INDICATOR)
    obj.add_style(style_radio_chk, lv.PART.INDICATOR | lv.STATE.CHECKED)

#
# Checkboxes as radio buttons
#

# The idea is to enable `LV_OBJ_FLAG_EVENT_BUBBLE` on checkboxes and process the
# `LV_EVENT_CLICKED` on the container.
# A variable is passed as event user data where the index of the active
# radiobutton is saved 

style_radio = lv.style_t()
style_radio.init()
style_radio.set_radius(lv.RADIUS_CIRCLE)

style_radio_chk = lv.style_t()
style_radio_chk.init()
style_radio_chk.set_bg_image_src(None)

cont1 = lv.obj(scr)
cont1.set_flex_flow(lv.FLEX_FLOW.COLUMN)
cont1.set_size(lv.pct(40), lv.pct(80))
cont1.add_event_cb(lambda e: radio_event_handler(e,1), lv.EVENT.CLICKED,None)

for i in range(5):
    radiobutton_create(cont1, "A {:d}".format(i))
    
# Make the first checkbox checked
cont1.get_child(0).add_state(lv.STATE.CHECKED)

cont2 = lv.obj(scr)
cont2.set_flex_flow(lv.FLEX_FLOW.COLUMN)
cont2.set_size(lv.pct(40), lv.pct(80))
cont2.set_x(lv.pct(50))
cont2.add_event_cb(lambda e: radio_event_handler(e,2), lv.EVENT.CLICKED,None)
    
for i in range(3):
    radiobutton_create(cont2, "B {:d}".format(i))

# Make the first checkbox checked
cont2.get_child(0).add_state(lv.STATE.CHECKED)
