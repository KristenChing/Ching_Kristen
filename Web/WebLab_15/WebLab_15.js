function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    canvas.beginPath();
    canvas.moveTo(70, 90);
    canvas.lineTo(220, 140);
    canvas.lineTo(250, 0);
    canvas.lineTo(295, 140);
    canvas.lineTo(460, 80);
    canvas.lineTo(350, 200);
    canvas.lineTo(500, 240);
    canvas.lineTo(350, 270);
    canvas.lineTo(460, 410);
    canvas.lineTo(300, 320);
    canvas.lineTo(260, 480);
    canvas.lineTo(220, 320);
    canvas.lineTo(50, 400);
    canvas.lineTo(180, 270);
    canvas.lineTo(20, 250);
    canvas.lineTo(180, 200);
    canvas.lineTo(70, 90);
    canvas.stroke();
    canvas.closePath();
    var gradient = canvas.createLinearGradient(0, 0 , 900, 900);
    gradient.addColorStop(0, "purple");
    gradient.addColorStop(0.26, "lightgrey");
    gradient.addColorStop(.5, "yellow");
    canvas.fillStyle = gradient;
    canvas.fill();

}

window.addEventListener("load", shapes, false);