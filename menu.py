import os, sys, time
import tkinter as tk

def scdl_time():
    scdl_day_etr.destroy()
    scdl_day_etr.destroy()

    scdl_time_etr = tk.Entry(root, width=50)
    scdl_time_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_)

def scdl_day():
    scdl_month_etr.destry()
    scdl_month_etr.destry()

    scdl_day_etr = tk.Entry(root, width=50)
    scdl_day_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_time)

def scdl_month_():
    scdl_year_lbl.destroy()
    scdl_year_btn.destroy()
    
    scdl_month_etr = tk.Entry(root, text="", font=("", 25), width=50)
    scdl_month_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_day)

def scdl_year():
    scdl_btn.destroy()
    talk_btn.destroy()

    #scdl_year_lbl = tk.Entry(root, font=("", 25), width=20)
    #scdl_year_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_month)
    scdl_year_lbl.pack(pady=250)
    scdl_year_btn.pack()

def talk():
    print("")

def scdl_month():
    scdl_year_btn.destroy()

root = tk.Tk()

scdl_year_lbl = tk.Entry(root, font=("", 25), width=20)
scdl_year_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_month)

#root = tk.Tk()
root.title("Menu")
root.attributes("-zoomed", "1")

scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
scdl_btn.pack(pady=250)#(anchor = "n")

talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
talk_btn.pack()#(anchor = "n")

root.mainloop()

