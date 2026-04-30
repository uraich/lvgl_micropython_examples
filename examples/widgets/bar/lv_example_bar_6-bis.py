from micropython import const
LV_ANIM_OFF = const(0)

MAX_VALUE = 100
MIN_VALUE = 0

# Create bar
bar = lv.bar(lv.screen_active())
bar.set_range(MIN_VALUE, MAX_VALUE)
bar.set_size(200, 20)
bar.center()

# Create label
label = lv.label(scr)
label.set_text("0")

def update_label(bar, label):
    value = bar.get_value()
    label.set_text(str(value))
    area = lv.area_t()
    bar_coords = bar.get_coords(area)
    bar_width = area.x2 - area.x1

    # approximate indicator width
    indic_width = bar_width * value // MAX_VALUE

    label_width = label.get_width()

    if indic_width > label_width + 20:
        # inside bar (right side)
        label.align_to(bar, lv.ALIGN.RIGHT_MID, -10, 0)
        label.set_style_text_color(lv.color_white(), 0)
    else:
        # outside bar
        label.align_to(bar, lv.ALIGN.OUT_RIGHT_MID, 10, 0)
        label.set_style_text_color(lv.color_black(), 0)

def anim_cb(a,v):
    bar.set_value(v, LV_ANIM_OFF)
    update_label(bar, label)


# Animation
a = lv.anim_t()
a.init()
a.set_var(bar)
a.set_values(0, 100)
a.set_duration(4000)
a.set_reverse_duration(4000)
a.set_repeat_count(lv.ANIM_REPEAT_INFINITE)
a.set_custom_exec_cb(lambda anim, val: anim_cb(anim,val))

lv.anim_t.start(a)
