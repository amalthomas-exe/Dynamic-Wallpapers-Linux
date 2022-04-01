from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setWallpaper")
def setWallpaper():
    wallpaper = request.args.get("wallpaper").lower()
    print(wallpaper)
    os.system(f'PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin DISPLAY=:0 DESKTOP_SESSION=plasma DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/1000/bus" /usr/bin/dwall -s {wallpaper}')
    os.system(f'notify-send "Linux Dynamic Wallpapers" "Set wallpaper to {wallpaper.upper()}" ')

if __name__ == "__main__":
    app.run(debug=True)