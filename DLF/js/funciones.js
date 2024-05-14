function validar(){
    let user = document.getElementById("username").value;
    let pass = document.getElementById("pass").value;
    if(String(user).length>=6 && String (user).length<=15){
        if(String(pass).length>=8){

        }else{
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger>  </div>"
        }
    }else{

    }
}