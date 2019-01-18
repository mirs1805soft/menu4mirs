import os, sys, time
import json
import subprocess
import socket
import string
import random
import numpy as np
from numpy.random import *

def Talk():
    read_file = open("schedule.json", "r")
    scdl_list = json.load(read_file)

    voice = scdl_list[before][year] + "年" + scdl_list[before][month] + "月" + scdl_list[before][day] + "日" + scdl_list[before][dayofweek] + "曜日の" + scdl_list[before][subject] + "が、" + scdl_list[after][year] + "年" + scdl_list[after][month] + "月" + scdl_list[after][day] + "日" + scdl_list[after][dayofweek] + "曜日の" + scdl_list[after][subject] + "と交換です。"
    voice2talk = "echo '" + voice + "' | open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./open_jtalk_tmp.wav"

    host = "localhost"
    port = 10500

    p = subprocess.Popen(["./julius_start.sh"], stdout=subprocess.PIPE, shell=True)
    pid = str(p.stdout.read().decode('utf-8'))  # juliusのプロセスIDを取得
    time.sleep(5)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    data = ""
    killword = ""

    while True:
        while (1):
            if '</RECOGOUT>\n.' in data:
                #data = data + sock.recv(1024)
                 strTemp = ""
                for line in data.split('\n'):
                    index = line.find('WORD="')
                    if index != -1:
                        line = line[index+6:line.find('"',index+6)]
                        strTemp += str(line)

                    elif strTemp == 'おはよう':
                        if killword != 'おはよう':
                            print ("Result: " + strTemp)
                            #os.system("aplay '/home/pi/Music/ohayo.wav'")
                            subprocess.call('echo "おはよう" | open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./open_jtalk_tmp.wav'.split())
                            killword = "おはよう"

                    elif strTemp == 'こんにちは':
                        if killword != "こんにちは":
                            print ("Result: " + strTemp)
                            #os.system("aplay '/home/pi/Music/konnichiwa.wav'")
                            subprocess.call('echo "こんにちは" | open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./open_jtalk_tmp.wav'.split())
                            killword = "こんにちは"

                    elif strTemp == 'こんばんは':
                        if killword != "こんばんは":
                            print ("Result: " + strTemp)
                            #os.system("aplay '/home/pi/Music/konbanwa.wav'")
                            subprocess.call('echo "こんばんは" | open_jtalk -m /usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice -x /var/lib/mecab/dic/open-jtalk/naist-jdic -ow ./open_jtalk_tmp.wav'.split())
                            killword = "こんばんは"

                    elif strTemp == 'よていをおしえて':
                        if killword != "よていをおしえて":
                            print ("Result: " + strTemp)
                            #os.system("aplay '/home/pi/Music/konbanwa.wav'")
                            subprocess.call(voice2talk.split())
                            killword = "よていをおしえて"

                    else:
                        print("Result:" + strTemp)
                        i = randint(3)
                        if i == 0:
                            print("")
                            #os.system("aplay: '/home/pi/Music/aizuchi00.wav'")
                        elif i == 1:
                            print("")
                            #os.system("aplay: '/home/pi/Music/aizuchi01.wav'")
                        elif i == 2:
                            print("")
                            #os.system("aplay: '/home/pi/Music/aizuchi02.wav'")
                    data = ""
      else:
                data += str(sock.recv(1024).decode('utf-8'))
