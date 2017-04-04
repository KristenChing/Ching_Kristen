function validate(){
    var x = document.forms.input.username.value;
    var y = document.forms.input.password.value;
    var atVal = x.indexOf("@");
    var dotVal = x.lastIndexOf(".");
    
    if((atVal < 1 || dotVal < atVal + 2)&&(y.length < 6))
        alert("Error: invalid email. Error: password is too short.");
    else {
        if (atVal < 1 || dotVal < atVal + 2)
            alert("Error: invalid email.");
        else if (y.length < 6)
            alert("Error: password is too short. Your password must be a minimum of 6 characters!");
        else
            alert("Success!")
    }

}