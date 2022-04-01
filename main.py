import datetime
from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

def setDEWallpaper(de,style):
    if style in ["bitday","firewatch","gradient"]:
        type = ".png"
    else:
        type = ".jpg"

    if de in ["/usr/share/xsessions/plasma","NEON","neon","PLASMA","Plasma","plasma","KDE","Kde","kde"]:
        print("Inside",de)
        os.system("qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file:///usr/share/linuxDynamicWallpapers/images/"+style+"/"+str(datetime.datetime.now().hour)+type+"\")}'")

    elif de in ["cinnamon","Cinnamon"]:
        print("Inside",de)
        os.system(f"gsettings set org.cinnamon.desktop.background picture-uri \"file:///usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}""{type}\"")
    
    elif de in ["Xfce Session","xfce session","XFCE","xfce","Xubuntu","xubuntu"]:
        print("Inside",de)
        SCREEN = subprocess.getoutput("echo $(xrandr --listactivemonitors | awk -F ' ' 'END {print $1}' | tr -d \:)")
        MONITOR = subprocess.getoutput("echo $(xrandr --listactivemonitors | awk -F ' ' 'END {print $2}' | tr -d \*+)")
        os.system(f"xfconf-query --channel xfce4-desktop --property /backdrop/screen{SCREEN}/monitor{MONITOR}/workspace0/last-image --set usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}""{type}")
    
    elif de in ["MATE","Mate","mate"]:
        print("Inside",de)
        os.system(f"gsettings set org.mate.background picture-filename usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}""{type}")

    elif de in ["LXDE","Lxde","lxde"]:
        print("Inside",de)
        os.system("pcmanfm --set-wallpaper=\"usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}""{type}\"")

    elif de in ["PANTHEON","Pantheon","pantheon","GNOME","Gnome","gnome","Gnome-xorg","gnome-xorg","UBUNTU","Ubuntu","ubuntu","DEEPIN","Deepin","deepin","POP","Pop","pop"]:
        print("Inside",de)
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file:///usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}""{type}")
    
    else:
        print("Inside",de)
        os.system("feh --bg-fill usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}""{type}")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setWallpaper")
def setWallpaper():
    wallpaper = request.args.get("wallpaper").lower()
    print(wallpaper)
    DE = subprocess.getoutput("echo $DESKTOP_SESSION")
    setDEWallpaper("plasma",wallpaper)
    #os.system(f'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin DISPLAY=:0 DESKTOP_SESSION=plasma DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" /usr/bin/dwall -s {wallpaper}')
    os.system(f'notify-send "Linux Dynamic Wallpapers" "Set wallpaper to {wallpaper.upper()}" ')

if __name__ == "__main__":
    app.run(debug=True)