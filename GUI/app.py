import os
import tkinter as tk

from GUI.load import run
from GUI.theme import process_theme, close_application, load_credential, select_save_path

URL_PATH = "https://hcc-benluc.ictlongan.vn"
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

    user_name, password,delay, page, ward, web, path, run_action, re_from, re_to, result_from, result_to = process_theme(
        win=win,
        web_list=WEB_LIST,
        ward_list = WARD_LIST,      
    )
    name_text, pw_text, url_text = load_credential()
    if name_text:
        select_save_path(item=user_name,value=name_text)
        select_save_path(item=password,value=pw_text)
    if url_text =="":
        url_text = URL_PATH

    run_action['command'] = lambda: run(
            name=user_name.get(), pw = password.get(),
            url=url_text, web= web.get(),
            path=path.get(), ward=ward.get(),
            delay=int(delay.get()), page=int(page.get()),
            re_from= re_from.get(), re_to= re_to.get(),
            result_from= result_from.get(), result_to= result_to.get()
        )
    
    win.bind("<Alt-KeyPress-r>", lambda event: run(
            name=user_name.get(), pw = password.get(),
            url=url_text, web= web.get(),
            path=path.get(), ward=ward.get(),
            delay=int(delay.get()), page=int(page.get()),
            re_from= re_from.get(), re_to= re_to.get(),
            result_from= result_from.get(), result_to= result_to.get()
        )
    )

    win.bind("<Alt-KeyPress-q>", lambda event: close_application(win=win))
    win.eval('tk::PlaceWindow . center')
    win.mainloop()