def event_handler(evt,cal):
    code = evt.get_code()

    if code == lv.EVENT.VALUE_CHANGED:
        print(type(cal))
        date = lv.calendar_date_t()
        cal.get_pressed_date(date)
        print("Clicked date: {:02d}.{:02d}.{:02d}".format(date.day, date.month, date.year))
        
calendar = lv.calendar(scr)
calendar.set_size(200, 200)
calendar.align(lv.ALIGN.CENTER, 0, 20)
calendar.add_event_cb(lambda e: event_handler(e,calendar), lv.EVENT.ALL, None)

calendar.set_today_date(2021, 2, 23)
calendar.set_month_shown(2021, 2)

# Highlight a few days
highlighted_days=[]
for i in range(3):
    highlighted_days.append(lv.calendar_date_t())

highlighted_days[0].year=2021
highlighted_days[0].month=2
highlighted_days[0].day=6

highlighted_days[1].year=2021
highlighted_days[1].month=2
highlighted_days[1].day=11

highlighted_days[2].year=2022
highlighted_days[2].month=2
highlighted_days[2].day=22

calendar.set_highlighted_dates(highlighted_days, 3)

try:
    calendar.add_header_dropdown()
except:
    calendar.add_header_arrow()


