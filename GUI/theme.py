import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from typing import Tuple, List

def close_application(win: tk.Tk):
    win.destroy()

def set_date_textbox(win: tk.Tk, value: datetime) -> DateEntry:
    text_box = DateEntry(
        win, 
        selectmode='day',
        date_pattern="dd/mm/yyyy", 
        year=value.year,
        month=value.month,
        day=value.day,
        font = ("Times New Roman", 12, "bold"),
        justify= "center"

    )
    return text_box

def select_save_path(item: ttk.Entry, value: str = None):
    if value:
        save_path = value
    else:
        save_path = filedialog.askdirectory()
        save_path = save_path.replace("/", "\\")
    item.delete(0, tk.END)
    item.insert(tk.END, save_path)

def load_credential() -> List[str]:
    list_txt = []
    for file in os.listdir("."):
        if file.endswith(".txt") and os.path.isfile(os.path.join(".", file)):
            list_txt.append(file)
    if "requirements.txt" in list_txt:
        list_txt.remove("requirements.txt")
    for file_path in list_txt:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines if line.strip()]
            lines = [line.replace('\n', '') for line in lines]
            if len(lines)>1 and (len(lines)<4):
                name_text, pw_text = lines[:2]
                url_text = lines[2] if len(lines) > 2 else ""
                return name_text, pw_text, url_text
    return "","",""

def process_theme(win: tk.Tk,
                  web_list: List[str],
                  ward_list: List[str]
                ):

    # Header
    ttk.Label(win, text = "Thuỷ thủ Bến Lức", foreground="red",
        font = ("Times New Roman", 20, "bold")).grid(column = 1, 
        row = 1, columnspan=4)
    

    # User - password
    ttk.Label(win, text = "User name:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 2, pady = 10, columnspan=2, sticky="e")
    
    ttk.Label(win, text = "Password:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 3, pady = 10, columnspan=2, sticky="e")
    
    user_name = ttk.Entry(win, font=("Times New Roman", 15), width=15)
    user_name.grid(
        column = 3, row = 2, columnspan= 2, padx=(10,0),sticky="w"
    )

    password = ttk.Entry(win, font=("Times New Roman", 15), width=15, show="*")
    password.grid(
        column = 3, row = 3, columnspan= 2, padx=(10,0), sticky="w"
    )

    # Delay - Ward - Page
    ttk.Label(win, text = "Delay",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 4)
    
    ttk.Label(win, text = "Trang",
        font = ("Times New Roman", 14, "bold")).grid(column = 2, 
        row = 4)
    
    ttk.Label(win, text = "Xã",
        font = ("Times New Roman", 14, "bold")).grid(column = 3, 
        row = 4, columnspan=2)
    
    delay = ttk.Entry(win, font=("Times New Roman", 15), width=4)
    delay.grid(
        column = 1, row = 5
    )
    delay.insert(0, "10")

    page = ttk.Combobox(win, width = 4, font=25, justify= "center", textvariable = tk.Listbox())
    page['values'] = list(range(1,4001))
    page.grid(column = 2, row = 5)
    page.current(0)

    ward = ttk.Combobox(win, width = 17, font=("Times New Roman", 15), justify= "center", textvariable = tk.Listbox(), state= "readonly")
    ward['values'] = ward_list
    ward.grid(column = 3, row = 5, columnspan= 2, padx=(10,10))
    ward.current(0)


    # Tool - path
    ttk.Label(win, text = "Web:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 6, pady=10, padx=(10,10))
    web = ttk.Combobox(win, width = 6, font=("Times New Roman", 15), justify= "center", textvariable = tk.Listbox(), state= "readonly")
    web['values'] = web_list
    web.grid(column = 2, row = 6, columnspan=3, sticky="w")
    web.current(0)

    ttk.Label(win, text = "Save:",
        font = ("Times New Roman", 14, "bold")).grid(column = 2, 
        row = 6, columnspan=3, padx=(0,60))
    path = ttk.Entry(win, font=("Times New Roman", 15), width=9)
    path.grid(
        column = 2, row = 6, sticky="e", columnspan=3, padx=(10,50)
    )
    browse_button = ttk.Button(win, text="...", width=5, command=lambda: select_save_path(item=path))
    browse_button.grid(column = 2, row = 6, sticky="e", columnspan=3, padx=(10,10))

    # Start
    run_action = tk.Button(
        win, text = "START", bg = "Green", fg="white", font = ("Times New Roman", 15, "bold"), width = 7, cursor="hand2"
    )
    run_action.grid(row=7, column=1, columnspan=4, pady=10)

    # Date now
    now = datetime.now()

    # Receive
    ttk.Label(win, text = "Ngày nhận:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 8, columnspan=4)

    re_from_val = datetime(year=now.year-1,month=1,day=1)
    re_from = set_date_textbox(win=win, value=re_from_val)
    re_from.grid(
        column = 1, columnspan=2, row = 9, padx=(10,0)
    )

    re_to_val = datetime(year=now.year,month=12,day=31)
    re_to = set_date_textbox(win=win, value=re_to_val)
    re_to.grid(
        column = 3, columnspan= 2, row = 9, padx=(10,0)
    )

    # Have result
    ttk.Label(win, text = "Ngày hẹn trả:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 10, columnspan=4)

    result_from_val = datetime(year=now.year-1,month=1,day=1)
    result_from = set_date_textbox(win=win, value=result_from_val)
    result_from.grid(
        column = 1,columnspan=2, row = 11, padx=(10,0), pady=(0,10)
    )

    result_to_val = datetime(year=now.year,month=12,day=31)
    result_to = set_date_textbox(win=win, value=result_to_val)
    result_to.grid(
        column = 3, columnspan=2, row = 11, padx=(10,0), pady=(0,10)
    )
    
    return user_name, password,delay, page, ward, web, path, run_action, re_from, re_to, result_from, result_to

