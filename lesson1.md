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

Bus 003 Device 003: ID 328f:0073 EMEET HD Webcam eMeet C950

`$ apt install fswebcam`

Take a picture

`$ fswebcam -r 1280x720 --no-banner /var/www/html/1.jpg`

View it in browser

http://pi.ip.addre.ss/1.jpg

Look at the file it created 

`$ ls -l /var/www/html/1.jpg`

-rw-r--r-- 1 root root 185255 Aug  4 14:11 /var/www/html/1.jpg
(Size in bytes 185255)


>> fswebcam -r 3840x288 --no-banner /var/www/html/1s.jpg
>> ls -l /var/www/html/1s.jpg
-rw-r--r-- 1 root root 130609 Aug  4 14:19 /var/www/html/1s.jpg

Get more detail
>> v4l2-ctl --list-formats-ext > /var/www/html/usbresolution.txt

Check it out in browser (for future reference)
http://192.168.1.149/usbresolution.txt


fswebcam -r 640x480 --no-banner /var/www/html/640x480.jpg
fswebcam -r 1920x1080 --no-banner /var/www/html/1920x1080.jpg
fswebcam -r 1280x960 --no-banner /var/www/html/1280x960.jpg
fswebcam -r 1280x720 --no-banner /var/www/html/1280x720.jpg
fswebcam -r 1024x576 --no-banner /var/www/html/1024x576.jpg
fswebcam -r 800x600 --no-banner /var/www/html/800x600.jpg
fswebcam -r 640x360 --no-banner /var/www/html/640x360.jpg
fswebcam -r 640x480 --no-banner /var/www/html/640x480.jpg

ls -l /var/www/html


-rw-r--r-- 1 root root 220087 Aug  4 14:28 1024x576.jpg
-rw-r--r-- 1 root root 318772 Aug  4 14:41 1280x720.jpg
-rw-r--r-- 1 root root 407712 Aug  4 14:26 1280x960.jpg
-rw-r--r-- 1 root root 677830 Aug  4 14:25 1920x1080.jpg
-rw-r--r-- 1 root root 185255 Aug  4 14:11 1.jpg
-rw-r--r-- 1 root root 130609 Aug  4 14:19 1s.jpg
-rw-r--r-- 1 root root 222889 Aug  4 14:11 2.jpg
-rw-r--r-- 1 root root 395652 Aug  4 14:12 3.jpg
-rw-r--r-- 1 root root 108512 Aug  4 14:29 640x360.jpg
-rw-r--r-- 1 root root 133886 Aug  4 14:29 640x480.jpg
-rw-r--r-- 1 root root 190412 Aug  4 14:29 800x600.jpg
-rw-r--r-- 1 root root  10701 Aug  4 12:52 index.html
-rw-r--r-- 1 root root   1197 Aug  4 14:23 usbresolution.txt



//look on browser
http://192.168.1.149/1920x1080.jpg

Make a spreadsheet  (figure out about https).
http://fairchildlabs.org/early/resolution.xlsx


apt install ffmpeg




ffmpeg -f v4l2 -framerate 25 -video_size 640x480 -i /dev/video0 output.mkv



v4l2-ctl --list-devices


v4l2-ctl --list-formats


/****************************************************
video streaming

https://randomnerdtutorials.com/video-streaming-with-raspberry-pi-camera/


https://www.instructables.com/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/


apt-get install motion 































