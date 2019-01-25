import os
import sys
import tkinter as tk
import json
import subprocess
import socket
import string
import random
import numpy as np
from numpy.random import *
from time import *
from datetime import datetime

def scdl_finish():
    subprocess.call("sudo rm schedule.json".split())
    subprocess.call("sudo touch schedule.json".split())
    subprocess.call("sudo chmod 777 schedule.json".split())
    write_file = open("schedule.json", "w")
    json.dump(scdl_list, write_file, indent=4)

    root.destroy()
    subprocess.call("python3 menu1.py".split())
    #scdl_finish_btn.pack_forget()
    #scdl_cancel_btn.pack_forget()

    #scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
    #scdl_btn.pack(pady=250)#(anchor = "n")

    #talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
    #talk_btn.pack()#(anchor = "n")

def scdl_cancel():
    root.destroy()
    subprocess.call("python3 menu2.py".split())

    #scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
    #scdl_btn.pack(pady=250)#(anchor = "n")

    #talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
    #talk_btn.pack()#(anchor = "n")

def scdl_mon_finish1():
    scdl_list["after"]["subject"] = "工学数理演習"

    scdl2_subject_lbl.pack_forget()
    scdl2_mon_btn1.pack_forget()
    scdl2_mon_btn2.pack_forget()
    scdl2_mon_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_mon_finish2():
    scdl_list["after"]["subject"] = "社会と工学"

    scdl2_subject_lbl.pack_forget()
    scdl2_mon_btn1.pack_forget()
    scdl2_mon_btn2.pack_forget()
    scdl2_mon_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_mon_finish3():
    scdl_list["after"]["subject"] = "電子機械設計製作"

    scdl2_subject_lbl.pack_forget()
    scdl2_mon_btn1.pack_forget()
    scdl2_mon_btn2.pack_forget()
    scdl2_mon_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_tue_finish1():
    scdl_list["after"]["subject"] = "応用数学"

    scdl2_subject_lbl.pack_forget()
    scdl2_tue_btn1.pack_forget()
    scdl2_tue_btn2.pack_forget()
    scdl2_tue_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_tue_finish2():
    scdl_list["after"]["subject"] = "電磁気学"

    scdl2_subject_lbl.pack_forget()
    scdl2_tue_btn1.pack_forget()
    scdl2_tue_btn2.pack_forget()
    scdl2_tue_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_tue_finish3():
    scdl_list["after"]["subject"] = "総合英語"

    scdl2_subject_lbl.pack_forget()
    scdl2_tue_btn1.pack_forget()
    scdl2_tue_btn2.pack_forget()
    scdl2_tue_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_wed_finish1():
    scdl_list["after"]["subject"] = "システム制御工学"

    scdl2_subject_lbl.pack_forget()
    scdl2_wed_btn1.pack_forget()
    scdl2_wed_btn2.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_wed_finish2():
    scdl_list["after"]["subject"] = "Java"

    scdl2_subject_lbl.pack_forget()
    scdl2_wed_btn1.pack_forget()
    scdl2_wed_btn2.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_thu_finish1():
    scdl_list["after"]["subject"] = "ドイツ語"

    scdl2_subject_lbl.pack_forget()
    scdl2_thu_btn1.pack_forget()
    scdl2_thu_btn2.pack_forget()
    scdl2_thu_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_thu_finish2():
    scdl_list["after"]["subject"] = "工学数理"

    scdl2_subject_lbl.pack_forget()
    scdl2_thu_btn1.pack_forget()
    scdl2_thu_btn2.pack_forget()
    scdl2_thu_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_thu_finish3():
    scdl_list["after"]["subject"] = "電子制御工学実験"

    scdl2_subject_lbl.pack_forget()
    scdl2_thu_btn1.pack_forget()
    scdl2_thu_btn2.pack_forget()
    scdl2_thu_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_fri_finish1():
    scdl_list["after"]["subject"] = "電磁気学"

    scdl2_subject_lbl.pack_forget()
    scdl2_fri_btn1.pack_forget()
    scdl2_fri_btn2.pack_forget()
    scdl2_fri_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_fri_finish2():
    scdl_list["after"]["subject"] = "文学特論"

    scdl2_subject_lbl.pack_forget()
    scdl2_fri_btn1.pack_forget()
    scdl2_fri_btn2.pack_forget()
    scdl2_fri_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_fri_finish3():
    scdl_list["after"]["subject"] = "電子機械設計製作"

    scdl2_subject_lbl.pack_forget()
    scdl2_fri_btn1.pack_forget()
    scdl2_fri_btn2.pack_forget()
    scdl2_fri_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl2_mon():
    scdl_list["after"]["dayofweek"] = "月"

    scdl2_subject_lbl.pack(pady=10)
    scdl2_mon_btn1.pack(pady=10)
    scdl2_mon_btn2.pack(pady=10)
    scdl2_mon_btn3.pack(pady=10)

def scdl2_tue():
    scdl_list["after"]["dayofweek"] = "火"

    scdl2_subject_lbl.pack(pady=10)
    scdl2_tue_btn1.pack(pady=10)
    scdl2_tue_btn2.pack(pady=10)
    scdl2_tue_btn3.pack(pady=10)

def scdl2_wed():
    scdl_list["after"]["dayofweek"] = "水"

    scdl2_subject_lbl.pack(pady=10)
    scdl2_wed_btn1.pack(pady=10)
    scdl2_wed_btn2.pack(pady=10)

def scdl2_thu():
    scdl_list["after"]["dayofweek"] = "木"

    scdl2_subject_lbl.pack(pady=10)
    scdl2_thu_btn1.pack(pady=10)
    scdl2_thu_btn2.pack(pady=10)
    scdl2_thu_btn3.pack(pady=10)

def scdl2_fri():
    scdl_list["after"]["dayofweek"] = "金"

    scdl2_subject_lbl.pack(pady=10)
    scdl2_fri_btn1.pack(pady=10)
    scdl2_fri_btn2.pack(pady=10)
    scdl2_fri_btn3.pack(pady=10)

