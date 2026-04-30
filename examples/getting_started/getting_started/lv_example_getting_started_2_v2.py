# Button with click counter
# Increment a label on a button each time it is clicked.
#
# A button sized 120x50 is placed at position (10, 10) on the active screen
# with a centered label reading `Button`. The button subscribes to
# `LV_EVENT_ALL` and on `LV_EVENT_CLICKED` the callback updates its child
# label with `lv_label_set_text` to show an incrementing counter.
 
class BtnClass(object):
    def __init__(self):
        self.cnt = 0

        self.btn = lv.button(scr)
        self.btn.set_pos(10,10)
        self.btn.set_size(120,50)
        self.btn.add_event_cb(self.btn_event_cb,lv.EVENT.ALL, None)
        self.label = lv.label(self.btn)
        self.label.set_text("Button")
        self.btn.center()
    
    def btn_event_cb(self,evt):

        code = evt.get_code()
        btn = evt.get_target_obj()
        if code == lv.EVENT.CLICKED:
            self.cnt += 1
            label = btn.get_child(0)
            label.set_text("Button: {:d}".format(self.cnt))

button = BtnClass()
