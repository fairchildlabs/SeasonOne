
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

