import os
import subprocess

def checkForRoot(): #Checks whether root priviledges have been provided .
    if(subprocess.getoutput("whoami")!="root"):
        print("Please execute the program as root!!")
        print("Exiting..")
        exit()
    else:
        installPreBuildDependencies()

def installPreBuildDependencies(): #Installing the pre-build dependencies
    print("Installing dependencies.....\n\nThis may take a few moments.....")
    if(subprocess.getstatusoutput("pip3")[0]!=0):
        os.system("sudo apt install python3-pip -y")
    if(subprocess.getstatusoutput("sudo python3 -m pyfiglet")[0] not in [0]):
        os.system("sudo pip3 install pyfiglet")
    if(subprocess.getstatusoutput("sudo python3 -m termcolor") not in [0]):
        os.system("sudo pip3 install termcolor")
    os.system("clear")
    installBuildDependencies()

def installBuildDependencies(): #install the build dependencies
    from pyfiglet import Figlet
    from termcolor import colored
    
    banner = Figlet(font="big")
    print(colored(banner.renderText("Linux Dynamic Wallpapers"),color="yellow"))
    print("\n")
    print(colored("By Amal Thomas",color="red"))
    print("\n\n")
    print(colored("Installing Build libraries. This may take some time.",color="green"))
    os.system("sudo apt-get install x11-xserver-utils python3-pyqt5 python3-pyqt5.qtwebengine python3-pyqt5.qtwebchannel libqt5webkit5-dev feh cron -y")
    os.system("pip3 install Flask pywebview argparse")
    print(colored("Installing files. This may take a while.",color="green"))
    if(os.path.exists("/usr/share/linuxDynamicWallpapers")):
        os.system("sudo rm -rf /usr/share/linuxDynamicWallpapers")
        os.system("sudo mkdir -p /usr/share/linuxDynamicWallpapers")
    else:
        os.system("sudo mkdir -p /usr/share/linuxDynamicWallpapers")
    os.system("sudo cp -r ./data /usr/share/linuxDynamicWallpapers")
    os.system("sudo cp -r ./static /usr/share/linuxDynamicWallpapers")
    os.system("sudo cp -r ./templates /usr/share/linuxDynamicWallpapers")
    os.system("sudo cp -r ./images /usr/share/linuxDynamicWallpapers")
    os.system("sudo cp -r ./dwl.sh /usr/share/linuxDynamicWallpapers")
    os.system("sudo cp -r ./setdwl.sh /usr/share/linuxDynamicWallpapers")
    os.system("sudo cp -r ./main.py /usr/share/linuxDynamicWallpapers")
    os.system("sudo chmod +x /usr/share/linuxDynamicWallpapers/dwl.sh")
    os.system("sudo chmod +x /usr/share/linuxDynamicWallpapers/setdwl.sh")
    os.system("sudo chmod 777 /usr/share/linuxDynamicWallpapers/data/data.dat")
    if(os.path.exists("/usr/bin/dwl")):
        os.system("sudo rm -rf /usr/bin/dwl")
        os.system("sudo ln -s /usr/share/linuxDynamicWallpapers/dwl.sh /usr/bin/dwl")
    if(os.path.exists("/usr/bin/setdwl")):
        os.system("sudo rm -rf /usr/bin/setdwl")
        os.system("sudo ln -s /usr/share/linuxDynamicWallpapers/setdwl.sh /usr/bin/setdwl")
    else:
        os.system("sudo ln -s /usr/share/linuxDynamicWallpapers/dwl.sh /usr/bin/dwl")
        os.system("sudo ln -s /usr/share/linuxDynamicWallpapers/setdwl.sh /usr/bin/setdwl")

    os.system("clear")
    print(colored("Finished!!",color="green"))
    print("\n")
    print(colored("Linux Dynamic Wallpapers have been installed in your system.\n\n",color="blue"))
    print(colored(f"To use it now, just type dwl in the terminal",color="green"))

def cleanUp(): #Clean up the installation files. Not executing as of now
    os.system("rm -rf ./data")
    os.system("rm -rf ./static")
    os.system("rm -rf ./templates")
    os.system("rm -rf ./images")
    os.system("rm -rf *")


if __name__ == "__main__":
    checkForRoot()


