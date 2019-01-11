import os, sys, time
import tkinter as tk
import json
#from collections import OrderedDict

def scdl_finish():
    scdl_finish_btn.destroy()

    scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
    scdl_btn.pack(pady=250)#(anchor = "n")

    talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
    talk_btn.pack()#(anchor = "n")

def scdl_cancel():
    scdl_finish_btn.destroy()

    scdl_btn = tk.Button(root, text="スケジュール編集", font=("", 25), command=scdl_year)
    scdl_btn.pack(pady=250)#(anchor = "n")

    talk_btn = tk.Button(root, text="ロボメイトと会話", font=("", 25), command=talk)
    talk_btn.pack()#(anchor = "n")

def scdl_mon_finish():
    scdl_mon_btn1.destroy()
    scdl_mon_btn2.destroy()
    scdl_mon_btn3.destroy()

    scdl_finish_btn.pack()

def scdl_tue_finish():
    scdl_tue2_btn1.destroy()
    scdl_tue2_btn2.destroy()
    scdl_tue2_btn3.destroy()

    scdl_finish_btn.pack()

def scdl_wed_finish():
    scdl_wed2_btn1.destroy()
    scdl_wed2_btn2.destroy()

    scdl_finish_btn.pack()

def scdl_thu_finish():
    scdl_thu2_btn1.destroy()
    scdl_thu2_btn2.destroy()
    scdl_thu2_btn3.destroy()

    scdl_finish_btn.pack()

def scdl_fri_finish():
    scdl_fri2_btn1.destroy()
    scdl_fri2_btn2.destroy()
    scdl_fri2_btn3.destroy()

    scdl_finish_btn.pack()

def scdl_mon2():
    scdl_day2_btn_mon.destroy()
    scdl_day2_btn_tue.destroy()
    scdl_day2_btn_wen.destroy()
    scdl_day2_btn_thu.destroy()
    scdl_day2_btn_fri.destroy()

    scdl_mon2_btn1.pack(pady=10)
    scdl_mon2_btn2.pack(pady=10)
    scdl_mon2_btn3.pack(pady=10)

def scdl_tue2():
    scdl_day2_btn_mon.destroy()
    scdl_day2_btn_tue.destroy()
    scdl_day2_btn_wen.destroy()
    scdl_day2_btn_thu.destroy()
    scdl_day2_btn_fri.destroy()

    scdl_tue2_btn1.pack(pady=10)
    scdl_tue2_btn2.pack(pady=10)
    scdl_tue2_btn3.pack(pady=10)

def scdl_wen2():
    scdl_day2_btn_mon.destroy()
    scdl_day2_btn_tue.destroy()
    scdl_day2_btn_wen.destroy()
    scdl_day2_btn_thu.destroy()
    scdl_day2_btn_fri.destroy()

    scdl_wen2_btn1.pack(pady=10)
    scdl_wen2_btn2.pack(pady=10)

def scdl_thu2():
    scdl_day2_btn_mon.destroy()
    scdl_day2_btn_tue.destroy()
    scdl_day2_btn_wen.destroy()
    scdl_day2_btn_thu.destroy()
    scdl_day2_btn_fri.destroy()

    scdl_thu2_btn1.pack(pady=10)
    scdl_thu2_btn2.pack(pady=10)
    scdl_thu2_btn3.pack(pady=10)
    scdl_thu2_btn4.pack(pady=10)

def scdl_fri2():
    scdl_day2_btn_mon.destroy()
    scdl_day2_btn_tue.destroy()
    scdl_day2_btn_wen.destroy()
    scdl_day2_btn_thu.destroy()
    scdl_day2_btn_fri.destroy()

    scdl_fri2_btn1.pack(pady=10)
    scdl_fri2_btn2.pack(pady=10)
    scdl_fri2_btn3.pack(pady=10)
    scdl_fri2_btn4.pack(pady=10)

def scdl_dayofweek2():
    scdl_day2_etr.destroy()
    scdl_day2_btn.destroy()

    scdl_day2_btn_mon.pack(pady=10)
    scdl_day2_btn_tue.pack(pady=10)
    scdl_day2_btn_wen.pack(pady=10)
    scdl_day2_btn_thu.pack(pady=10)
    scdl_day2_btn_fri.pack(pady=10)

def scdl_day2():
    scdl_month_etr.destry()
    scdl_month_etr.destry()

    scdl_day2_etr.pack(pady=250)
    scdl_day2_btn.pack()

