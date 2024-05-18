$.validator.setDefaults({
    submitHandler: function () {
        alert("Formulario enviado!");
    }
 });
 
 $(document).ready(function(){
    $('#login').validate({
        rules: {
            mail: {
                required: true,
                email: true
            },
            pass: {
                required: true,
                minlength: 8
            }
        },
        messages: {           
            pass: {
                required: "Ingresa tu contraseña",
                minlength: "Tu contraseña debe tener minimo 8 caracteres"
            },
            correo: "Por favor ingresa un correo válido"
        },
        errorElement: "em",
        errorPlacement: function (error, element) {
            error.addClass("help-block");
            if (element.prop("type") === "checkbox" || element.prop("type") === "radio") {
                error.insertAfter(element.parent("label"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function (element, errorClass, validClass) {
            $(element).parents(".col-sm-10").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).parents(".col-sm-10").addClass("has-success").removeClass("has-error");  
        }
    });
 });
 