def scdl2_dayofweek():
    scdl2_day_lbl.grid_forget()
    scdl2_day_btn1.grid_forget()
    scdl2_day_btn2.grid_forget()
    scdl2_day_btn3.grid_forget()
    scdl2_day_btn4.grid_forget()
    scdl2_day_btn5.grid_forget()
    scdl2_day_btn6.grid_forget()
    scdl2_day_btn7.grid_forget()
    scdl2_day_btn8.grid_forget()
    scdl2_day_btn9.grid_forget()
    scdl2_day_btn10.grid_forget()
    scdl2_day_btn11.grid_forget()
    scdl2_day_btn12.grid_forget()
    scdl2_day_btn13.grid_forget()
    scdl2_day_btn14.grid_forget()
    scdl2_day_btn15.grid_forget()
    scdl2_day_btn16.grid_forget()
    scdl2_day_btn17.grid_forget()
    scdl2_day_btn18.grid_forget()
    scdl2_day_btn19.grid_forget()
    scdl2_day_btn20.grid_forget()
    scdl2_day_btn21.grid_forget()
    scdl2_day_btn22.grid_forget()
    scdl2_day_btn23.grid_forget()
    scdl2_day_btn24.grid_forget()
    scdl2_day_btn25.grid_forget()
    scdl2_day_btn26.grid_forget()
    scdl2_day_btn27.grid_forget()
    scdl2_day_btn28.grid_forget()
    if scdl_list["after"]["month"] != "2":
        scdl2_day_btn29.grid_forget()
        scdl2_day_btn30.grid_forget()
        if scdl_list["after"]["month"] != "4" and scdl_list["after"]["month"] != "6" and scdl_list["after"]["month"] != "9" and scdl_list["after"]["month"] != "11":
            scdl2_day_btn31.grid_forget()

    after_date = "{}/{}/{}".format(scdl_list["after"]["year"], scdl_list["after"]["month"], scdl_list["after"]["day"])
    a = datetime.strptime(after_date,'%Y/%m/%d')

    if a.weekday() == 0:
        scdl2_mon()
    elif a.weekday() == 1:
        scdl2_tue()
    elif a.weekday() == 2:
        scdl2_wed()
    elif a.weekday() == 3:
        scdl2_thu()
    elif a.weekday() == 4:
        scdl2_fri()
    else:
        print("Error row:317")

def scdl2_dayofweek1():
    scdl_list["after"]["day"] = "1"
    scdl2_dayofweek()

def scdl2_dayofweek2():
    scdl_list["after"]["day"] = "2"
    scdl2_dayofweek()

def scdl2_dayofweek3():
    scdl_list["after"]["day"] = "3"
    scdl2_dayofweek()

def scdl2_dayofweek4():
    scdl_list["after"]["day"] = "4"
    scdl2_dayofweek()

def scdl2_dayofweek5():
    scdl_list["after"]["day"] = "5"
    scdl2_dayofweek()

def scdl2_dayofweek6():
    scdl_list["after"]["day"] = "6"
    scdl2_dayofweek()

def scdl2_dayofweek7():
    scdl_list["after"]["day"] = "7"
    scdl2_dayofweek()

def scdl2_dayofweek8():
    scdl_list["after"]["day"] = "8"
    scdl2_dayofweek()

def scdl2_dayofweek9():
    scdl_list["after"]["day"] = "9"
    scdl2_dayofweek()

def scdl2_dayofweek10():
    scdl_list["after"]["day"] = "10"
    scdl2_dayofweek()

def scdl2_dayofweek11():
    scdl_list["after"]["day"] = "11"
    scdl2_dayofweek()

def scdl2_dayofweek12():
    scdl_list["after"]["day"] = "12"
    scdl2_dayofweek()

def scdl2_dayofweek13():
    scdl_list["after"]["day"] = "13"
    scdl2_dayofweek()

def scdl2_dayofweek14():
    scdl_list["after"]["day"] = "14"
    scdl2_dayofweek()

def scdl2_dayofweek15():
    scdl_list["after"]["day"] = "15"
    scdl2_dayofweek()

def scdl2_dayofweek16():
    scdl_list["after"]["day"] = "16"
    scdl2_dayofweek()

def scdl2_dayofweek17():
    scdl_list["after"]["day"] = "17"
    scdl2_dayofweek()

def scdl2_dayofweek18():
    scdl_list["after"]["day"] = "18"
    scdl2_dayofweek()

def scdl2_dayofweek19():
    scdl_list["after"]["day"] = "19"
    scdl2_dayofweek()

def scdl2_dayofweek20():
    scdl_list["after"]["day"] = "20"
    scdl2_dayofweek()

def scdl2_dayofweek21():
    scdl_list["after"]["day"] = "21"
    scdl2_dayofweek()

def scdl2_dayofweek22():
    scdl_list["after"]["day"] = "22"
    scdl2_dayofweek()

def scdl2_dayofweek23():
    scdl_list["after"]["day"] = "23"
    scdl2_dayofweek()

def scdl2_dayofweek24():
    scdl_list["after"]["day"] = "24"
    scdl2_dayofweek()

def scdl2_dayofweek25():
    scdl_list["after"]["day"] = "25"
    scdl2_dayofweek()

def scdl2_dayofweek26():
    scdl_list["after"]["day"] = "26"
    scdl2_dayofweek()

def scdl2_dayofweek27():
    scdl_list["after"]["day"] = "27"
    scdl2_dayofweek()

def scdl2_dayofweek28():
    scdl_list["after"]["day"] = "28"
    scdl2_dayofweek()

def scdl2_dayofweek29():
    scdl_list["after"]["day"] = "29"
    scdl2_dayofweek()

def scdl2_dayofweek30():
    scdl_list["after"]["day"] = "30"
    scdl2_dayofweek()

def scdl2_dayofweek31():
    scdl_list["after"]["day"] = "31"
    scdl2_dayofweek()

def scdl2_day1():
    scdl_list["after"]["month"] = "1"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)
    scdl2_day_btn31.grid(column=2, row=11)

def scdl2_day2():
    scdl_list["after"]["month"] = "2"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)

def scdl2_day3():
    scdl_list["after"]["month"] = "3"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)
    scdl2_day_btn31.grid(column=2, row=11)

def scdl2_day4():
    scdl_list["after"]["month"] = "4"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)

def scdl2_day5():
    scdl_list["after"]["month"] = "5"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)
    scdl2_day_btn31.grid(column=2, row=11)

def scdl2_day6():
    scdl_list["after"]["month"] = "6"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)

def scdl2_day7():
    scdl_list["after"]["month"] = "7"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)
    scdl2_day_btn31.grid(column=2, row=11)

def scdl2_day8():
    scdl_list["after"]["month"] = "8"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)
    scdl2_day_btn31.grid(column=2, row=11)

def scdl2_day9():
    scdl_list["after"]["month"] = "9"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)

def scdl2_day10():
    scdl_list["after"]["month"] = "10"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)
    scdl2_day_btn31.grid(column=2, row=11)

def scdl2_day11():
    scdl_list["after"]["month"] = "11"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)

