$(document).ready(function () {
        $('#registro').validate({
            rules: {
                usuario: {
                    required: true,
                    minlength: 3
                },
                mail: {
                    required: true,
                    email: true
                },
                pass: {
                    required: true,
                    minlength: 6
                },
                confirm: {
                    required: true,
                    equalTo: "#pass"
                }
            },
            messages: {
                usuario: {
                    required: "Por favor ingresa un usuario",
                    minlength: "El usuario debe tener al menos 3 caracteres"
                },
                mail: {
                    required: "Por favor ingresa un correo electrónico",
                    email: "Por favor ingresa un correo electrónico válido"
                },
                pass: {
                    required: "Por favor ingresa una contraseña",
                    minlength: "La contraseña debe tener al menos 6 caracteres"
                },
                confirm: {
                    required: "Por favor confirma tu contraseña",
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