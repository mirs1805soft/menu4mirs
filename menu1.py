import os, sys, time
import tkinter as tk
import json
import subprocess
#from collections import OrderedDict

def scdl_finish():


    root.destroy()
    subprocess.call("python3 menu2.py".split())
    #scdl_finish_btn.pack_forget()
    #scdl_cancel_btn.pack_forget()

    #scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
    #scdl_btn.pack(pady=250)#(anchor = "n")

    #talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
    #talk_btn.pack()#(anchor = "n")

def scdl_cancel():
    scdl_finish_btn.pack_forget()
    scdl_cancel_btn.pack_forget()

    #scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
    scdl_btn.pack(pady=250)#(anchor = "n")

    #talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
    talk_btn.pack()#(anchor = "n")

def scdl_mon_finish1():
    scdl["before"]["subject"] = "工学数理演習"

    scdl_mon2_btn1.pack_forget()
    scdl_mon2_btn2.pack_forget()
    scdl_mon2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_mon_finish2():
    scdl["before"]["subject"] = "社会と工学"

    scdl_mon2_btn1.pack_forget()
    scdl_mon2_btn2.pack_forget()
    scdl_mon2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_mon_finish3():
    scdl["before"]["subject"] = "電子機械設計製作"

    scdl_mon2_btn1.pack_forget()
    scdl_mon2_btn2.pack_forget()
    scdl_mon2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_tue_finish1():
    scdl["before"]["subject"] = "応用数学"

    scdl_tue2_btn1.pack_forget()
    scdl_tue2_btn2.pack_forget()
    scdl_tue2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_tue_finish2():
    scdl["before"]["subject"] = "電磁気学"

    scdl_tue2_btn1.pack_forget()
    scdl_tue2_btn2.pack_forget()
    scdl_tue2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_tue_finish3():
    scdl["before"]["subject"] = "総合英語"

    scdl_tue2_btn1.pack_forget()
    scdl_tue2_btn2.pack_forget()
    scdl_tue2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_wed_finish1():
    scdl["before"]["subject"] = "システム制御工学"
    scdl_wed2_btn1.pack_forget()
    scdl_wed2_btn2.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_wed_finish2():
    scdl["before"]["subject"] = "Java"

    scdl_wed2_btn1.pack_forget()
    scdl_wed2_btn2.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_thu_finish1():
    scdl["before"]["subject"] = "ドイツ語"

    scdl_thu2_btn1.pack_forget()
    scdl_thu2_btn2.pack_forget()
    scdl_thu2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_thu_finish2():
    scdl["before"]["subject"] = "工学数理"

    scdl_thu2_btn1.pack_forget()
    scdl_thu2_btn2.pack_forget()
    scdl_thu2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_thu_finish3():
    scdl["before"]["subject"] = "電子制御工学実験"

    scdl_thu2_btn1.pack_forget()
    scdl_thu2_btn2.pack_forget()
    scdl_thu2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_fri_finish1():
    scdl["before"]["subject"] = "電磁気学"

    scdl_fri2_btn1.pack_forget()
    scdl_fri2_btn2.pack_forget()
    scdl_fri2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_fri_finish2():
    scdl["before"]["subject"] = "文学特論"

    scdl_fri2_btn1.pack_forget()
    scdl_fri2_btn2.pack_forget()
    scdl_fri2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_fri_finish3():
    scdl["before"]["subject"] = "電子機械設計製作"

    scdl_fri2_btn1.pack_forget()
    scdl_fri2_btn2.pack_forget()
    scdl_fri2_btn3.pack_forget()

    scdl_finish_btn.pack(pady=250)
    scdl_cancel_btn.pack()

def scdl_mon2():
    scdl_day2_btn_mon.pack_forget()
    scdl_day2_btn_tue.pack_forget()
    scdl_day2_btn_wed.pack_forget()
    scdl_day2_btn_thu.pack_forget()
    scdl_day2_btn_fri.pack_forget()

    scdl_mon2_btn1.pack(pady=10)
    scdl_mon2_btn2.pack(pady=10)
    scdl_mon2_btn3.pack(pady=10)

def scdl_tue2():
    scdl_day2_btn_mon.pack_forget()
    scdl_day2_btn_tue.pack_forget()
    scdl_day2_btn_wed.pack_forget()
    scdl_day2_btn_thu.pack_forget()
    scdl_day2_btn_fri.pack_forget()

    scdl_tue2_btn1.pack(pady=10)
    scdl_tue2_btn2.pack(pady=10)
    scdl_tue2_btn3.pack(pady=10)

