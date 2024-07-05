$(document).ready(function () {
    $('#registro').validate({
        rules: {
            username: {
                required: true,
                minlength: 3
            },
            rut: {
                required: true,
                minlength: 10,
                maxlength: 10
            },
            first_name: {
                required: true,
                minlength: 3
            },
            last_name: {
                required: true,
                minlength: 3
            },
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 6
            },
            confirm: {
                required: true,
                equalTo: "#password"
            }
        },
        messages: {
            usuario: {
                required: "Por favor ingresa un usuario",
                minlength: "El usuario debe tener al menos 3 caracteres"
            },
            rut: {
                required: "Ingrese un rut",
                minlength: "Ingrese el rut en formato: 01234567-8",
                maxlength: "Ingrese el rut en formato: 01234567-8"
            },
            first_name: {
                required: "Ingrese un nombre",
                minlength: "El nombre debe tener al menos 3 caracteres"
            },
            last_name: {
                required: "Ingrese un apellido",
                minlength: "El apellido debe tener al menos 3 caracteres"
            },
            email: {
                required: "Por favor ingresa un correo electrónico",
                email: "Por favor ingresa un correo electrónico válido"
            },
            password: {
                required: "Por favor ingresa una contraseña",
                minlength: "La contraseña debe tener al menos 6 caracteres"
            },
            confirm: {
                required: "Por favor",
                equalTo: "Las contraseñas no coinciden"
            }
        },
        errorElement: 'div',
        errorPlacement: function (error, element) {
            error.addClass('invalid-feedback');
            element.closest('.form-floating').append(error);
        },
        highlight: function (element, errorClass, validClass) {
            $(element).addClass('is-invalid');
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).removeClass('is-invalid');
        }
    });
});