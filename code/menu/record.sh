#!/bin/bash

vid_size="640x480"
vid_device="/dev/video0"
out_file="/var/www/html/video_15/640x480_a.mp4" 


ffmpeg -f v4l2 -framerate 30 -video_size $vid_size -i $vid_device $out_file





