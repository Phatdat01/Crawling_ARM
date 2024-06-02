from tkinter import ttk
from tkinter import messagebox

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
        "re_from": re_from,
        "re_to": re_to,
        "result_from": result_from,
        "result_to": result_to
    }
    if cre["name"]== "" or cre["pw"] == "":
        messagebox.showerror("Error!", "User Name or Password?")
    else:
        try:
            crawl(
                cre=cre
            )
            messagebox.showinfo("Notice!", "Done!!!")
        except:
            messagebox.showerror("Error!", "Có lỗi Xảy Ra với máy chủ web, Vui Lòng Mở Lại!")