def scdl_wed2():
    scdl_day2_btn_mon.pack_forget()
    scdl_day2_btn_tue.pack_forget()
    scdl_day2_btn_wed.pack_forget()
    scdl_day2_btn_thu.pack_forget()
    scdl_day2_btn_fri.pack_forget()

    scdl_wed2_btn1.pack(pady=10)
    scdl_wed2_btn2.pack(pady=10)

def scdl_thu2():
    scdl_day2_btn_mon.pack_forget()
    scdl_day2_btn_tue.pack_forget()
    scdl_day2_btn_wed.pack_forget()
    scdl_day2_btn_thu.pack_forget()
    scdl_day2_btn_fri.pack_forget()

    scdl_thu2_btn1.pack(pady=10)
    scdl_thu2_btn2.pack(pady=10)
    scdl_thu2_btn3.pack(pady=10)

def scdl_fri2():
    scdl_day2_btn_mon.pack_forget()
    scdl_day2_btn_tue.pack_forget()
    scdl_day2_btn_wed.pack_forget()
    scdl_day2_btn_thu.pack_forget()
    scdl_day2_btn_fri.pack_forget()

    scdl_fri2_btn1.pack(pady=10)
    scdl_fri2_btn2.pack(pady=10)
    scdl_fri2_btn3.pack(pady=10)

def scdl_dayofweek2():
    scdl_day2_etr.pack_forget()
    scdl_day2_btn.pack_forget()

    scdl_day2_btn_mon.pack(pady=10)
    scdl_day2_btn_tue.pack(pady=10)
    scdl_day2_btn_wed.pack(pady=10)
    scdl_day2_btn_thu.pack(pady=10)
    scdl_day2_btn_fri.pack(pady=10)

def scdl_day2():
    scdl_month2_etr.pack_forget()
    scdl_month2_btn.pack_forget()

    scdl_day2_etr.pack(pady=250)
    scdl_day2_btn.pack()

def scdl_month2():
    scdl_year2_lbl.pack_forget()
    scdl_year2_btn.pack_forget()

    scdl_month2_etr.pack(pady=250)
    scdl_month2_btn.pack()

def scdl_year2_mon1():
    scdl["before"]["subject"] = "工学数理演習"

    scdl_mon2_btn1.pack_forget()
    scdl_mon2_btn2.pack_forget()
    scdl_mon2_btn3.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_mon2():
    scdl["before"]["subject"] = "社会と工学"

    scdl_mon2_btn1.pack_forget()
    scdl_mon2_btn2.pack_forget()
    scdl_mon2_btn3.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_mon3():
    scdl["before"]["subject"] = "電子機械設計製作"

    scdl_mon2_btn1.pack_forget()
    scdl_mon2_btn2.pack_forget()
    scdl_mon2_btn3.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_tue1():
    scdl["before"]["subject"] = "応用数学"

    scdl_tue_btn1.pack_forget()
    scdl_tue_btn2.pack_forget()
    scdl_tue_btn3.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_tue2():
    scdl["before"]["subject"] = "電磁気学"

    scdl_tue_btn1.pack_forget()
    scdl_tue_btn2.pack_forget()
    scdl_tue_btn3.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_tue3():
    scdl["before"]["subject"] = "総合英語"

    scdl_tue_btn1.pack_forget()
    scdl_tue_btn2.pack_forget()
    scdl_tue_btn3.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_wed1():
    scdl["before"]["subject"] = "システム制御工学"

    scdl_wed_btn1.pack_forget()
    scdl_wed_btn2.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_wed2():
    scdl["before"]["subject"] = "Java"

    scdl_wed_btn1.pack_forget()
    scdl_wed_btn2.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_thu1():
    scdl["before"]["subject"] = "ドイツ語"

    scdl_thu_btn1.pack_forget()
    scdl_thu_btn2.pack_forget()
    scdl_thu_btn3.pack_forget()
    scdl_thu_btn4.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_thu2():
    scdl["before"]["subject"] = "工学数理"

    scdl_thu_btn1.pack_forget()
    scdl_thu_btn2.pack_forget()
    scdl_thu_btn3.pack_forget()
    scdl_thu_btn4.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_thu3():
    scdl["before"]["subject"] = "電子制御工学実験"

    scdl_thu_btn1.pack_forget()
    scdl_thu_btn2.pack_forget()
    scdl_thu_btn3.pack_forget()
    scdl_thu_btn4.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_fri1():
    scdl["before"]["subject"] = "電磁気学"

    scdl_fri_btn1.pack_forget()
    scdl_fri_btn2.pack_forget()
    scdl_fri_btn3.pack_forget()
    scdl_fri_btn4.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_fri2():
    scdl["before"]["subject"] = "文学特論"

    scdl_fri_btn1.pack_forget()
    scdl_fri_btn2.pack_forget()
    scdl_fri_btn3.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_fri3():
    scdl["before"]["subject"] = "電子機械設計製作"

    scdl_fri_btn1.pack_forget()
    scdl_fri_btn2.pack_forget()
    scdl_fri_btn3.pack_forget()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_mon():
    scdl["before"]["dayofweek"] = "月"

    scdl_day_btn_mon.pack_forget()
    scdl_day_btn_tue.pack_forget()
    scdl_day_btn_wen.pack_forget()
    scdl_day_btn_thu.pack_forget()
    scdl_day_btn_fri.pack_forget()

    scdl_mon_btn1.pack(pady=10)
    scdl_mon_btn2.pack(pady=10)
    scdl_mon_btn3.pack(pady=10)