def scdl_month2():
    scdl_year2_lbl.destroy()
    scdl_year2_btn.destroy()

    scdl_month2_etr.pack(pady=250)
    scdl_month2_btn.pack()

def scdl_year2_mon():
    scdl_mon_btn1.destroy()
    scdl_mon_btn2.destroy()
    scdl_mon_btn3.destroy()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_tue():
    scdl_tue_btn1.destroy()
    scdl_tue_btn2.destroy()
    scdl_tue_btn3.destroy()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_wed():
    scdl_wed_btn1.destroy()
    scdl_wed_btn2.destroy()
    scdl_wed_btn3.destroy()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_thu():
    scdl_thu_btn1.destroy()
    scdl_thu_btn2.destroy()
    scdl_thu_btn3.destroy()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_year2_fri():
    scdl_fri_btn1.destroy()
    scdl_fri_btn2.destroy()
    scdl_fri_btn3.destroy()

    scdl_year2_lbl.pack(pady=250)
    scdl_year2_btn.pack()

def scdl_mon():
    scdl_day_btn_mon.destroy()
    scdl_day_btn_tue.destroy()
    scdl_day_btn_wen.destroy()
    scdl_day_btn_thu.destroy()
    scdl_day_btn_fri.destroy()

    scdl_mon_btn1.pack(pady=10)
    scdl_mon_btn2.pack(pady=10)
    scdl_mon_btn3.pack(pady=10)

def scdl_tue():
    scdl_day_btn_mon.destroy()
    scdl_day_btn_tue.destroy()
    scdl_day_btn_wen.destroy()
    scdl_day_btn_thu.destroy()
    scdl_day_btn_fri.destroy()

    scdl_tue_btn1.pack(pady=10)
    scdl_tue_btn2.pack(pady=10)
    scdl_tue_btn3.pack(pady=10)

def scdl_wen():
    scdl_day_btn_mon.destroy()
    scdl_day_btn_tue.destroy()
    scdl_day_btn_wen.destroy()
    scdl_day_btn_thu.destroy()
    scdl_day_btn_fri.destroy()

    scdl_wen_btn1.pack(pady=10)
    scdl_wen_btn2.pack(pady=10)

def scdl_thu():
    scdl_day_btn_mon.destroy()
    scdl_day_btn_tue.destroy()
    scdl_day_btn_wen.destroy()
    scdl_day_btn_thu.destroy()
    scdl_day_btn_fri.destroy()

    scdl_thu_btn1.pack(pady=10)
    scdl_thu_btn2.pack(pady=10)
    scdl_thu_btn3.pack(pady=10)
    scdl_thu_btn4.pack(pady=10)

def scdl_fri():
    scdl_day_btn_mon.destroy()
    scdl_day_btn_tue.destroy()
    scdl_day_btn_wen.destroy()
    scdl_day_btn_thu.destroy()
    scdl_day_btn_fri.destroy()

    scdl_fri_btn1.pack(pady=10)
    scdl_fri_btn2.pack(pady=10)
    scdl_fri_btn3.pack(pady=10)
    scdl_fri_btn4.pack(pady=10)

def scdl_dayofweek():
    scdl_day_etr.destroy()
    scdl_day_btn.destroy()

    scdl_day_btn_mon.pack(pady=10)
    scdl_day_btn_tue.pack(pady=10)
    scdl_day_btn_wen.pack(pady=10)
    scdl_day_btn_thu.pack(pady=10)
    scdl_day_btn_fri.pack(pady=10)

def scdl_day():
    scdl_month_etr.destroy()
    scdl_month_btn.destroy()

    scdl_day_etr.pack(pady=250)
    scdl_day_btn.pack()

def scdl_month():
    scdl_year_lbl.destroy()
    scdl_year_btn.destroy()

    scdl_month_etr.pack(pady=250)
    scdl_month_btn.pack()

def scdl_year():
    scdl_btn.destroy()
    talk_btn.destroy()

    scdl_year_lbl.pack(pady=250)
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
#file = open("schedule.json")
#scdl_dic = json.load(file)

# ウィンドウの生成
root = tk.Tk()
root.title("Menu")
root.attributes("-zoomed", "1")

# あとで表示するオブジェクト
scdl_finish_btn1 = tk.Button(root, text="編集完了", font=("", 25), command=scdl_finish)
scdl_finish_btn2 = tk.Button(root, text="キャンセル", font=("", 25), command=scdl_cancel)

scdl_mon2_btn1 = tk.Button(root, text="工学数理演習", font=("", 25), command=scdl_mon_finish)
scdl_mon2_btn2 = tk.Button(root, text="社会と工学", font=("", 25), command=scdl_mon_finish)
scdl_mon2_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_mon_finish)

