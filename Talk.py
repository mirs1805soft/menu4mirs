import os, sys, time
import json
import subprocess
import socket
import string
import random
import numpy as np
from numpy.random import *

def Talk():
    host = "localhost"
    port = 10500

    p = subprocess.Popen(["./julius_start.sh"], stdout=subprocess.PIPE, shell=True)
    pid = str(p.stdout.read().decode('utf-8'))  # juliusのプロセスIDを取得
    time.sleep(5)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    data =""
    killword =""

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
                            print ("<<<please speak>>>")
                            killword = "おはよう"

                    elif strTemp == 'こんにちは':
                        if killword != "こんにちは":
                            print ("Result: " + strTemp)
                            #os.system("aplay '/home/pi/Music/konnichiwa.wav'")
                            print ("<<<please speak>>>")
                            killword = "こんにちは"

                    elif strTemp == 'こんばんは':
                        if killword != "こんばんは":
                            print ("Result: " + strTemp)
                            #os.system("aplay '/home/pi/Music/konbanwa.wav'")
                            print ("<<<please speak>>>")
                            killword = "こんばんは"

                    elif strTemp == 'よていをおしえて':
                        if killword != "よていをおしえて":
                            print ("Result: " + strTemp)
                            #os.system("aplay '/home/pi/Music/konbanwa.wav'")
                            print ("<<<please speak>>>")
                            killword = "よていをおしえて"

                    else:
                        print("Result:" + strTemp)
                        i = randint(3)
                        if i == 0:
                            os.system("aplay: '/home/pi/Music/aizuchi00.wav'")
                        elif i == 1:
                            os.system("aplay: '/home/pi/Music/aizuchi01.wav'")
                        elif i == 2:
                            os.system("aplay: '/home/pi/Music/aizuchi02.wav'")
                        print ("<<<please speak>>>")
                    data = ""
      else:
                data += str(sock.recv(1024).decode('utf-8'))