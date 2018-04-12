# GNUradio-802.11ah

Hey there,

This respository contains an IEEE 802.11ah transceiver implementation in GNUradio. It has been tested with the Ettus USRP N210, but should be able to work with other high-bandwidth Software Defined Radios (SDRs) as well. It relies on a few other repositories, mainly the one created by Bastian Bloessl: https://github.com/bastibl/gr-ieee802-11. 

## Installing GNUradio

If you're starting this project as a total beginner like me, first things first is setting up your Linux distribution. I heavily recommend to install Linux natively, if you'd like to know why please read the section _GNUradio in a VM_ at the bottom of the page. Any distro should work fine, Ubuntu is the most commonly used one so that is my preferred choice.  

Next is installing GNUradio. There are many ways to install GNUradio, some being much easier than others. The one I initially tried was just doing an _apt install gnuradio_ command. However, if you choose to do this you need to install all the dependencies manually, and if only one version mismatches with another (for example, one hasn't been updated for a while) everything might not work. For me, after a lot of hassle and manually fixing stuff I had an apparently unfixable library mismatch. 

Because of this, after having tried several installation methods I can say that installing GNUradio is by far the easiest using PyBOMBS. To do this, start by installing pip:

    sudo apt install python-pip

Then follow the instructions posted on https://github.com/gnuradio/pybombs. For the impatient, these were the commands that did the trick the last time I checked:

    pip install PyBOMBS
    pybombs auto-config
    pybombs prefix init ~/prefix -a myprefix -R gnuradio-default

This last step can easily take a few hours, so be patient. After this, GNUradio should be installed in the folder "prefix" located in your home directory (~/prefix). Normally, Linux would install everything in various locations; doing this ensures everything is installed in one folder. This is really useful if you mess things up, since you can simply delete the prefix folder and try again. Now, _every_ time you want to start GNUradio in a new terminal, execute the following commands:

    source ~/prefix/setup_env.sh
    gnuradio-companion

Try to do the _source_ command before you do anything else in terminal, forgetting this has cost me a lot of extra hassle at times.And GNUradio should be working!

## Installing gr-ieee802-11

Next up is installing the repository by Bastian Bloessl. How to do this is described in detail on https://github.com/bastibl/gr-ieee802-11. Some tips to overcome obstacles I encountered are:

- If you installed using PyBOMBS, make sure you are on the _master_ branch on both Bastian's repositories (gr-foo and gr-ieee-802-11), and not on the _next_ branch. If you're not, you'll get some weird errors later on. To do this, type _git checkout master_ after cloning each git repository. 
- Make sure you've typed source _~/prefix/setup_env.sh_, or cmake won't know where to find the gnuradio files.
- It doesn't really matter where you clone the repositories gr-foo and gr-ieee802-11 to, since the _cmake_ command you run later will automatically install everything in the right location. I recommend creating a folder like ~/Documents/gnuradio and install everything there to keep things clear.

Now, everything should be working. Enjoy!

### GNUradio in a VM
I thought it would be the most practical to set everything up on a VM (VirtualBox/VMware), however in the end this proved to involve a large amount of extra operations I had to carry out to make everything working. In the end after hours of fixing small VM-specific errors I received underflow/overflow errors from my SDR: my ethernet driver could not connect to the SDR fast enough, even though it was a full-duplex 1Gbit/s adapter. I tried to mess around with installing and changing custom drivers for my ethernet adapter, but all to no avail. Installing native Linux immediately solved this and many other problems. Therefore I heavily recommend to isntall Linux natively, especially if you are not an advanced Linux user like me. 