scdl_tue2_btn1 = tk.Button(root, text="応用数学", font=("", 25), command=scdl_tue_finish)
scdl_tue2_btn2 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_tue_finish)
scdl_tue2_btn3 = tk.Button(root, text="総合英語", font=("", 25), command=scdl_tue_finish)

scdl_wed2_btn1 = tk.Button(root, text="システム制御工学", font=("", 25), command=scdl_wed_finish)
scdl_wed2_btn2 = tk.Button(root, text="Java", font=("", 25), command=scdl_wed_finish)

scdl_thu2_btn1 = tk.Button(root, text="ドイツ語", font=("", 25), command=scdl_thu_finish)
scdl_thu2_btn2 = tk.Button(root, text="工学数理", font=("", 25), command=scdl_thu_finish)
scdl_thu2_btn3 = tk.Button(root, text="電子制御工学実験", font=("", 25), command=scdl_thu_finish)
scdl_thu2_btn4 = tk.Button(root, text="電子制御工学実験", font=("", 25), command=scdl_thu_finish)

scdl_fri2_btn1 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_fri_finish)
scdl_fri2_btn2 = tk.Button(root, text="文学特論", font=("", 25), command=scdl_fri_finish)
scdl_fri2_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_fri_finish)
scdl_fri2_btn4 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_fri_finish)

scdl_day2_btn_mon = tk.Button(root, text="月曜日", font=("", 25), command=scdl_mon2)
scdl_day2_btn_tue = tk.Button(root, text="火曜日", font=("", 25), command=scdl_tue2)
scdl_day2_btn_wen = tk.Button(root, text="水曜日", font=("", 25), command=scdl_wen2)
scdl_day2_btn_thu = tk.Button(root, text="木曜日", font=("", 25), command=scdl_thu2)
scdl_day2_btn_fri = tk.Button(root, text="金曜日", font=("", 25), command=scdl_fri2)

scdl_day2_etr = tk.Entry(root, text="", font=("", 25), width=20)
scdl_day2_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_dayofweek2)

scdl_month2_etr = tk.Entry(root, text="", font=("", 25), width=20)
scdl_month2_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_day2)

scdl_year2_lbl = tk.Entry(root, font=("", 25), width=20)
scdl_year2_btn = tk.Button(root, text="OK", font=("", 25), command=scdl_month2)

scdl_mon_btn1 = tk.Button(root, text="工学数理演習", font=("", 25), command=scdl_year2_mon)
scdl_mon_btn2 = tk.Button(root, text="社会と工学", font=("", 25), command=scdl_year2_mon)
scdl_mon_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_year2_mon)

scdl_tue_btn1 = tk.Button(root, text="応用数学", font=("", 25), command=scdl_year2_tue)
scdl_tue_btn2 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_year2_tue)
scdl_tue_btn3 = tk.Button(root, text="総合英語", font=("", 25), command=scdl_year2_tue)

scdl_wed_btn1 = tk.Button(root, text="システム制御工学", font=("", 25), command=scdl_year2_wed)
scdl_wed_btn2 = tk.Button(root, text="Java", font=("", 25), command=scdl_year2_wed)

scdl_thu_btn1 = tk.Button(root, text="ドイツ語", font=("", 25), command=scdl_year2_thu)
scdl_thu_btn2 = tk.Button(root, text="工学数理", font=("", 25), command=scdl_year2_thu)
scdl_thu_btn3 = tk.Button(root, text="電子制御工学実験", font=("", 25), command=scdl_year2_thu)
scdl_thu_btn4 = tk.Button(root, text="電子制御工学実験", font=("", 25), command=scdl_year2_thu)

scdl_fri_btn1 = tk.Button(root, text="電磁気学", font=("", 25), command=scdl_year2_fri)
scdl_fri_btn2 = tk.Button(root, text="文学特論", font=("", 25), command=scdl_year2_fri)
scdl_fri_btn3 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_year2_fri)
scdl_fri_btn4 = tk.Button(root, text="電子機械設計製作", font=("", 25), command=scdl_year2_fri)

scdl_day_btn_mon = tk.Button(root, text="月曜日", font=("", 25), command=scdl_mon)
scdl_day_btn_tue = tk.Button(root, text="火曜日", font=("", 25), command=scdl_tue)
scdl_day_btn_wen = tk.Button(root, text="水曜日", font=("", 25), command=scdl_wen)
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
