import datetime
from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

def setDEWallpaper(de,style):
    if de=="plasma":
        os.system("qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file:///usr/share/linuxDynamicWallpapers/images/"+style+"/"+str(datetime.datetime.now().hour)+".jpg\")}'")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setWallpaper")
def setWallpaper():
    wallpaper = request.args.get("wallpaper").lower()
    print(wallpaper)
    setDEWallpaper("plasma",wallpaper)
    #os.system(f'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin DISPLAY=:0 DESKTOP_SESSION=plasma DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" /usr/bin/dwall -s {wallpaper}')
    os.system(f'notify-send "Linux Dynamic Wallpapers" "Set wallpaper to {wallpaper.upper()}" ')

if __name__ == "__main__":
    app.run(debug=True)