def scdl_tue():
    scdl["before"]["dayofweek"] = "火"

    scdl_day_btn_mon.pack_forget()
    scdl_day_btn_tue.pack_forget()
    scdl_day_btn_wen.pack_forget()
    scdl_day_btn_thu.pack_forget()
    scdl_day_btn_fri.pack_forget()

    scdl_tue_btn1.pack(pady=10)
    scdl_tue_btn2.pack(pady=10)
    scdl_tue_btn3.pack(pady=10)

def scdl_wed():
    scdl["before"]["dayofweek"] = "水"

    scdl_day_btn_mon.pack_forget()
    scdl_day_btn_tue.pack_forget()
    scdl_day_btn_wen.pack_forget()
    scdl_day_btn_thu.pack_forget()
    scdl_day_btn_fri.pack_forget()

    scdl_wed_btn1.pack(pady=10)
    scdl_wed_btn2.pack(pady=10)

def scdl_thu():
    scdl["before"]["dayofweek"] = "木"

    scdl_day_btn_mon.pack_forget()
    scdl_day_btn_tue.pack_forget()
    scdl_day_btn_wen.pack_forget()
    scdl_day_btn_thu.pack_forget()
    scdl_day_btn_fri.pack_forget()

    scdl_thu_btn1.pack(pady=10)
    scdl_thu_btn2.pack(pady=10)
    scdl_thu_btn3.pack(pady=10)

def scdl_fri():
    scdl["before"]["dayofweek"] = "金"

    scdl_day_btn_mon.pack_forget()
    scdl_day_btn_tue.pack_forget()
    scdl_day_btn_wen.pack_forget()
    scdl_day_btn_thu.pack_forget()
    scdl_day_btn_fri.pack_forget()

    scdl_fri_btn1.pack(pady=10)
    scdl_fri_btn2.pack(pady=10)
    scdl_fri_btn3.pack(pady=10)

def scdl_dayofweek():
    scdl["before"]["day"] = scdl_day_etr.get()

    scdl_day_etr.pack_forget()
    scdl_day_btn.pack_forget()

    scdl_day_btn_mon.pack(pady=10)
    scdl_day_btn_tue.pack(pady=10)
    scdl_day_btn_wen.pack(pady=10)
    scdl_day_btn_thu.pack(pady=10)
    scdl_day_btn_fri.pack(pady=10)

def scdl_day():
    scdl["before"]["month"] = scdl_month_etr.get()

    scdl_month_etr.pack_forget()
    scdl_month_btn.pack_forget()

    scdl_day_etr.pack(pady=250)
    scdl_day_btn.pack()

def scdl_month():
    scdl["before"]["year"] = scdl_year_etr.get()

    scdl_year_lbl.pack_forget()
    scdl_year_btn.pack_forget()

    scdl_month_etr.pack(pady=250)
    scdl_month_btn.pack()

def scdl_year():
    scdl_btn.pack_forget()
    talk_btn.pack_forget()

    scdl_year_etr.pack(pady=250)
    scdl_year_btn.pack()

def talk():
    print("")

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

# jsonファイルの読み込み
#read_file = open("schedule.json")
#read_scdl_dic = json.load(read_file)

# jsonファイルの書き込み
write_file = open("schedule.json", "w")
json.dump(scdl_list, write_file)

# ウィンドウの生成
root = tk.Tk()
root.title("Menu")
root.attributes("-zoomed", "1")

# あとで表示するオブジェクト
scdl_finish_btn = tk.Button(root, text="編集完了", font=("", 25), command=scdl_finish)
scdl_cancel_btn = tk.Button(root, text="キャンセル", font=("", 25), command=scdl_cancel)

scdl_mon2_btn1 = tk.Button(root, text="工学数理演習", font=("", 25), command=scdl_mon_finish1)
scdl_mon2_btn2 = tk.Button(root, text="社会と工学", font=("", 25), command=scdl_mon_finish2)
scdl_mon2_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_mon_finish3)

