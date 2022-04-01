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
    print("Installing dependencies.....\n\n This may take a few moments.....")
    if(subprocess.getstatusoutput("pip3")[0]!=0):
        os.system("sudo apt install python3-pip -y")
    if(subprocess.getstatusoutput("python3 -m pyfiglet")[0] not in [0,1]):
        os.system("pip3 install pyfiglet")
    if(subprocess.getstatusoutput("python3 -m termcolor") not in [0,1]):
        os.system("pip3 install termcolor")
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
    subprocess.getoutput("sudo apt-get install x11-xserver-utils feh cron -y")
    os.system("clear")
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
    os.system("sudo cp -r ./ldw.sh /usr/share/linuxDynamicWallpapers")
    os.system("sudo chmod +x /usr/share/linuxDynamicWallpapers/ldw.sh")
    if(os.path.exists("/usr/bin/ldw")):
        os.system("sudo rm -rf /usr/bin/ldw")
        os.system("sudo ln -s /usr/share/linuxDynamicWallpapers/ldw.sh /usr/bin/ldw")
    else:
        os.system("sudo ln -s /usr/share/linuxDynamicWallpapers/ldw.sh /usr/bin/ldw")



if __name__ == "__main__":
    checkForRoot()


