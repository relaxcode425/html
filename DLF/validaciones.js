$.validator.setDefaults({
   submitHandler: function () {
       alert("Formulario enviado!");
   }
});

$(document).ready(function(){
   $('#rentalForm').validate({
       rules: {
           nombre: {
               required: true,
               minlength: 5
           },
           correo: {
               required: true,
               email: true
           },
           numero: {
               required: true,
               digits: true
           },
           bicicleta: {
               required: true
           },
           talla: {
               required: true,
               digits: true
           },
           fecha: {
               required: true,
               date: true
           }
       },
       messages: {           
           nombre: {
               required: "Por favor ingresa tu nombre completo",
               minlength: "Tu nombre debe tener al menos 5 caracteres"
           },
           correo: "Por favor ingresa un correo válido",
           numero: {
               required: "Por favor ingresa un número de contacto",
               digits: "Por favor ingresa solo dígitos"
           },
           bicicleta: "Por favor selecciona un tipo de bicicleta",
           talla: {
               required: "Por favor ingresa una talla",
               digits: "Por favor ingresa solo dígitos"
           },
           fecha: "Por favor ingresa una fecha válida"
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
