import task_handler
th = task_handler.TaskHandler()
while True:
    try:
        sleep_ms(100)
    except KeyboardInterrupt:
        break
