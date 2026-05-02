
 # Base objects with and without shadow
 # Two base objects showing default styling next to a custom blue shadow.
 # 
 # Two `lv_obj` base objects are placed on the active screen. The
 # first, sized 100 by 50, uses the default theme. The second keeps
 # the default size and picks up a shared `lv_style_t` with a blue
 # 10 px shadow spread by 5 px. Both are offset from center so the
 # shadow difference is visible side by side.

obj1 = lv.obj(scr)
obj1.set_size(100, 50)
obj1.align(lv.ALIGN.CENTER, -60, -30)

style_shadow = lv.style_t()
style_shadow.init()
style_shadow.set_shadow_width(10)
style_shadow.set_shadow_spread(5)
style_shadow.set_shadow_color(lv.palette_main(lv.PALETTE.BLUE))

obj2 = lv.obj(scr)
obj2.add_style(style_shadow, 0)
obj2.align(lv.ALIGN.CENTER, 60, 30)