def scdl2_day12():
    scdl_list["after"]["month"] = "12"

    scdl2_month_lbl.pack_forget()
    scdl2_month_btn1.pack_forget()
    scdl2_month_btn2.pack_forget()
    scdl2_month_btn3.pack_forget()
    scdl2_month_btn4.pack_forget()
    scdl2_month_btn5.pack_forget()
    scdl2_month_btn6.pack_forget()
    scdl2_month_btn7.pack_forget()
    scdl2_month_btn8.pack_forget()
    scdl2_month_btn9.pack_forget()
    scdl2_month_btn10.pack_forget()
    scdl2_month_btn11.pack_forget()
    scdl2_month_btn12.pack_forget()

    scdl2_day_lbl.grid(column=1, row=0)
    scdl2_day_btn1.grid(column=0, row=1)
    scdl2_day_btn2.grid(column=0, row=2)
    scdl2_day_btn3.grid(column=0, row=3)
    scdl2_day_btn4.grid(column=0, row=4)
    scdl2_day_btn5.grid(column=0, row=5)
    scdl2_day_btn6.grid(column=0, row=6)
    scdl2_day_btn7.grid(column=0, row=7)
    scdl2_day_btn8.grid(column=0, row=8)
    scdl2_day_btn9.grid(column=0, row=9)
    scdl2_day_btn10.grid(column=0, row=10)
    scdl2_day_btn11.grid(column=1, row=1)
    scdl2_day_btn12.grid(column=1, row=2)
    scdl2_day_btn13.grid(column=1, row=3)
    scdl2_day_btn14.grid(column=1, row=4)
    scdl2_day_btn15.grid(column=1, row=5)
    scdl2_day_btn16.grid(column=1, row=6)
    scdl2_day_btn17.grid(column=1, row=7)
    scdl2_day_btn18.grid(column=1, row=8)
    scdl2_day_btn19.grid(column=1, row=9)
    scdl2_day_btn20.grid(column=1, row=10)
    scdl2_day_btn21.grid(column=2, row=1)
    scdl2_day_btn22.grid(column=2, row=2)
    scdl2_day_btn23.grid(column=2, row=3)
    scdl2_day_btn24.grid(column=2, row=4)
    scdl2_day_btn25.grid(column=2, row=5)
    scdl2_day_btn26.grid(column=2, row=6)
    scdl2_day_btn27.grid(column=2, row=7)
    scdl2_day_btn28.grid(column=2, row=8)
    scdl2_day_btn29.grid(column=2, row=9)
    scdl2_day_btn30.grid(column=2, row=10)
    scdl2_day_btn31.grid(column=2, row=11)

def scdl2_month2019():
    scdl_list["after"]["year"] = "2019"

    scdl2_year_lbl.pack_forget()
    scdl2_year_btn1.pack_forget()
    scdl2_year_btn2.pack_forget()

    scdl2_month_lbl.pack()
    scdl2_month_btn1.pack()
    scdl2_month_btn2.pack()
    scdl2_month_btn3.pack()
    scdl2_month_btn4.pack()
    scdl2_month_btn5.pack()
    scdl2_month_btn6.pack()
    scdl2_month_btn7.pack()
    scdl2_month_btn8.pack()
    scdl2_month_btn9.pack()
    scdl2_month_btn10.pack()
    scdl2_month_btn11.pack()
    scdl2_month_btn12.pack()

def scdl2_month2020():
    scdl_list["after"]["year"] = "2020"

    scdl2_year_lbl.pack_forget()
    scdl2_year_btn1.pack_forget()
    scdl2_year_btn2.pack_forget()

    scdl2_month_lbl.pack()
    scdl2_month_btn1.pack()
    scdl2_month_btn2.pack()
    scdl2_month_btn3.pack()
    scdl2_month_btn4.pack()
    scdl2_month_btn5.pack()
    scdl2_month_btn6.pack()
    scdl2_month_btn7.pack()
    scdl2_month_btn8.pack()
    scdl2_month_btn9.pack()
    scdl2_month_btn10.pack()
    scdl2_month_btn11.pack()
    scdl2_month_btn12.pack()

def scdl2_year_mon1():
    scdl_list["before"]["subject"] = "工学数理演習"

    scdl_subject_lbl.pack_forget()
    scdl_mon_btn1.pack_forget()
    scdl_mon_btn2.pack_forget()
    scdl_mon_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_mon2():
    scdl_list["before"]["subject"] = "社会と工学"

    scdl_subject_lbl.pack_forget()
    scdl_mon_btn1.pack_forget()
    scdl_mon_btn2.pack_forget()
    scdl_mon_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_mon3():
    scdl_list["before"]["subject"] = "電子機械設計製作"

    scdl_subject_lbl.pack_forget()
    scdl_mon_btn1.pack_forget()
    scdl_mon_btn2.pack_forget()
    scdl_mon_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_tue1():
    scdl_list["before"]["subject"] = "応用数学"

    scdl_subject_lbl.pack_forget()
    scdl_tue_btn1.pack_forget()
    scdl_tue_btn2.pack_forget()
    scdl_tue_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_tue2():
    scdl_list["before"]["subject"] = "電磁気学"

    scdl_subject_lbl.pack_forget()
    scdl_tue_btn1.pack_forget()
    scdl_tue_btn2.pack_forget()
    scdl_tue_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_tue3():
    scdl_list["before"]["subject"] = "総合英語"

    scdl_subject_lbl.pack_forget()
    scdl_tue_btn1.pack_forget()
    scdl_tue_btn2.pack_forget()
    scdl_tue_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_wed1():
    scdl_list["before"]["subject"] = "システム制御工学"

    scdl_subject_lbl.pack_forget()
    scdl_wed_btn1.pack_forget()
    scdl_wed_btn2.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_wed2():
    scdl_list["before"]["subject"] = "Java"

    scdl_subject_lbl.pack_forget()
    scdl_wed_btn1.pack_forget()
    scdl_wed_btn2.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_thu1():
    scdl_list["before"]["subject"] = "ドイツ語"

    scdl_subject_lbl.pack_forget()
    scdl_thu_btn1.pack_forget()
    scdl_thu_btn2.pack_forget()
    scdl_thu_btn3.pack_forget()
    scdl_thu_btn4.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_thu2():
    scdl_list["before"]["subject"] = "工学数理"

    scdl_subject_lbl.pack_forget()
    scdl_thu_btn1.pack_forget()
    scdl_thu_btn2.pack_forget()
    scdl_thu_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_thu3():
    scdl_list["before"]["subject"] = "電子制御工学実験"

    scdl_subject_lbl.pack_forget()
    scdl_thu_btn1.pack_forget()
    scdl_thu_btn2.pack_forget()
    scdl_thu_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_fri1():
    scdl_list["before"]["subject"] = "電磁気学"

    scdl_subject_lbl.pack_forget()
    scdl_fri_btn1.pack_forget()
    scdl_fri_btn2.pack_forget()
    scdl_fri_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_fri2():
    scdl_list["before"]["subject"] = "文学特論"

    scdl_subject_lbl.pack_forget()
    scdl_fri_btn1.pack_forget()
    scdl_fri_btn2.pack_forget()
    scdl_fri_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl2_year_fri3():
    scdl_list["before"]["subject"] = "電子機械設計製作"

    scdl_subject_lbl.pack_forget()
    scdl_fri_btn1.pack_forget()
    scdl_fri_btn2.pack_forget()
    scdl_fri_btn3.pack_forget()

    scdl2_year_lbl.pack(pady=10)
    scdl2_year_btn1.pack()
    scdl2_year_btn2.pack()

