import subprocess

completed_proc = subprocess.run(["pgrep", "-l", "rofi"])

if completed_proc.returncode == 1:
    subprocess.check_output(["eww", "open", "window-background"])

    proc = subprocess.Popen(["rofi", "-show", "drun"])
    proc.wait()

    subprocess.check_output(["eww", "close", "window-background"])