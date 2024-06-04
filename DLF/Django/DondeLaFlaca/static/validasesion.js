$.validator.setDefaults({
    submitHandler: function () {
        alert("Formulario enviado!");
    }
 });
 
 $(document).ready(function(){
    $('#login').validate({
        rules: {
            usuario: {
                required: true
            },
            pass: {
                required: true,
                minlength: 6
            }
        },
        messages: {           
            pass: {
                required: "Ingresa tu contraseña",
                minlength: "Tu contraseña debe tener minimo 8 caracteres"
            },
            usuario: {
                required: "Por favor ingresa un usuario válido"
            }
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

    /* $('#registro').validate({
        rules: {
            usuario: {
                required: true
            },
            mail: {
                required: true,
                email: true
            },
            pass: {
                required: true,
                minlength: 8,
                contieneMayuscula: true,
                contieneNumero: true
            },
            confirm: {
                required: true,
                equalTo: '#pass',
                minlength: 8,
                contieneMayuscula: true,
                contieneNumero: true
            }
        },
        messages: {           
            usuario: {
                required: "Por favor ingresa un usuario válido"
            },
            mail: {
                required: "Por favor ingresa un correo",
                email: "Por favor ingresa un correo válido"
            },
            pass: {
                required: "Ingresa tu contraseña",
                minlength: "Tu contraseña debe tener minimo 8 caracteres",
                contieneMayuscula: "La contraseña debe contener al menos una letra mayúscula",
                contieneNumero: "La contraseña debe contener al menos un número"
            },
            confirm: {
                required: "Ingresa tu contraseña",
                equalTo: "Las contraseñas no coinciden",
                minlength: "Tu contraseña debe tener minimo 8 caracteres",
                contieneMayuscula: "La contraseña debe contener al menos una letra mayúscula",
                contieneNumero: "La contraseña debe contener al menos un número"
            }

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
        },
        addMethods: function() {
            jQuery.validator.addMethod("contieneMayuscula", (value, element) => {
                return /[A-Z]/.test(value); // Verifica si hay al menos una letra mayúscula
            }, "La contraseña debe contener al menos una letra mayúscula");
            jQuery.validator.addMethod("contieneNumero", (value, element) => {
                return /\d/.test(value); // Verifica si hay al menos un número
            }, "La contraseña debe contener al menos un número");
        }
    }); */

 });
 