/* function validar(){
    let user = document.getElementById("username").value;
    let pass = document.getElementById("pass").value;
    if(String(user).length>=6 && String (user).length<=15){
        if(String(pass).length>=8){

        }else{
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger>  </div>"
        }
    }else{

    }
}; */

$(document).ready(function(){

    let nombre = $("#nombre");
    /* let correo = $("#correo");
    let telefono = $("#numero");
    let bici = $("#bicicleta");
    let talla = $("#talla");
    let fecha = $("#fecha"); */

    nombre.keydown(function(){
        if (String(nombre.val()).length < 3) {
            nombre.css("border", "2px solid red");
        }
    })

})
/* style="border: 2px solid red;" */