import subprocess
import sys

completed_proc = subprocess.run(["pgrep", "-l", "rofi"])

if completed_proc.returncode == 1:
    subprocess.check_output(["eww", "open", "dropdown-animation"])
    subprocess.check_output(["eww", "open", "window-background"])

    proc = subprocess.Popen(["rofi", "-show", sys.argv[1]])
    proc.wait()

    subprocess.check_output(["eww", "close", "window-background"])
    subprocess.check_output(["eww", "close", "dropdown-animation"])