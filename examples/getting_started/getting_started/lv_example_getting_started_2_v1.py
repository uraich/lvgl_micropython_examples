global cnt
cnt = 0

def btn_event_cb(evt):
    global cnt
    code = evt.get_code()
    btn = evt.get_target_obj()

    if code == lv.EVENT.CLICKED:
        cnt += 1
        label = btn.get_child(0)
        label.set_text("Button: {:d}".format(cnt))

btn = lv.button(scr)
btn.set_pos(10,10)
btn.set_size(120,50)
btn.add_event_cb(btn_event_cb,lv.EVENT.ALL, None)
label = lv.label(btn)
label.set_text("Button")
btn.center()
