#!/bin/sh

julius -C /home/pi/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/main.jconf -module > /dev/null &
echo $! # プロセスIDを出力
sleep 3 # 5秒間スリープ
