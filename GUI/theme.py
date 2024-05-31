import os
import tkinter as tk
from tkinter import ttk
from typing import Tuple, List
from tkinter import filedialog

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
        row = 2, pady = 10, columnspan=2)
    
    ttk.Label(win, text = "Password:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 3, pady = 10, columnspan=2)
    
    user_name = ttk.Entry(win, font=("Times New Roman", 15), width=15)
    user_name.grid(
        column = 3, row = 2, columnspan= 2, padx=(10,0)
    )

    password = ttk.Entry(win, font=("Times New Roman", 15), width=15, show="*")
    password.grid(
        column = 3, row = 3, columnspan= 2, padx=(10,0)
    )

    # Delay - Ward - Page
    ttk.Label(win, text = "Delay",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 4, pady = 10)
    
    ttk.Label(win, text = "Trang",
        font = ("Times New Roman", 14, "bold")).grid(column = 2, 
        row = 4, pady = 10)
    
    ttk.Label(win, text = "Xã",
        font = ("Times New Roman", 14, "bold")).grid(column = 3, 
        row = 4, pady = 10, columnspan=2)
    
    delay = ttk.Entry(win, font=("Times New Roman", 15), width=6)
    delay.grid(
        column = 1, row = 5, padx=(10,0)
    )

    page = ttk.Combobox(win, width = 4, font=25, justify= "center", textvariable = tk.Listbox())
    page['values'] = list(range(1,4001))
    page.grid(column = 2, row = 5, pady=10)
    page.current(0)

    ward = ttk.Combobox(win, width = 17, font=("Times New Roman", 15), justify= "center", textvariable = tk.Listbox(), state= "readonly")
    ward['values'] = ward_list
    ward.grid(column = 3, row = 5, columnspan= 2, padx=(10,0))
    ward.current(0)


    # Tool - path
    ttk.Label(win, text = "Web:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 6, pady = 10, sticky="e")
    web = ttk.Entry(win, font=("Times New Roman", 15), width=5)
    web.grid(
        column = 2, row = 6, sticky="w", padx=(10,0)
    )

    ttk.Label(win, text = "Save:",
        font = ("Times New Roman", 14, "bold")).grid(column = 3, 
        row = 6, pady = 10, sticky="e")
    path = ttk.Entry(win, font=("Times New Roman", 15), width=5)
    path.grid(
        column = 4, row = 6, padx=(10,0)
    )

    # Start
    run_action = tk.Button(
        win, text = "Start", bg = "Green", font = ("Times New Roman", 15, "bold"), width = 7, cursor="hand2"
    )
    run_action.grid(row=7, column=1, columnspan=4, pady=10)

    # Receive
    ttk.Label(win, text = "Ngày nhận:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 8, columnspan=4)

    re_from = ttk.Entry(win, font=("Times New Roman", 15), width=10)
    re_from.grid(
        column = 1, columnspan=2, row = 9, padx=(10,0)
    )

    re_to = ttk.Entry(win, font=("Times New Roman", 15), width=10)
    re_to.grid(
        column = 3, columnspan= 2, row = 9, padx=(10,0)
    )

    # Have result
    ttk.Label(win, text = "Ngày hẹn trả:",
        font = ("Times New Roman", 14, "bold")).grid(column = 1, 
        row = 10, columnspan=4)

    result_from = ttk.Entry(win, font=("Times New Roman", 15), width=10)
    result_from.grid(
        column = 1,columnspan=2, row = 11, padx=(10,0), pady=(0,10)
    )

    result_to = ttk.Entry(win, font=("Times New Roman", 15), width=10)
    result_to.grid(
        column = 3, columnspan=2, row = 11, padx=(10,0), pady=(0,10)
    )