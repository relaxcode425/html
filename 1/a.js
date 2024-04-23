function sumar(){
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    
    let suma = Number(num1) + Number(num2);
    /* console.log("Num 1: "+num1+"|| Num 2: "+num2);
    console.log("suma: "+suma); */
    document.getElementById("resultado").innerHTML = "<p>La suma: "+suma+"</p>";
}