def scdl_mon():
    scdl_list["before"]["dayofweek"] = "月"

    scdl_subject_lbl.pack(pady=10)
    scdl_mon_btn1.pack(pady=10)
    scdl_mon_btn2.pack(pady=10)
    scdl_mon_btn3.pack(pady=10)

def scdl_tue():
    scdl_list["before"]["dayofweek"] = "火"

    scdl_subject_lbl.pack(pady=10)
    scdl_tue_btn1.pack(pady=10)
    scdl_tue_btn2.pack(pady=10)
    scdl_tue_btn3.pack(pady=10)

def scdl_wed():
    scdl_list["before"]["dayofweek"] = "水"

    scdl_subject_lbl.pack(pady=10)
    scdl_wed_btn1.pack(pady=10)
    scdl_wed_btn2.pack(pady=10)

def scdl_thu():
    scdl_list["before"]["dayofweek"] = "木"

    scdl_subject_lbl.pack(pady=10)
    scdl_thu_btn1.pack(pady=10)
    scdl_thu_btn2.pack(pady=10)
    scdl_thu_btn3.pack(pady=10)

def scdl_fri():
    scdl_list["before"]["dayofweek"] = "金"

    scdl_subject_lbl.pack(pady=10)
    scdl_fri_btn1.pack(pady=10)
    scdl_fri_btn2.pack(pady=10)
    scdl_fri_btn3.pack(pady=10)

def scdl_dayofweek():
    scdl_day_lbl.grid_forget()
    scdl_day_btn1.grid_forget()
    scdl_day_btn2.grid_forget()
    scdl_day_btn3.grid_forget()
    scdl_day_btn4.grid_forget()
    scdl_day_btn5.grid_forget()
    scdl_day_btn6.grid_forget()
    scdl_day_btn7.grid_forget()
    scdl_day_btn8.grid_forget()
    scdl_day_btn9.grid_forget()
    scdl_day_btn10.grid_forget()
    scdl_day_btn11.grid_forget()
    scdl_day_btn12.grid_forget()
    scdl_day_btn13.grid_forget()
    scdl_day_btn14.grid_forget()
    scdl_day_btn15.grid_forget()
    scdl_day_btn16.grid_forget()
    scdl_day_btn17.grid_forget()
    scdl_day_btn18.grid_forget()
    scdl_day_btn19.grid_forget()
    scdl_day_btn20.grid_forget()
    scdl_day_btn21.grid_forget()
    scdl_day_btn22.grid_forget()
    scdl_day_btn23.grid_forget()
    scdl_day_btn24.grid_forget()
    scdl_day_btn25.grid_forget()
    scdl_day_btn26.grid_forget()
    scdl_day_btn27.grid_forget()
    scdl_day_btn28.grid_forget()
    if scdl_list["before"]["month"] != "2":
        scdl_day_btn29.grid_forget()
        scdl_day_btn30.grid_forget()
        if scdl_list["before"]["month"] != "4" and scdl_list["before"]["month"] != "6" and scdl_list["before"]["month"] != "9" and scdl_list["before"]["month"] != "11":
            scdl_day_btn31.grid_forget()

    before_date = "{}/{}/{}".format(scdl_list["before"]["year"], scdl_list["before"]["month"], scdl_list["before"]["day"])
    b = datetime.strptime(before_date,'%Y/%m/%d')

    if b.weekday() == 0:
        scdl_mon()
    elif b.weekday() == 1:
        scdl_tue()
    elif b.weekday() == 2:
        scdl_wed()
    elif b.weekday() == 3:
        scdl_thu()
    elif b.weekday() == 4:
        scdl_fri()
    else:
        print("Error row:1380")

def scdl_dayofweek1():
    scdl_list["before"]["day"] = "1"
    scdl_dayofweek()

def scdl_dayofweek2():
    scdl_list["before"]["day"] = "2"
    scdl_dayofweek()

def scdl_dayofweek3():
    scdl_list["before"]["day"] = "3"
    scdl_dayofweek()

def scdl_dayofweek4():
    scdl_list["before"]["day"] = "4"
    scdl_dayofweek()

def scdl_dayofweek5():
    scdl_list["before"]["day"] = "5"
    scdl_dayofweek()

def scdl_dayofweek6():
    scdl_list["before"]["day"] = "6"
    scdl_dayofweek()

def scdl_dayofweek7():
    scdl_list["before"]["day"] = "7"
    scdl_dayofweek()

def scdl_dayofweek8():
    scdl_list["before"]["day"] = "8"
    scdl_dayofweek()

def scdl_dayofweek9():
    scdl_list["before"]["day"] = "9"
    scdl_dayofweek()

def scdl_dayofweek10():
    scdl_list["before"]["day"] = "10"
    scdl_dayofweek()

def scdl_dayofweek11():
    scdl_list["before"]["day"] = "11"
    scdl_dayofweek()

def scdl_dayofweek12():
    scdl_list["before"]["day"] = "12"
    scdl_dayofweek()

def scdl_dayofweek13():
    scdl_list["before"]["day"] = "13"
    scdl_dayofweek()

def scdl_dayofweek14():
    scdl_list["before"]["day"] = "14"
    scdl_dayofweek()

def scdl_dayofweek15():
    scdl_list["before"]["day"] = "15"
    scdl_dayofweek()

def scdl_dayofweek16():
    scdl_list["before"]["day"] = "16"
    scdl_dayofweek()

def scdl_dayofweek17():
    scdl_list["before"]["day"] = "17"
    scdl_dayofweek()

def scdl_dayofweek18():
    scdl_list["before"]["day"] = "18"
    scdl_dayofweek()

def scdl_dayofweek19():
    scdl_list["before"]["day"] = "19"
    scdl_dayofweek()

def scdl_dayofweek20():
    scdl_list["before"]["day"] = "20"
    scdl_dayofweek()

def scdl_dayofweek21():
    scdl_list["before"]["day"] = "21"
    scdl_dayofweek()

def scdl_dayofweek22():
    scdl_list["before"]["day"] = "22"
    scdl_dayofweek()

def scdl_dayofweek23():
    scdl_list["before"]["day"] = "23"
    scdl_dayofweek()

def scdl_dayofweek24():
    scdl_list["before"]["day"] = "24"
    scdl_dayofweek()

