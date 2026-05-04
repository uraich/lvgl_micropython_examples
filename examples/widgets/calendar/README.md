When calling evt.get_target_obj, the buttonmatrix underlying the calendar is
returned and not the calendar object. In order to get at the calendar object
itself, I pass it through the lambda function. Only like this the
get_pressed_date call is working.