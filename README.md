

#Season  One - Lab 1

##1. Install micro-SD card.
##2. Install video screen, keyboard, mouse.
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

apt install ffmpeg

##11. Shutdown PI and install USB Camera (video.....)

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

`$ v4l2-ctl --list-formats-ext > /var/www/html/usbresolution.txt`

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

`$  ls -l /var/www/html/jpg_sizes`

<pre>
-rw-r--r-- 1 root root 167068 Aug 19 12:10 1024x576.jpg
-rw-r--r-- 1 root root 225826 Aug 19 12:10 1280x720.jpg
-rw-r--r-- 1 root root 223167 Aug 19 12:10 1280x960.jpg
-rw-r--r-- 1 root root 504530 Aug 19 12:09 1920x1080.jpg
-rw-r--r-- 1 root root 110898 Aug 19 12:10 640x360.jpg
-rw-r--r-- 1 root root 115160 Aug 19 12:10 640x480.jpg
-rw-r--r-- 1 root root 152399 Aug 19 12:10 800x600.jpg
<pre>


//look on browser
http://pi.ip.addre.ss/jpg_sizes/1920x1080.jpg

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


##13. Record Videos

`$ mkdir /var/www/html/video_13/`


####Record a single video
`$ ffmpeg -f v4l2 -framerate 30 -video_size 640x480 -i /dev/video0 /var/www/html/video_13/640x480.mp4`
<CTRL-C> to Stop
http://pi.ip.addre.ss/video_13/640x480.mp4

####Record a single video with sound
##### Get the card # of USB Audio (Webcam) [card 2: in example]
`$ arecord -l`
<pre>

**** List of CAPTURE Hardware Devices ****
card 2: W4DS [W4DS], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
</pre>
##### Record video and audio in same capture
`$ ffmpeg -f alsa -ac 2 -i hw:2 -f v4l2 -framerate 30 -video_size 640x480 -i /dev/video0 /var/www/html/video_13/640x480_sound.mp4`

http://pi.ip.addre.ss/video_13/640x480_sound.mp4

##14. Build Menu
### Use git to clone repository
`$ cd ~`
`$ git clone https://github.com/fairchildlabs/SeasonOne.git`

ON PI TERMINAL
`$ su root`
TYPE LAB PASSWORD
`$ cd ~`
`$ cd SeasonOne/code/menu`
`$ python menu.py`

Look at the code in menu.py
FROM PC PUTTY
`$ cd ~`
`$ cd SeasonOne/code/menu`
`$ nano menu.py`


##14. Build Menu
### Use git to clone repository
`$ cd ~`
`$ git clone https://github.com/fairchildlabs/SeasonOne.git`

ON PI TERMINAL or FROM PC PUTTY
`$ su root`
TYPE LAB PASSWORD
`$ cd ~`
`$ cd SeasonOne/code/menu`
`$ python menu.py`

Look at the code in menu.py
FROM PC PUTTY
`$ cd ~`
`$ cd SeasonOne/code/menu`
`$ nano menu.py`
##15. Test Bash script
FROM PC PUTTY
`$ cd ~`
`$ cd SeasonOne/code/menu`
`$ mkdir /var/www/html/video_15/`
`$ nano record.sh`
LOOK AT SCRIPT
<CTRL-X> to Exit
`$ ./record.sh`
EXPLAIN Permision denied
`$ chmod +x record.sh`
`$ ./record.sh`
RECORD SOME VIDEO <CTRL-X> to stop
WATCH it in browser
http://192.168.1.157/video_15/640x480.mp4


##16. Test Menu2



ON PI TERMINAL
`$ su root`
TYPE LAB PASSWORD
`$ cd ~`
`$ cd SeasonOne/code/menu`
`$ python menu2.py`


 Map network drive (to make file copy easier)  Open Terminal (putty SSH with root/Astros.22) 
    a. CMD> mkdir /root/perfshare
    b. CMD> nano /etc/fstab
       Add this line at : //10.238.18.110/perfshare /root/perfshare  cifs  credentials=/root/.perfsharecred,file_mode=0777,dir_mode=0777,noperm,iocharset=utf8 0       0
    c. CMD > nano /root/.perfsharecred 
    //NOTE:  creATE NEW FILE WITH NANO AND TYPE THE FOLLOWING, DON'T COPY/PASTE SOME CHARECTER ENCODING STUFF WILL 
    //CAUSE IT NOT TO WORK


//otis-fairchild-labs/labshare /var/www/html/labshare  cifs  credentials=/var/www/.labsharecred,file_mode=0777,dir_mode=0777,noperm,iocharset=utf8 0    
 
    labshare (file://OTIS-FAIRCHILD-/labshare)

       Add these lines:
       username=Administrator
	   password=Astros.22
       domain=MCHP-MAIN
    d. CMD> mount  -a

