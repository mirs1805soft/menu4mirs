import subprocess
import os, sys, time

#run = subprocess.call("thread_min0_1".split())
open_jtalk = ["open_jtalk"]
ropen_jtalk = ["open_jtalk"]
mech = ["-x", "/var/lib/mecab/dic/open-jtalk/naist-jdic"]
htsvoice = ["-m", "/usr/share/hts-voice/miku/miku.htsvoice"]
voice_speed = ["-r", "1.0"]
outwav = ["-ow", "/home/pi/menu4mirs/open_jtalk.wav"]
cmd = open_jtalk + mech + htsvoice + voice_speed + outwav
c = subprocess.Popen(cmd, stdin = subprocess.PIPE)
c.stdin.write("あしたのじゅぎょうはどいつご、こうがくすうり、でんしせいぎょこうがくじっけん、だよ、わすれないでね".encode("utf-8"))
c.stdin.close()
c.wait()
aplay = ["aplay", "-q", "/home/pi/menu4mirs/open_jtalk.wav"]
wr = subprocess.Popen(aplay)
