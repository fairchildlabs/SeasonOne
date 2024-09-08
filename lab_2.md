7
#185`$ffmpeg -f v4l2 -framerate 30 -video_size 800x600 -i /dev/video0 -segment_time 8 -f segment output%03d.mp4`

$ffmpeg -f v4l2 -framerate 30 -video_size 800x600 -i /dev/video0 -segment_time 185 -f segment output%03d.mp4`


###GUI
PY GAME
https://www.pygame.org/wiki/GettingStarted
https://github.com/PySimpleGUI
https://kivy.org/#home

#1. Plug In USB Thumbdrive
`$ lsblk`
`
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    1 119.5G  0 disk
└─sda1        8:1    1 119.5G  0 part /media/astros/Samsung USB
mmcblk0     179:0    0  29.7G  0 disk
├─mmcblk0p1 179:1    0   512M  0 part /boot/firmware
└─mmcblk0p2 179:2    0  29.2G  0 part /
`
#2. Create Partition and Format Drive

`$ umount /media/astros/Samsung\ USB`
`$ fdisk /dev/sda`
(d) for delete 
(n) new
(p) primary
<enter><enter><enter>
(w) for write

###Create file system
`$ mkfs -t vfat -I /dev/sda1`
`$ cd ~`
`$ mkdir usbdrive`
`$ mount /dev/sda1 usbdrive -o umask=000`
---------------------------------------------------------------------------------

cat /dev/ttyACM0

 apt install gpsd


apt-get install gpsd gpsd-clients
mkdir gps
cd pgs
 wget http://fairchildlabs.org/SeasonOne/code/library_gps.py
  wget http://fairchildlabs.org/SeasonOne/code/serial_gps.py

----------------------------------------------------------------------------

https://pygame-menu.readthedocs.io/en/latest/

pip install pygame-menu -U





####Record a video in 8 second segments

`$ffmpeg -f v4l2 -framerate 30 -video_size 800x600 -i /dev/video0 -segment_time 8 -f segment output%03d.mp4`

#### Covert video to Black & White

`$ffmpeg -i output000.mp4 -vf extractplanes=y bw000.mp4`

#### Reduce frame rate

`$ffmpeg -i output000.mp4  -filter:v fps=2 slow.mp4`

`$ffmpeg -i output000.mp4  -filter:v fps=10 -vf extractplanes=y slow_bw.mp4`





v4l2-ctl --list-formats


/****************************************************
video streaming

https://randomnerdtutorials.com/video-streaming-with-raspberry-pi-camera/


https://www.instructables.com/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/

apt-get install motion 









ffmpeg -f dshow -framerate 15 -i video="USB Video Device":audio="Microphone (USB Audio Device)" -s 640x360 -c:v libx264 -g 15 -c:a aac -preset veryfast -segment_time 10 -segment_wrap 24 -f segment %03d.ts

