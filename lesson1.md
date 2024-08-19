#Lesson One

##1. Install micro-SD card.
##2. Plug in keyboard, mouse and video.
##3. Enable SSH 
To enable SSH on a Raspberry Pi using the GUI, you can do the following:
Click the Raspberry Pi logo in the top-left corner
Select Preferences > Raspberry Pi Configuration
Click the Interfaces tab
Select Enable in the SSH options
Click OK to save the changes 
You can also enable SSH using the Raspberry P
##4. Get the IP Address (referred to below as pi.ip.addre.ss)
`$ ip address`
##5. Set root password

Open Terminal

`$ sudo passwd root`

LAB_PASSWORD (twice)

##6. Set Pi Name
hostnamectl set-hostname YOUR_PI_NAME
##7. Allow SSH Root Login

`$ sudo nano /etc/ssh/sshd_config`

Change: 
PermitRootLogin prohibit-password

To:
PermitRootLogin yes

Exit (Ctl-X)

##8. Set up SSH Login

Complete Article for furture reference: https://help.dreamhost.com/hc/en-us/articles/215464758-Set-up-passwordless-login-in-PuTTY

`$ cd ~`

`$ wget http://13.64.77.78/keys/pi_key`

`$ mkdir .ssh`

`$ chmod 700 .ssh`

`$ ssh-keygen -i -f pi_key >> ~/.ssh/authorized_keys`

##9. Putty Config (demonstration)

##10. Install and test apache (web server)

`$ apt install apache2 -y`

Test it, put the pi address in PC browser 

http://pi.ip.addre.ss/

#11. Shutdown PI and install USB Camera (video.....)

`$ lsusb`

Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub

`$ apt install fswebcam`

Take a picture

`$ fswebcam -r 1280x720 --no-banner /var/www/html/1.jpg`

View it in browser

http://pi.ip.addre.ss/1.jpg

Look at the file it created 

`$ ls -l /var/www/html/1.jpg`

-rw-r--r-- 1 root root 185255 Aug  4 14:11 /var/www/html/1.jpg

(Size in bytes 185255)


`$ fswebcam -r 3840x288 --no-banner /var/www/html/1s.jpg`

`$ ls -l /var/www/html/1s.jpg`

-rw-r--r-- 1 root root 130609 Aug  4 14:19 /var/www/html/1s.jpg

##12. Get more detail about camera

>> v4l2-ctl --list-formats-ext > /var/www/html/usbresolution.txt

Check it out in browser (for future reference)
http://pi.ip.addre.ss/usbresolution.txt

`$ mkdir /var/www/html/jpg_sizes`


`$ fswebcam -r 640x480 --no-banner /var/www/html/jpg_sizes/640x480.jpg`
`$ fswebcam -r 1920x1080 --no-banner /var/www/html/jpg_sizes/1920x1080.jpg`
`$ fswebcam -r 1280x960 --no-banner /var/www/html/jpg_sizes/1280x960.jpg`
`$ fswebcam -r 1280x720 --no-banner /var/www/html/jpg_sizes/1280x720.jpg`
`$ fswebcam -r 1024x576 --no-banner /var/www/html/jpg_sizes/1024x576.jpg`
`$ fswebcam -r 800x600 --no-banner /var/www/html/jpg_sizes/800x600.jpg`
`$ fswebcam -r 640x360 --no-banner /var/www/html/jpg_sizes/640x360.jpg`
`$ fswebcam -r 640x480 --no-banner /var/www/html/jpg_sizes/640x480.jpg`

`$  ls -l /var/www/html/jpg_sizes

`
-rw-r--r-- 1 root root 167068 Aug 19 12:10 1024x576.jpg
-rw-r--r-- 1 root root 225826 Aug 19 12:10 1280x720.jpg
-rw-r--r-- 1 root root 223167 Aug 19 12:10 1280x960.jpg
-rw-r--r-- 1 root root 504530 Aug 19 12:09 1920x1080.jpg
-rw-r--r-- 1 root root 110898 Aug 19 12:10 640x360.jpg
-rw-r--r-- 1 root root 115160 Aug 19 12:10 640x480.jpg
-rw-r--r-- 1 root root 152399 Aug 19 12:10 800x600.jpg
`


//look on browser
http://192.168.1.149/1920x1080.jpg

Make a spreadsheet  (figure out about https).
http://fairchildlabs.org/early/resolution.xlsx


apt install ffmpeg


###ffmpeg Documntation

https://www.ffmpeg.org/ffmpeg.html

Help Files 




http://fairchildlabs.org/SeasonOne/ref/ffmpeg.txt
http://fairchildlabs.org/SeasonOne/ref/ffmpeg_long.txt
http://fairchildlabs.org/SeasonOne/ref/ffmpeg_long.txt

To get from command line type:
`$ ffmpeg --help`



### Record a Video


####Record a single video
`$ffmpeg -f v4l2 -framerate 30 -video_size 640x480 -i /dev/video0 output.mp4`

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





















