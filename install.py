from pathlib import Path
import shutil
import os

os.chdir("./src")

paths = Path(".").iterdir()

def install_dir_sub(dir_path):
    for src_path in dir_path.iterdir():
        if src_path.is_dir():
            dest_path = Path.home() / src_path
            if not dest_path.exists():
                print("Making directory", dest_path)
                dest_path.mkdir(parents = True, exist_ok = True)
            install_dir_sub(src_path)
        elif src_path.is_file():
            dest_path = Path.home() / src_path
            print("Copying", src_path, "to", dest_path)
            shutil.copy(src_path, dest_path)

install_dir_sub(Path("."))