def scdl_dayofweek25():
    scdl_list["before"]["day"] = "25"
    scdl_dayofweek()

def scdl_dayofweek26():
    scdl_list["before"]["day"] = "26"
    scdl_dayofweek()

def scdl_dayofweek27():
    scdl_list["before"]["day"] = "27"
    scdl_dayofweek()

def scdl_dayofweek28():
    scdl_list["before"]["day"] = "28"
    scdl_dayofweek()

def scdl_dayofweek29():
    scdl_list["before"]["day"] = "29"
    scdl_dayofweek()

def scdl_dayofweek30():
    scdl_list["before"]["day"] = "30"
    scdl_dayofweek()

def scdl_dayofweek31():
    scdl_list["before"]["day"] = "31"
    scdl_dayofweek()

def scdl_day1():
    scdl_list["before"]["month"] = "1"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)
    scdl_day_btn31.grid(column=2, row=11)

def scdl_day2():
    scdl_list["before"]["month"] = "2"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)

def scdl_day3():
    scdl_list["before"]["month"] = "3"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)
    scdl_day_btn31.grid(column=2, row=11)

def scdl_day4():
    scdl_list["before"]["month"] = "4"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)

def scdl_day5():
    scdl_list["before"]["month"] = "5"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)
    scdl_day_btn31.grid(column=2, row=11)

def scdl_day6():
    scdl_list["before"]["month"] = "6"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)

def scdl_day7():
    scdl_list["before"]["month"] = "7"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)
    scdl_day_btn31.grid(column=2, row=11)

def scdl_day8():
    scdl_list["before"]["month"] = "8"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)
    scdl_day_btn31.grid(column=2, row=11)

def scdl_day9():
    scdl_list["before"]["month"] = "9"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)

def scdl_day10():
    scdl_list["before"]["month"] = "10"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)
    scdl_day_btn31.grid(column=2, row=11)

def scdl_day11():
    scdl_list["before"]["month"] = "11"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)

def scdl_day12():
    scdl_list["before"]["month"] = "12"

    scdl_month_lbl.pack_forget()
    scdl_month_btn1.pack_forget()
    scdl_month_btn2.pack_forget()
    scdl_month_btn3.pack_forget()
    scdl_month_btn4.pack_forget()
    scdl_month_btn5.pack_forget()
    scdl_month_btn6.pack_forget()
    scdl_month_btn7.pack_forget()
    scdl_month_btn8.pack_forget()
    scdl_month_btn9.pack_forget()
    scdl_month_btn10.pack_forget()
    scdl_month_btn11.pack_forget()
    scdl_month_btn12.pack_forget()

    scdl_day_lbl.grid(column=1, row=0)
    scdl_day_btn1.grid(column=0, row=1)
    scdl_day_btn2.grid(column=0, row=2)
    scdl_day_btn3.grid(column=0, row=3)
    scdl_day_btn4.grid(column=0, row=4)
    scdl_day_btn5.grid(column=0, row=5)
    scdl_day_btn6.grid(column=0, row=6)
    scdl_day_btn7.grid(column=0, row=7)
    scdl_day_btn8.grid(column=0, row=8)
    scdl_day_btn9.grid(column=0, row=9)
    scdl_day_btn10.grid(column=0, row=10)
    scdl_day_btn11.grid(column=1, row=1)
    scdl_day_btn12.grid(column=1, row=2)
    scdl_day_btn13.grid(column=1, row=3)
    scdl_day_btn14.grid(column=1, row=4)
    scdl_day_btn15.grid(column=1, row=5)
    scdl_day_btn16.grid(column=1, row=6)
    scdl_day_btn17.grid(column=1, row=7)
    scdl_day_btn18.grid(column=1, row=8)
    scdl_day_btn19.grid(column=1, row=9)
    scdl_day_btn20.grid(column=1, row=10)
    scdl_day_btn21.grid(column=2, row=1)
    scdl_day_btn22.grid(column=2, row=2)
    scdl_day_btn23.grid(column=2, row=3)
    scdl_day_btn24.grid(column=2, row=4)
    scdl_day_btn25.grid(column=2, row=5)
    scdl_day_btn26.grid(column=2, row=6)
    scdl_day_btn27.grid(column=2, row=7)
    scdl_day_btn28.grid(column=2, row=8)
    scdl_day_btn29.grid(column=2, row=9)
    scdl_day_btn30.grid(column=2, row=10)
    scdl_day_btn31.grid(column=2, row=11)

def scdl_month2019():
    scdl_list["before"]["year"] = "2019"

    scdl_year_lbl.pack_forget()
    scdl_year_btn1.pack_forget()
    scdl_year_btn2.pack_forget()

    scdl_month_lbl.pack()
    scdl_month_btn1.pack()
    scdl_month_btn2.pack()
    scdl_month_btn3.pack()
    scdl_month_btn4.pack()
    scdl_month_btn5.pack()
    scdl_month_btn6.pack()
    scdl_month_btn7.pack()
    scdl_month_btn8.pack()
    scdl_month_btn9.pack()
    scdl_month_btn10.pack()
    scdl_month_btn11.pack()
    scdl_month_btn12.pack()

def scdl_month2020():
    scdl_list["before"]["year"] = "2020"

    scdl_year_lbl.pack_forget()
    scdl_year_btn1.pack_forget()
    scdl_year_btn2.pack_forget()

    scdl_month_lbl.pack()
    scdl_month_btn1.pack()
    scdl_month_btn2.pack()
    scdl_month_btn3.pack()
    scdl_month_btn4.pack()
    scdl_month_btn5.pack()
    scdl_month_btn6.pack()
    scdl_month_btn7.pack()
    scdl_month_btn8.pack()
    scdl_month_btn9.pack()
    scdl_month_btn10.pack()
    scdl_month_btn11.pack()
    scdl_month_btn12.pack()

def scdl_year():
    scdl_btn.pack_forget()
    talk_btn.pack_forget()

    scdl_year_lbl.pack(pady=10)
    scdl_year_btn1.pack()
    scdl_year_btn2.pack()

