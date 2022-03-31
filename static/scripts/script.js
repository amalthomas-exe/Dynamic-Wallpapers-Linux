const backgrounds = document.getElementById("backgrounds")

const availableBackgrounds = [{name:"Aurora",image:"images/aurora.jpg"},{name:"Beach",image:"images/beach.jpg"},{name:"Bitday",image:"images/bitday.png"},{name:"Chihuahuan",image:"images/chihuahuan.jpg"},{name:"Cliffs",image:"images/cliffs.jpg"},{name:"Colony",image:"images/colony.jpg"},{name:"Desert",image:"images/desert.jpg"},{name:"Earth",image:"images/earth.jpg"},{name:"Exodus",image:"images/exodus.jpg"},{name:"Factory",image:"images/factory.jpg"},{name:"Firewatch",image:"images/firewatch.jpg"},{name:"Forest",image:"images/forest.jpg"},{name:"Gradient",image:"images/gradient.png"},{name:"Home",image:"images/home.jpg"},{name:"Island",image:"images/island.jpg"},{name:"Lake",image:"images/lake.jpg"},{name:"Lakeside",image:"images/lakeside.jpg"},{name:"Market",image:"images/market.jpg"},{name:"Mojave",image:"images/mojave.jpg"},{name:"Moon",image:"images/moon.jpg"},{name:"Mountains",image:"images/mountains.jpg"},{name:"Room",image:"images/room.jpg"},{name:"Sahara",image:"images/sahara.jpg"},{name:"Street",image:"images/street.jpg"},{name:"Tokyo",image:"images/tokyo.jpg"}]

let availableBackgroundsHTML = ""

availableBackgrounds.forEach((background)=>{
    availableBackgroundsHTML+=`<div id="${background.name}" class="box" style="overflow:hidden;border-radius: 25px"><div  style="
    background-image: url('/static/${background.image}');
    background-size: cover;
    border-radius:25px;
    padding-top: 20%;
    padding-bottom: 20%;
    margin-bottom: 20px;
    margin-top:20px;
    text-align: center;" class="backgroundView"><div class="title">${background.name}</div></div></div>`
})

backgrounds.innerHTML= availableBackgroundsHTML;

document.querySelectorAll(".box").forEach((element)=>{
    document.getElementById(element.getAttribute("id")).onclick = ()=>{
        $.get("/setWallpaper",{wallpaper: element.getAttribute("id")}).done((data)=>{
            alert(`Task ${(data)?"Success":"Failed"}`);
        })
    }
})
