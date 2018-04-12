# GNUradio-802.11ah

Hey there,

This respository contains an IEEE 802.11ah transceiver implementation in GNUradio. It has been tested with the Ettus USRP N210, but should be able to work with other high-bandwidth software defined radios as well. It relies on a few other repositories, mainly the one created by Bastian Bloessl: https://github.com/bastibl/gr-ieee802-11. 

## Installing GNUradio

If you started this project as a total noob like me, first things first is setting up your Linux distribution. I heavily recommend to install Linux natively, if you'd like to know why please read _this_. Any distro should work fine, Ubuntu is the most commonly used one so that is my preferred choice.  

Next is installing GNUradio. There are many ways to install GNUradio, and some are incredibly easy. The one I initially tried was just doing an apt-get command. However, if you choose to do this you need to install all the dependencies manually, and if only one version mismatches with another (for example, one hasn't been updated for a while) everything might not work. After having tried several installation methods I can say that installing GNUradio is by far the easiest using PyBOMBS. To do this, start by installing pip:

  $ sudo apt install python-pip

Then follow the instructions posted on https://github.com/gnuradio/pybombs. For the impatient, these were the commands that did the trick the last time I checked:

$ pip install PyBOMBS
$ pybombs auto-config
$ pybombs prefix init ~/prefix -a myprefix -R gnuradio-default

This last step can easily take a few hours, so be patient. After this, GNUradio should be installed in the folder "prefix" located in your home directory (~/prefix). Normally, Linux would install everything in various locations; doing this ensures everything is installed in one folder. This is really useful if you mess things up, you can simply delete the prefix folder and try again. Now, every time you want to start GNUradio in a new terminal, execute the following commands:

 $ source ~/prefix/setup_env.sh
 $ gnuradio-companion

And GNUradio should be working!

## Installing gr-ieee802-11

Next up is installing the repository by Bastian Bloessl. How to do this is described on https://github.com/bastibl/gr-ieee802-11. Three tips for installing it are:

- If you installed using PyBOMBS, make sure you install the _master_ branch on Bastian's repository. If you don't, you'll get some weird errors later on.
- Since we've installed using PyBOMBS in the custom "prefix" directory, you need to specify this to gr-ieee-802-11. You can do this by changing the ... file, adding the following lines:

[base]....
$need to fill this in

- It doesn't really matter where you clone the repositories gr-foo and gr-ieee802-11 to, since the _cmake_ command you run later will automatically install everything in the right location. I recommend creating a folder like ~/Documents/gnuradio and install everything there to keep things clear.

Now, everything should be working. Enjoy!

### GNUradio in a VM
I thought it would be the most practical to set everything up on a VM (VirtualBox/VMware), however in the end this proved to involve a large amount of extra operations I had to carry out to make everything working. In the end after hours of fixing small VM-specific errors I received underflow/overflow errors from my SDR: my ethernet driver could not connect to the SDR fast enough, even though it was a full-duplex 1Gbit/s adapter. I tried to mess around with installing and changing custom drivers for my ethernet adapter, but all to no avail. Installing native Linux immediately solved this and many other problems. Therefore I heavily recommend to isntall Linux natively, especially if you are not an advanced Linux user like me. 