def talk():
    read_file = open("schedule.json", "r")
    scdl_list = json.load(read_file)

    voice_subject_u1 = scdl_list["before"]["year"] + "年" + scdl_list["before"]["month"] + "月" + scdl_list["before"]["day"] + "日" + scdl_list["before"]["dayofweek"] + "曜日の" + scdl_list["before"]["subject"] + "が"
    voice_subject_b1 = voice_subject_u1.encode("utf-8")
    voice_subject_u2 = scdl_list["after"]["year"] + "年" + scdl_list["after"]["month"] + "月" + scdl_list["after"]["day"] + "日" + scdl_list["after"]["dayofweek"] + "曜日の" + scdl_list["after"]["subject"]
    voice_subject_b2 = voice_subject_u2.encode("utf-8")
    voice_subject_u3 = "と交換です。"
    voice_subject_b3 = voice_subject_u3.encode("utf-8")
    #voicetalk = "sudo echo '" + voice1 + "' | sudo open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./open_jtalk_tmp.wav"

    host = "localhost"
    port = 10500

    p = subprocess.Popen(["./julius_start.sh"], stdout=subprocess.PIPE, shell=True)
    pid = str(p.stdout.read().decode("utf-8"))  # juliusのプロセスIDを取得
    sleep(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    data = ""
    killword = ""

    flag = False

    while True:
        if "</RECOGOUT>\n." in data:
            #data = data + sock.recv(1024)
            strTemp = ""
            for line in data.split("\n"):
                index = line.find('WORD="')
                if index != -1:
                    line = line[index+6:line.find('"',index+6)]
                    strTemp += str(line)

                elif strTemp == "おはよう":
                    if killword != "おはよう":
                        print("Result:" + strTemp)
                        #subprocess.call("sudo echo 'あいうえお' | sudo open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./open_jtalk_tmp.wav".split())
                        #subprocess.call('aplay ./open_jtalk_tmp.wav'.split())
                        open_jtalk = ["open_jtalk"]
                        mech = ["-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic"]
                        htsvoice = ["-m", "/usr/share/hts-voice/miku/miku.htsvoice"]
                        voice_speed = ["-r", "1.0"]
                        outwav = ["-ow", "open_jtalk.wav"]
                        cmd = open_jtalk + mech + htsvoice + voice_speed + outwav
                        c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
                        c.stdin.write("おはよう".encode("utf-8"))
                        c.stdin.close()
                        c.wait()
                        aplay = ["aplay", "-q", "open_jtalk.wav"]
                        wr = subprocess.Popen(aplay)
                        killword = "おはよう"
                        flag = True

                elif strTemp == "こんにちは":
                    if killword != "こんにちは":
                        print("Result:" + strTemp)
                        #subprocess.call('echo "こんにちは" | open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./open_jtalk_tmp.wav'.split())
                        #subprocess.call('aplay ./open_jtalk_tmp.wav'.split())
                        open_jtalk = ["open_jtalk"]
                        mech = ["-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic"]
                        htsvoice = ["-m", "/usr/share/hts-voice/miku/miku.htsvoice"]
                        voice_speed = ["-r", "1.0"]
                        outwav = ["-ow", "open_jtalk.wav"]
                        cmd = open_jtalk + mech + htsvoice + voice_speed + outwav
                        c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
                        c.stdin.write("こんにちは".encode("utf-8"))
                        c.stdin.close()
                        c.wait()
                        aplay = ["aplay", "-q", "open_jtalk.wav"]
                        wr = subprocess.Popen(aplay)
                        killword = "こんにちは"
                        flag = True

                elif strTemp == "こんばんは":
                    if killword != "こんばんは":
                        print("Result:" + strTemp)
                        #subprocess.call('echo "こんばんは" | open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./open_jtalk_tmp.wav'.split())
                        #subprocess.call('aplay ./open_jtalk_tmp.wav'.split())
                        open_jtalk = ["open_jtalk"]
                        mech = ["-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic"]
                        htsvoice = ["-m", "/usr/share/hts-voice/miku/miku.htsvoice"]
                        voice_speed = ["-r", "1.0"]
                        outwav = ["-ow", "open_jtalk.wav"]
                        cmd = open_jtalk + mech + htsvoice + voice_speed + outwav
                        c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
                        c.stdin.write("こんばんは".encode("utf-8"))
                        c.stdin.close()
                        c.wait()
                        aplay = ["aplay", "-q", "open_jtalk.wav"]
                        wr = subprocess.Popen(aplay)
                        killword = "こんばんは"
                        flag = True

                elif strTemp == "よてい":
                    if killword != "よてい":
                        print("Result:" + strTemp)
                        open_jtalk = ["open_jtalk"]
                        mech = ["-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic"]
                        htsvoice = ["-m", "/usr/share/hts-voice/miku/miku.htsvoice"]
                        voice_speed = ["-r", "1.0"]
                        outwav = ["-ow", "open_jtalk.wav"]
                        cmd = open_jtalk + mech + htsvoice + voice_speed + outwav

                        c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
                        c.stdin.write(voice_subject_b1)
                        c.stdin.close()
                        c.wait()
                        aplay = ["aplay", "-q", "open_jtalk.wav"]
                        print("aplay1 start")
                        wr = subprocess.Popen(aplay)
                        print("aplay1 end")

                        print("sleep1 start")
                        sleep(4)
                        print("sleep1 end")

                        c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
                        c.stdin.write(voice_subject_b2)
                        c.stdin.close()
                        c.wait()
                        aplay = ["aplay", "-q", "open_jtalk.wav"]
                        print("aplay2 start")
                        wr = subprocess.Popen(aplay)
                        print("aplay2 end")

                        print("sleep2 start")
                        sleep(4)
                        print("sleep2 end")

                        c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
                        c.stdin.write(voice_subject_b3)
                        c.stdin.close()
                        c.wait()
                        aplay = ["aplay", "-q", "open_jtalk.wav"]
                        print("aplay3 start")
                        wr = subprocess.Popen(aplay)
                        print("aplay3 end")

                        killword = "よてい"
                        flag = True

                else:
                    wait = 0
                    if wait == 10:
                        print("")
                        wait = 0
                    else:
                        wait += 1

                data = ""

                if flag == True:
                    break
        else:
            data += str(sock.recv(1024).decode("utf-8"))

        if flag == True:
            break

scdl_list = {
    "before" : {
        "year" : "",
        "month" : "",
        "day" : "",
        "dayofweek" : "",
        "subject" : ""
    },
    "after" : {
        "year" : "",
        "month" : "",
        "day" : "",
        "dayofweek" : "",
        "subject" : ""
    }
}

# ウィンドウの生成
root = tk.Tk()
root.title("Menu")
root.attributes("-zoomed", "1")

# あとで表示するオブジェクト
scdl_finish_btn = tk.Button(root, text="編集完了", font=("", 25), command=scdl_finish)
scdl_cancel_btn = tk.Button(root, text="キャンセル", font=("", 25), command=scdl_cancel)

# after
scdl2_subject_lbl = tk.Label(root, text="教科を選んでください。", font=("", 25), width=20)

scdl2_mon_btn1 = tk.Button(root, text="工学数理演習", font=("", 25), command=scdl_mon_finish1)
scdl2_mon_btn2 = tk.Button(root, text="社会と工学", font=("", 25), command=scdl_mon_finish2)
scdl2_mon_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_mon_finish3)

