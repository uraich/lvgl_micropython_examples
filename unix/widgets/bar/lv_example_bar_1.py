from micropython import const
LV_ANIM_OFF = const(0)
bar1 = lv.bar(scr)
bar1.set_size(200, 20)
bar1.center()
bar1.set_value(70, LV_ANIM_OFF)

