function drag(){
    k = document.getElementById("img");
    leftBox = document.getElementById("left");
    k.addEventListener("dragstart", start, false);
    k.addEventListener("dragend", end, false);
    leftBox.addEventListener("dragenter", enter, false);
    leftBox.addEventListener("dragleave",  leave, false);
    leftBox.addEventListener("dragover", over, false);
    leftBox.addEventListener("drop", drop, false);
}

function start (e){
    var img = '<img id = "img" src = "image.jpg" height = "200" width = "200">';
    e.dataTransfer.setData("image", img);
    e.target.style.opacity = "0.5";
}

function enter (e) {
    e.preventDefault();
    leftBox.style.background = "#42d100";
    leftBox.style.border = "3px solid green";

}

function leave (e){
    e.preventDefault();
    leftBox.style.background = "white";
    leftBox.style.border = "3px solid blue";
}

function end(e){
    e.target.style.visibility = "hidden";
}

function over(e){
    e.preventDefault();
    leftBox.style.background = "#42d100";
    leftBox.style.border = "3px solid green";
}

function drop(e){
    e.preventDefault();
    leftBox.style.background = "white";
    leftBox.style.border = "3px solid blue";
    left.innerHTML = e.dataTransfer.getData("image");
}
window.addEventListener("load", drag, false);