scdl2_tue_btn1 = tk.Button(root, text="応用数学", font=("", 25), command=scdl_tue_finish1)
scdl2_tue_btn2 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_tue_finish2)
scdl2_tue_btn3 = tk.Button(root, text="総合英語", font=("", 25), command=scdl_tue_finish3)

scdl2_wed_btn1 = tk.Button(root, text="システム制御工学", font=("", 25), command=scdl_wed_finish1)
scdl2_wed_btn2 = tk.Button(root, text="Java", font=("", 25), command=scdl_wed_finish2)

scdl2_thu_btn1 = tk.Button(root, text="ドイツ語", font=("", 25), command=scdl_thu_finish1)
scdl2_thu_btn2 = tk.Button(root, text="工学数理", font=("", 25), command=scdl_thu_finish2)
scdl2_thu_btn3 = tk.Button(root, text="電子制御工学実験", font=("", 25), command=scdl_thu_finish3)

scdl2_fri_btn1 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_fri_finish1)
scdl2_fri_btn2 = tk.Button(root, text="文学特論", font=("", 25), command=scdl_fri_finish2)
scdl2_fri_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_fri_finish3)

scdl2_day_lbl = tk.Label(root, text="日を選んでください。", font=("", 25))
scdl2_day_btn1 = tk.Button(root, text="1日", font=("", 25), command=scdl2_dayofweek1)
scdl2_day_btn2 = tk.Button(root, text="2日", font=("", 25), command=scdl2_dayofweek2)
scdl2_day_btn3 = tk.Button(root, text="3日", font=("", 25), command=scdl2_dayofweek3)
scdl2_day_btn4 = tk.Button(root, text="4日", font=("", 25), command=scdl2_dayofweek4)
scdl2_day_btn5 = tk.Button(root, text="5日", font=("", 25), command=scdl2_dayofweek5)
scdl2_day_btn6 = tk.Button(root, text="6日", font=("", 25), command=scdl2_dayofweek6)
scdl2_day_btn7 = tk.Button(root, text="7日", font=("", 25), command=scdl2_dayofweek7)
scdl2_day_btn8 = tk.Button(root, text="8日", font=("", 25), command=scdl2_dayofweek8)
scdl2_day_btn9 = tk.Button(root, text="9日", font=("", 25), command=scdl2_dayofweek9)
scdl2_day_btn10 = tk.Button(root, text="10日", font=("", 25), command=scdl2_dayofweek10)#
scdl2_day_btn11 = tk.Button(root, text="11日", font=("", 25), command=scdl2_dayofweek11)
scdl2_day_btn12 = tk.Button(root, text="12日", font=("", 25), command=scdl2_dayofweek12)
scdl2_day_btn13 = tk.Button(root, text="13日", font=("", 25), command=scdl2_dayofweek13)
scdl2_day_btn14 = tk.Button(root, text="14日", font=("", 25), command=scdl2_dayofweek14)
scdl2_day_btn15 = tk.Button(root, text="15日", font=("", 25), command=scdl2_dayofweek15)
scdl2_day_btn16 = tk.Button(root, text="16日", font=("", 25), command=scdl2_dayofweek16)
scdl2_day_btn17 = tk.Button(root, text="17日", font=("", 25), command=scdl2_dayofweek17)
scdl2_day_btn18 = tk.Button(root, text="18日", font=("", 25), command=scdl2_dayofweek18)
scdl2_day_btn19 = tk.Button(root, text="19日", font=("", 25), command=scdl2_dayofweek19)
scdl2_day_btn20 = tk.Button(root, text="20日", font=("", 25), command=scdl2_dayofweek20)#
scdl2_day_btn21 = tk.Button(root, text="21日", font=("", 25), command=scdl2_dayofweek21)
scdl2_day_btn22 = tk.Button(root, text="22日", font=("", 25), command=scdl2_dayofweek22)
scdl2_day_btn23 = tk.Button(root, text="23日", font=("", 25), command=scdl2_dayofweek23)
scdl2_day_btn24 = tk.Button(root, text="24日", font=("", 25), command=scdl2_dayofweek24)
scdl2_day_btn25 = tk.Button(root, text="25日", font=("", 25), command=scdl2_dayofweek25)
scdl2_day_btn26 = tk.Button(root, text="26日", font=("", 25), command=scdl2_dayofweek26)
scdl2_day_btn27 = tk.Button(root, text="27日", font=("", 25), command=scdl2_dayofweek27)
scdl2_day_btn28 = tk.Button(root, text="28日", font=("", 25), command=scdl2_dayofweek28)
scdl2_day_btn29 = tk.Button(root, text="29日", font=("", 25), command=scdl2_dayofweek29)
scdl2_day_btn30 = tk.Button(root, text="30日", font=("", 25), command=scdl2_dayofweek30)#
scdl2_day_btn31 = tk.Button(root, text="31日", font=("", 25), command=scdl2_dayofweek31)

scdl2_month_lbl = tk.Label(root, text="月を選んでください。", font=("", 25))
scdl2_month_btn1 = tk.Button(root, text="1月", font=("", 25), command=scdl2_day1)
scdl2_month_btn2 = tk.Button(root, text="2月", font=("", 25), command=scdl2_day2)
scdl2_month_btn3 = tk.Button(root, text="3月", font=("", 25), command=scdl2_day3)
scdl2_month_btn4 = tk.Button(root, text="4月", font=("", 25), command=scdl2_day4)
scdl2_month_btn5 = tk.Button(root, text="5月", font=("", 25), command=scdl2_day5)
scdl2_month_btn6 = tk.Button(root, text="6月", font=("", 25), command=scdl2_day6)
scdl2_month_btn7 = tk.Button(root, text="7月", font=("", 25), command=scdl2_day7)
scdl2_month_btn8 = tk.Button(root, text="8月", font=("", 25), command=scdl2_day8)
scdl2_month_btn9 = tk.Button(root, text="9月", font=("", 25), command=scdl2_day9)
scdl2_month_btn10 = tk.Button(root, text="10月", font=("", 25), command=scdl2_day10)
scdl2_month_btn11 = tk.Button(root, text="11月", font=("", 25), command=scdl2_day11)
scdl2_month_btn12 = tk.Button(root, text="12月", font=("", 25), command=scdl2_day12)

scdl2_year_lbl = tk.Label(root, text="年を選んでください。", font=("", 25))
scdl2_year_btn1 = tk.Button(root, text="2019", font=("", 25), command=scdl2_month2019)
scdl2_year_btn2 = tk.Button(root, text="2020", font=("", 25), command=scdl2_month2020)

# before
scdl_subject_lbl = tk.Label(root, text="教科を選んでください。", font=("", 25), width=20)

