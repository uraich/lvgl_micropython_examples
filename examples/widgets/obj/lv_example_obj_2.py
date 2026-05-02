
def drag_event_handler(e):

    obj = e.get_target_obj()
    indev = lv.indev_active()
    
    if indev == None:
       return
    vect = lv.point_t()
    indev.get_vect(vect)

    indev.get_vect(vect)
    x = obj.get_x_aligned() + vect.x
    y = obj.get_y_aligned() + vect.y
    obj.set_pos(x, y)

# Draggable base object
# Move a `Drag me` object under the pointer using `LV_EVENT_PRESSING`.
#
# A 150 by 100 base object carries a centered `Drag me` label. An
# `LV_EVENT_PRESSING` callback reads the active input device's motion
# vector with `lv_indev_get_vect`, adds it to the object's current
# aligned position, and calls `lv_obj_set_pos` so the object follows
# the pointer as long as it is held down.

obj = lv.obj(scr)
obj.set_size(150, 100)
obj.add_event_cb(drag_event_handler, lv.EVENT.PRESSING, None)
label = lv.label(obj)
label.set_text("Drag me")
label.center()

