#!/bin/sh

julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.3.1-linux/word.jconf -module > /dev/null &
echo $! # プロセスIDを出力
sleep 5 # 5秒間スリープ
