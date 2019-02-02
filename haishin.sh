#!/bin/sh

ffmpeg -f alsa -i hw:1 -f v4l2 -thread_queue_size 8192 -input_format yuyv422 -video_size 1280x720 -framerate 2 -i /dev/video0 -c:v h264_omx -b:v 64k -bufsize 64k -vsync 1 -g 8 -c:a aac -b:a 16k -ar 44100 -f flv rtmp://a.rtmp.youtube.com/live2/brvq-0r7s-sztd-5dqs
