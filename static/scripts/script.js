const backgrounds = document.getElementById("backgrounds")

const availableBackgrounds = [{id:"aurora",name:"Aurora",image:"images/aurora.jpg"},{id:"beach",name:"Beach",image:"images/beach.jpg"},{id:"bitday",name:"Bitday",image:"images/bitday.png"},{id:"catalina",name:"Catalina",image:"images/catalina.jpg"},{id:"chihuahuan",name:"Chihuahuan",image:"images/chihuahuan.jpg"},{id:"cliffs",name:"Cliffs",image:"images/cliffs.jpg"},{id:"colony",name:"Colony",image:"images/colony.jpg"},{id:"desert",name:"Desert",image:"images/desert.jpg"},{id:"earth",name:"Earth",image:"images/earth.jpg"},{id:"exodus",name:"Exodus",image:"images/exodus.jpg"},{id:"Factory",name:"Factory",image:"images/factory.jpg"},{id:"firewatch",name:"Firewatch",image:"images/firewatch.jpg"},{id:"forest",name:"Forest",image:"images/forest.jpg"},{id:"gradient",name:"Gradient",image:"images/gradient.png"},{id:"home",name:"Home",image:"images/home.jpg"},{id:"island",name:"Island",image:"images/island.jpg"},{id:"lake",name:"Lake",image:"images/lake.jpg"},{id:"lakeside",name:"Lakeside",image:"images/lakeside.jpg"},{id:"london",name:"London",image:"images/london.jpg"},{id:"maldives",name:"Maldives",image:"images/maldives.jpg"},{id:"market",name:"Market",image:"images/market.jpg"},{id:"mojave",name:"Mojave",image:"images/mojave.jpg"},{id:"mojave_HD",name:"Mojave HD",image:"images/mojave_HD.jpg"},{id:"moon",name:"Moon",image:"images/moon.jpg"},{id:"mountains",name:"Mountains",image:"images/mountains.jpg"},{id:"mount_fuji",name:"Mount Fuji",image:"images/mount_fuji.jpg"},{id:"room",name:"Room",image:"images/room.jpg"},{id:"sahara",name:"Sahara",image:"images/sahara.jpg"},{id:"seoul",name:"Seoul",image:"images/seoul.jpg"},{id:"street",name:"Street",image:"images/street.jpg"},{id:"tokyo",name:"Tokyo",image:"images/tokyo.jpg"}]

let availableBackgroundsHTML = ""

availableBackgrounds.forEach((background)=>{
    availableBackgroundsHTML+=`<div id="${background.id}" class="box" style="overflow:hidden;border-radius: 25px"><div  style="
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
