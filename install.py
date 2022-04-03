import os
import subprocess

def checkForRoot():
    if(subprocess.getoutput("whoami")!="root"):
        print("Please execute the program as root!!")
        print("Exiting..")
        exit()
    else:
        installPreBuildDependencies()

def installPreBuildDependencies():
    print("Installing dependencies.....\n\nThis may take a few moments.....")
    if(subprocess.getstatusoutput("pip3")[0]!=0):
        os.system("sudo apt install python3-pip -y")
    if(subprocess.getstatusoutput("python3 -m pyfiglet")[0] not in [0,1]):
        os.system("sudo pip3 install pyfiglet")
    if(subprocess.getstatusoutput("python3 -m termcolor") not in [0,1]):
        os.system("sudo pip3 install termcolor")
    os.system("clear")
    installBuildDependencies()

def installBuildDependencies():
    from pyfiglet import Figlet
    from termcolor import colored

    banner = Figlet(font="big")
    print(colored(banner.renderText("Linux Dynamic Wallpapers"),color="yellow"))
    print("\n")
    print(colored("By Amal Thomas",color="red"))
    print("\n\n")
    a = input("checkpoint 1")
    print(colored("Installing Build libraries. This may take some time.",color="green"))
    subprocess.getoutput("sudo apt-get install x11-xserver-utils python3-pyqt5 python3-pyqt5.qtwebengine python3-pyqt5.qtwebchannel libqt5webkit5-dev feh cron -y")
    b = input("checkpoint 2")
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
    os.system("sudo cp -r ./main.py /usr/share/linuxDynamicWallpapers")
    os.system("sudo chmod +x /usr/share/linuxDynamicWallpapers/dwl.sh")
    if(os.path.exists("/usr/bin/dwl")):
        os.system("sudo rm -rf /usr/bin/dwl")
        os.system("sudo ln -s /usr/share/linuxDynamicWallpapers/dwl.sh /usr/bin/dwl")
    else:
        os.system("sudo ln -s /usr/share/linuxDynamicWallpapers/dwl.sh /usr/bin/dwl")

    os.system("clear")
    print(colored("Finished!!",color="green"))
    print("\n")
    print(colored("Linux Dynamic Wallpapers have been installed in your system.\n\n",color="blue"))
    print(colored(f"To use it now, just type dwl in the terminal",color="green"))
def cleanUp():
    os.system("rm -rf ./data")
    os.system("rm -rf ./static")
    os.system("rm -rf ./templates")
    os.system("rm -rf ./images")
    os.system("rm -rf *")


if __name__ == "__main__":
    checkForRoot()


