import os
import tkinter as tk

from GUI.theme import process_theme

WEB_LIST = ["chrome","edge"]
WARD_LIST = ["Thị trấn Bến Lức","xã An Thạnh","xã Bình Đức","xã Long Hiệp","xã Lương Bình", 
            "xã Lương Hòa", "xã Mỹ Yên","xã Nhựt Chánh","xã Phước Lợi","xã Tân Bửu",
            "xã Tân Hòa","xã Thạnh Đức","xã Thạnh Hòa","xã Thạnh Lợi","xã Thanh Phú"]

def app():
    win = tk.Tk()
    win.title("Thuỷ thủ Bến Lức")
    win.resizable(width=False, height=False)
    if os.path.exists("Images/icon.ico"):
        win.iconbitmap("Images/icon.ico")

    user_name, password,delay, page, ward, web, path, re_from, re_to, result_from, result_to = process_theme(
        win=win,
        web_list=WEB_LIST,
        ward_list = WARD_LIST,      
    )

    win.eval('tk::PlaceWindow . center')
    win.mainloop()