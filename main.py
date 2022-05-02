import datetime
from flask import Flask, render_template, request, url_for
import webview
import os
import pickle
import argparse
import multiprocessing
import subprocess

"""
The program first reads for the required info stored in the ./data/data.dat binary file.
"""
app = Flask(__name__)
parser = argparse.ArgumentParser()
parser.add_argument("--type",type=str,required=False)
args = parser.parse_args()
fr = open(r"/usr/share/linuxDynamicWallpapers/data/data.dat","rb")
data = pickle.load(fr)
fr.close()

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


def setDEWallpaper(de,style):
    if style in ["bitday","firewatch","gradient"]: #only these 3 types have .png file extension.
        type = ".png"
    else:
        type = ".jpg"

    if de in ["/usr/share/xsessions/plasma","NEON","neon","PLASMA","Plasma","plasma","KDE","Kde","kde"]: #Set Wallpaper for Plasma DE
        print("Inside",de)
        os.system("qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file:///usr/share/linuxDynamicWallpapers/images/"+style+"/"+str(datetime.datetime.now().hour)+type+"\")}'")

    elif de in ["cinnamon","Cinnamon"]: # Set Wallpaper for Cinnamon DE
        print("Inside",de)
        os.system(f"gsettings set org.cinnamon.desktop.background picture-uri \"file:///usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}"+f"{type}\"")
    
    elif de in ["Xfce Session","xfce session","XFCE","xfce","Xubuntu","xubuntu"]: #Set Wallpaper for XFCE DE
        print("Inside",de)
        SCREEN = subprocess.getoutput("echo $(xrandr --listactivemonitors | awk -F ' ' 'END {print $1}' | tr -d \:)")
        MONITOR = subprocess.getoutput("echo $(xrandr --listactivemonitors | awk -F ' ' 'END {print $2}' | tr -d \*+)")
        os.system(f"xfconf-query --channel xfce4-desktop --property /backdrop/screen{SCREEN}/monitor{MONITOR}/workspace0/last-image --set usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}"+f"{type}")
    
    elif de in ["MATE","Mate","mate"]: #Set Wallpaper for Mate DE
        print("Inside",de)
        os.system(f"gsettings set org.mate.background picture-filename usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}"+f"{type}")

    elif de in ["LXDE","Lxde","lxde"]: #Set Wallpaper for LXDE
        print("Inside",de)
        os.system("pcmanfm --set-wallpaper=\"usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}"+f"{type}\"")

    elif de in ["PANTHEON","Pantheon","pantheon","GNOME","Gnome","gnome","Gnome-xorg","gnome-xorg","UBUNTU","Ubuntu","ubuntu","DEEPIN","Deepin","deepin","POP","Pop","pop"]: #Set Wallpaper for Ubuntu, Pop, Pantheon DE
        print("Inside",de)
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file:///usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}"+f"{type}")
    
    else:
        print("Inside",de)
        os.system("feh --bg-fill usr/share/linuxDynamicWallpapers/images/{style}/{datetime.datetime.now().hour}"+f"{type}")


@app.route("/")
def index():
    return render_template("index.html") #Display the Flask Frontend.

@app.route("/setWallpaper")
def setWallpaper():
    wallpaper = request.args.get("wallpaper").lower()
    print(wallpaper)
    DE = subprocess.getoutput("echo $DESKTOP_SESSION")
    previousWallpaper = data["currentWallpaper"]
    setDEWallpaper(DE,wallpaper)
    data["DE"] = DE
    data["currentWallpaper"] = wallpaper
    fw = open("/usr/share/linuxDynamicWallpapers/data/data.dat","wb")
    pickle.dump(data,fw)
    fw.close()
    os.system(f'(crontab -u {subprocess.getoutput("whoami")} -l ; echo "* * * * * setdwl {wallpaper}") | crontab -u {subprocess.getoutput("whoami")} -') #Sets a cronjob for the wallpaper to change every hour.
    os.system(f'crontab -u {subprocess.getoutput("whoami")} -l | grep -v "{previousWallpaper}"  | crontab -u {subprocess.getoutput("whoami")} -')
    os.system("/etc/init.d/cron reload")
    os.system(f'notify-send "Linux Dynamic Wallpapers" "Set wallpaper to {wallpaper.upper()}" ')

def runServer():
    app.run()

def onclose():
    p1.kill()

if __name__ == "__main__": 
    if args.type == None: #For setting the Wallpaper using GUI
        p1 = multiprocessing.Process(target=runServer)
        p1.start()
        window = webview.create_window("Linux Dynamic Wallpapers","http://localhost:5000")
        window.closing+=onclose
        webview.start(http_server=True)
    else:
        f = open("/usr/share/linuxDynamicWallpapers/data/data.dat","rb") #For changing the wallpaper every hour, managed by setdwl.sh
        data = pickle.load(f)
        setDEWallpaper(data["DE"],args.type)
