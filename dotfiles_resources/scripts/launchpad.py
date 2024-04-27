import subprocess

proc = subprocess.check_output(["eww", "open", "window-background"])

proc = subprocess.Popen(["rofi", "-show", "drun"])
proc.wait()

proc = subprocess.check_output(["eww", "close", "window-background"])