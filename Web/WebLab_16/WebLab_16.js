function mouse()
{
    var z = document.getElementById("canvas");
    canvas = z.getContext("2d");
    window.addEventListener("mousemove",image,false);

}

function image(e)
{
    canvas.clearRect(0,0,1000,1000);
    var pic = new Image();
    pic.src = "image.jpg";
    var x = e.clientX;
    var y = e.clientY;
    canvas.drawImage(pic, x, y, 200, 200);
}
window.addEventListener("load", mouse, false);