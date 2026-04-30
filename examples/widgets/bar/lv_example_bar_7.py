from micropython import const
LV_ANIM_OFF = const(0)
bar_tob = lv.bar(scr)
bar_tob.set_size(20, 180)
bar_tob.set_range(100, 0)
bar_tob.set_value(70, LV_ANIM_OFF)
bar_tob.align(lv.ALIGN.CENTER, 0, 10)

label = lv.label(scr);
label.set_text("From top to bottom")
label.align_to(bar_tob, lv.ALIGN.OUT_TOP_MID, 0, -5)
