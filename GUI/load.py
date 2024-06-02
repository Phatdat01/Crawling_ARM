from tkinter import ttk
from tkinter import messagebox

from datetime import datetime

from Crawl.crawl import crawl

def run(
        name: str, pw: str, 
        url: str, web: str,
        path: str,ward: str,
        delay: int, page: int,
        re_from: str, re_to: str,
        result_from: str, result_to: str
    ):
    
    cre ={
        "name": name,
        "pw": pw,
        "url": url,
        "web": web,
        "path": path,
        "ward": ward,
        "delay": delay,
        "page": page,
        "refrom": datetime.strptime(re_from, "%d/%m/%Y"),
        "re_to": datetime.strptime(re_to, "%d/%m/%Y"),
        "result_from": datetime.strptime(result_from, "%d/%m/%Y"),
        "result_to": datetime.strptime(result_to, "%d/%m/%Y")
    }
    if cre["name"]== "" or cre["pw"] == "":
        messagebox.showerror("showerror", "User Name or Password?")
    else:
        try:
            crawl(
                cre=cre
            )
            messagebox.showinfo("Notice!", "Done!!!")
        except:
            messagebox.showerror("showerror", "Có lỗi Xảy Ra với máy chủ web, Vui Lòng Mở Lại!")