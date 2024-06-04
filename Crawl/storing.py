import os
import time
import shutil

def get_by_latest_file(num: int, download_path: str):
    lst= [file for file in os.listdir(download_path) if os.path.isfile(os.path.join(download_path, file)) and file.lower().endswith('.pdf')]
    sorted_files = sorted(lst, key=lambda x: os.path.getmtime(os.path.join(download_path, x)), reverse=True)
    return sorted_files[:num]

def make_dirs(target: str):
    if not os.path.exists(target):
        os.makedirs(target)
        time.sleep(0.5)

def move_to_des(root:str, ward: str, page: str, id: str, file: str):
    target = f"{root}\\\\{ward}"
    make_dirs(target=target)
    target = f"{target}\\\\{page}"
    make_dirs(target=target)
    target = f"{target}\\\\{id}"
    make_dirs(target=target)
    shutil.move(f"{root}\\\\{file}",target)