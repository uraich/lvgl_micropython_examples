def event_handler(e):

    code = e.get_code()
    obj = e.get_target_obj()
    if code == lv.EVENT.VALUE_CHANGED:
        id = obj.get_selected_button()
        txt = obj.get_button_text(id)

        print("{:s} was pressed".format(txt))

btnm_map = ["1", "2", "3", "4", "5", "\n",
            "6", "7", "8", "9", "0", "\n",
            "Action1", "Action2", ""]
              
# Numeric keypad with action row
# A 3-row button matrix with a checkable Action1 button and a checked Action2 button.
 #
 # `lv_buttonmatrix_set_map` lays out digits `1` through `0` on two rows and
 # `Action1`/`Action2` on a third, where the newline strings split the rows.
 # `Action1` is made twice as wide as `Action2` via
 # `lv_buttonmatrix_set_button_width` and marked
 # `LV_BUTTONMATRIX_CTRL_CHECKABLE`; `Action2` starts in the
 # `LV_BUTTONMATRIX_CTRL_CHECKED` state. The callback subscribes to
 # `LV_EVENT_ALL` and logs the text of the button that fired
 # `LV_EVENT_VALUE_CHANGED`.
 
btnm1 = lv.buttonmatrix(scr)
btnm1.set_map(btnm_map)
btnm1.set_button_width(10, 2)      # Make "Action1" twice as wide as "Action2"
btnm1.set_button_ctrl(10, lv.buttonmatrix.CTRL.CHECKABLE)
btnm1.set_button_ctrl(11, lv.buttonmatrix.CTRL.CHECKED)
btnm1.align(lv.ALIGN.CENTER, 0, 0)
btnm1.add_event_cb(event_handler, lv.EVENT.ALL, None)

