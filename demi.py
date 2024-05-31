import tkinter  as tk 
from tkcalendar import DateEntry
my_w = tk.Tk()
my_w.geometry("380x200")  

cal=DateEntry(my_w,date_pattern="dd/mm/yyyy")
cal.grid(row=1,column=1,padx=20)

my_w.mainloop()