scdl_mon_btn1 = tk.Button(root, text="工学数理演習", font=("", 25), command=scdl2_year_mon1)
scdl_mon_btn2 = tk.Button(root, text="社会と工学", font=("", 25), command=scdl2_year_mon2)
scdl_mon_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl2_year_mon3)

scdl_tue_btn1 = tk.Button(root, text="応用数学", font=("", 25), command=scdl2_year_tue1)
scdl_tue_btn2 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl2_year_tue2)
scdl_tue_btn3 = tk.Button(root, text="総合英語", font=("", 25), command=scdl2_year_tue3)

scdl_wed_btn1 = tk.Button(root, text="システム制御工学", font=("", 25), command=scdl2_year_wed1)
scdl_wed_btn2 = tk.Button(root, text="Java", font=("", 25), command=scdl2_year_wed2)

scdl_thu_btn1 = tk.Button(root, text="ドイツ語", font=("", 25), command=scdl2_year_thu1)
scdl_thu_btn2 = tk.Button(root, text="工学数理", font=("", 25), command=scdl2_year_thu2)
scdl_thu_btn3 = tk.Button(root, text="電子制御工学実験", font=("", 25), command=scdl2_year_thu3)

scdl_fri_btn1 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl2_year_fri1)
scdl_fri_btn2 = tk.Button(root, text="文学特論", font=("", 25), command=scdl2_year_fri2)
scdl_fri_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl2_year_fri3)

scdl_day_lbl = tk.Label(root, text="日を選んでください。", font=("", 25))
scdl_day_btn1 = tk.Button(root, text="1日", font=("", 25), command=scdl_dayofweek1)
scdl_day_btn2 = tk.Button(root, text="2日", font=("", 25), command=scdl_dayofweek2)
scdl_day_btn3 = tk.Button(root, text="3日", font=("", 25), command=scdl_dayofweek3)
scdl_day_btn4 = tk.Button(root, text="4日", font=("", 25), command=scdl_dayofweek4)
scdl_day_btn5 = tk.Button(root, text="5日", font=("", 25), command=scdl_dayofweek5)
scdl_day_btn6 = tk.Button(root, text="6日", font=("", 25), command=scdl_dayofweek6)
scdl_day_btn7 = tk.Button(root, text="7日", font=("", 25), command=scdl_dayofweek7)
scdl_day_btn8 = tk.Button(root, text="8日", font=("", 25), command=scdl_dayofweek8)
scdl_day_btn9 = tk.Button(root, text="9日", font=("", 25), command=scdl_dayofweek9)
scdl_day_btn10 = tk.Button(root, text="10日", font=("", 25), command=scdl_dayofweek10)#
scdl_day_btn11 = tk.Button(root, text="11日", font=("", 25), command=scdl_dayofweek11)
scdl_day_btn12 = tk.Button(root, text="12日", font=("", 25), command=scdl_dayofweek12)
scdl_day_btn13 = tk.Button(root, text="13日", font=("", 25), command=scdl_dayofweek13)
scdl_day_btn14 = tk.Button(root, text="14日", font=("", 25), command=scdl_dayofweek14)
scdl_day_btn15 = tk.Button(root, text="15日", font=("", 25), command=scdl_dayofweek15)
scdl_day_btn16 = tk.Button(root, text="16日", font=("", 25), command=scdl_dayofweek16)
scdl_day_btn17 = tk.Button(root, text="17日", font=("", 25), command=scdl_dayofweek17)
scdl_day_btn18 = tk.Button(root, text="18日", font=("", 25), command=scdl_dayofweek18)
scdl_day_btn19 = tk.Button(root, text="19日", font=("", 25), command=scdl_dayofweek19)
scdl_day_btn20 = tk.Button(root, text="20日", font=("", 25), command=scdl_dayofweek20)#
scdl_day_btn21 = tk.Button(root, text="21日", font=("", 25), command=scdl_dayofweek21)
scdl_day_btn22 = tk.Button(root, text="22日", font=("", 25), command=scdl_dayofweek22)
scdl_day_btn23 = tk.Button(root, text="23日", font=("", 25), command=scdl_dayofweek23)
scdl_day_btn24 = tk.Button(root, text="24日", font=("", 25), command=scdl_dayofweek24)
scdl_day_btn25 = tk.Button(root, text="25日", font=("", 25), command=scdl_dayofweek25)
scdl_day_btn26 = tk.Button(root, text="26日", font=("", 25), command=scdl_dayofweek26)
scdl_day_btn27 = tk.Button(root, text="27日", font=("", 25), command=scdl_dayofweek27)
scdl_day_btn28 = tk.Button(root, text="28日", font=("", 25), command=scdl_dayofweek28)
scdl_day_btn29 = tk.Button(root, text="29日", font=("", 25), command=scdl_dayofweek29)
scdl_day_btn30 = tk.Button(root, text="30日", font=("", 25), command=scdl_dayofweek30)#
scdl_day_btn31 = tk.Button(root, text="31日", font=("", 25), command=scdl_dayofweek31)

scdl_month_lbl = tk.Label(root, text="月を選んでください。", font=("", 25))
scdl_month_btn1 = tk.Button(root, text="1月", font=("", 25), command=scdl_day1)
scdl_month_btn2 = tk.Button(root, text="2月", font=("", 25), command=scdl_day2)
scdl_month_btn3 = tk.Button(root, text="3月", font=("", 25), command=scdl_day3)
scdl_month_btn4 = tk.Button(root, text="4月", font=("", 25), command=scdl_day4)
scdl_month_btn5 = tk.Button(root, text="5月", font=("", 25), command=scdl_day5)
scdl_month_btn6 = tk.Button(root, text="6月", font=("", 25), command=scdl_day6)
scdl_month_btn7 = tk.Button(root, text="7月", font=("", 25), command=scdl_day7)
scdl_month_btn8 = tk.Button(root, text="8月", font=("", 25), command=scdl_day8)
scdl_month_btn9 = tk.Button(root, text="9月", font=("", 25), command=scdl_day9)
scdl_month_btn10 = tk.Button(root, text="10月", font=("", 25), command=scdl_day10)
scdl_month_btn11 = tk.Button(root, text="11月", font=("", 25), command=scdl_day11)
scdl_month_btn12 = tk.Button(root, text="12月", font=("", 25), command=scdl_day12)

scdl_year_lbl = tk.Label(root, text="年を選んでください。", font=("", 25))
scdl_year_btn1 = tk.Button(root, text="2019", font=("", 25), command=scdl_month2019)
scdl_year_btn2 = tk.Button(root, text="2020", font=("", 25), command=scdl_month2020)

# 最初に表示するオブジェクト
scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
scdl_btn.pack(pady=20)
talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
talk_btn.pack()

root.mainloop()