scdl_tue2_btn1 = tk.Button(root, text="応用数学", font=("", 25), command=scdl_tue_finish1)
scdl_tue2_btn2 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_tue_finish2)
scdl_tue2_btn3 = tk.Button(root, text="総合英語", font=("", 25), command=scdl_tue_finish3)

scdl_wed2_btn1 = tk.Button(root, text="システム制御工学", font=("", 25), command=scdl_wed_finish1)
scdl_wed2_btn2 = tk.Button(root, text="Java", font=("", 25), command=scdl_wed_finish2)

scdl_thu2_btn1 = tk.Button(root, text="ドイツ語", font=("", 25), command=scdl_thu_finish1)
scdl_thu2_btn2 = tk.Button(root, text="工学数理", font=("", 25), command=scdl_thu_finish2)
scdl_thu2_btn4 = tk.Button(root, text="電子制御工学実験", font=("", 25), command=scdl_thu_finish3)

scdl_fri2_btn1 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_fri_finish1)
scdl_fri2_btn2 = tk.Button(root, text="文学特論", font=("", 25), command=scdl_fri_finish2)
scdl_fri2_btn4 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_fri_finish3)

scdl_day2_btn_mon = tk.Button(root, text="月曜日", font=("", 25), command=scdl_mon2)
scdl_day2_btn_tue = tk.Button(root, text="火曜日", font=("", 25), command=scdl_tue2)
scdl_day2_btn_wed = tk.Button(root, text="水曜日", font=("", 25), command=scdl_wed2)
scdl_day2_btn_thu = tk.Button(root, text="木曜日", font=("", 25), command=scdl_thu2)
scdl_day2_btn_fri = tk.Button(root, text="金曜日", font=("", 25), command=scdl_fri2)

scdl_day2_etr = tk.Entry(root, text="", font=("", 25), width=20)
scdl_day2_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_dayofweek2)

scdl_month2_etr = tk.Entry(root, text="", font=("", 25), width=20)
scdl_month2_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_day2)

scdl_year2_lbl = tk.Entry(root, font=("", 25), width=20)
scdl_year2_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_month2)

scdl_mon_btn1 = tk.Button(root, text="工学数理演習", font=("", 25), command=scdl_year2_mon1)
scdl_mon_btn2 = tk.Button(root, text="社会と工学", font=("", 25), command=scdl_year2_mon2)
scdl_mon_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_year2_mon3)

scdl_tue_btn1 = tk.Button(root, text="応用数学", font=("", 25), command=scdl_year2_tue1)
scdl_tue_btn2 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_year2_tue2)
scdl_tue_btn3 = tk.Button(root, text="総合英語", font=("", 25), command=scdl_year2_tue3)

scdl_wed_btn1 = tk.Button(root, text="システム制御工学", font=("", 25), command=scdl_year2_wed1)
scdl_wed_btn2 = tk.Button(root, text="Java", font=("", 25), command=scdl_year2_wed2)

scdl_thu_btn1 = tk.Button(root, text="ドイツ語", font=("", 25), command=scdl_year2_thu1)
scdl_thu_btn2 = tk.Button(root, text="工学数理", font=("", 25), command=scdl_year2_thu2)
scdl_thu_btn3 = tk.Button(root, text="電子制御工学実験", font=("", 25), command=scdl_year2_thu3)

scdl_fri_btn1 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_year2_fri1)
scdl_fri_btn2 = tk.Button(root, text="文学特論", font=("", 25), command=scdl_year2_fri2)
scdl_fri_btn4 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_year2_fri3)

scdl_day_btn_mon = tk.Button(root, text="月曜日", font=("", 25), command=scdl_mon)
scdl_day_btn_tue = tk.Button(root, text="火曜日", font=("", 25), command=scdl_tue)
scdl_day_btn_wen = tk.Button(root, text="水曜日", font=("", 25), command=scdl_wed)
scdl_day_btn_thu = tk.Button(root, text="木曜日", font=("", 25), command=scdl_thu)
scdl_day_btn_fri = tk.Button(root, text="金曜日", font=("", 25), command=scdl_fri)

scdl_day_etr = tk.Entry(root, text="", font=("", 25), width=20)
scdl_day_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_dayofweek)

scdl_month_etr = tk.Entry(root, text="", font=("", 25), width=20)
scdl_month_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_day)

scdl_year_lbl = tk.Entry(root, font=("", 25), width=20)
scdl_year_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_month)

# 最初に表示するオブジェクト
scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
scdl_btn.pack(pady=250)#(anchor = "n")

talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
talk_btn.pack()#(anchor = "n")

root.mainloop()