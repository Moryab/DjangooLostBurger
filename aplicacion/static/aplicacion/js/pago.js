// Función para formatear el número de tarjeta
function formatTarjeta() {
    document.getElementById('tarjeta').addEventListener('input', function (e) {
        var target = e.target;
        var input = target.value.replace(/\D/g, '').substring(0, 16);
        target.value = input.replace(/([0-9]{4})/g, '$1 ').trim();
    });
}

// Función para manejar el envío del formulario y mostrar un mensaje de éxito
function msjPago() {
    // Obtener todos los campos del formulario
    var fname = document.getElementById("fname").value;
    var email = document.getElementById("email").value;
    var address = document.getElementById("address").value;
    var city = document.getElementById("city").value;
    var cardname = document.getElementById("cardname").value;
    var tarjeta = document.getElementById("tarjeta").value;
    var expyear = document.getElementById("expyear").value;
    var cvv = document.getElementById("cvv").value;


    // Verificar si algún campo está vacío
    if (fname === "" || email === "" || address === "" || city === "" || cardname === "" || tarjeta === "" || expyear === "" || cvv === "") {
        alert("Por favor, complete todos los campos antes de enviar el formulario.");
        return; // No continuar si hay campos vacíos
    }
    alert("Su pago a sido un éxito.");
    window.location.href = 'index.html'; // Redirigir a la página index.html después de aceptar la alerta
}

document.getElementById("pagar").addEventListener("click", msjPago);
//Validar textos
function validarfname() {
    var input = document.getElementById('fname');
    var valor = input.value;

    // Eliminar caracteres no permitidos (no alfabéticos)
    var newValue = valor.replace(/[^a-zA-Z\s]/g, '');

    // Actualizar el valor del campo de entrada
    input.value = newValue;
}

document.addEventListener("DOMContentLoaded", function () {
    var inputNombre = document.getElementById('fname');

    inputNombre.addEventListener('input', validarfname);
});

function validarCiudad() {
    var input = document.getElementById('city');
    var valor = input.value;

    // Eliminar caracteres no permitidos (no alfabéticos)
    var newValue = valor.replace(/[^a-zA-Z\s]/g, '');

    // Actualizar el valor del campo de entrada
    input.value = newValue;
}

document.addEventListener("DOMContentLoaded", function () {
    var inputNombre = document.getElementById('city');

    inputNombre.addEventListener('input', validarCiudad);
});

function validarCardname() {
    var input = document.getElementById('cardname');
    var valor = input.value;

    // Eliminar caracteres no permitidos (no alfabéticos)
    var newValue = valor.replace(/[^a-zA-Z\s]/g, '');

    // Actualizar el valor del campo de entrada
    input.value = newValue;
}

document.addEventListener("DOMContentLoaded", function () {
    var inputNombre = document.getElementById('cardname');

    inputNombre.addEventListener('input', validarCardname);
});

//validacion correo
function validarEmail() {
    var input = document.getElementById('email');
    var valor = input.value;
  
    if (!valor.includes('@')) {
        input.setCustomValidity('El correo electrónico debe contener "@".');
    } else {
        input.setCustomValidity('');
    }
  }

//
function validarDireccion() {
    var input = document.getElementById('address');
    var valor = input.value;
  
    // Eliminar caracteres no permitidos (solo números y letras)
    var newValue = valor.replace(/[^a-zA-Z0-9\s]/g, '');
    // Actualizar el valor del campo de entrada
    input.value = newValue;
  }
// Validar EXPYEAR
function validarFechaExpiracion() {
    var input = document.getElementById('expyear');
    var valor = input.value;
  
    // Eliminar caracteres no permitidos (solo números y "/")
    var newValue = valor.replace(/[^0-9/]/g, '');
  
    // Si se ingresa el tercer número y no hay "/", agregar automáticamente "/"
    if (newValue.length === 3 && valor.length <= 3 && valor.charAt(2) !== '/') {
      newValue = newValue.slice(0, 2) + '/' + newValue.slice(2);
    }
  
    // Limitar la longitud a 5 caracteres
    newValue = newValue.slice(0, 5);
  
    // Actualizar el valor del campo de entrada
    input.value = newValue;
  }
//Validadr CVV
function validarCVV() {
    var input = document.getElementById('cvv');
    var valor = input.value;
  
    // Eliminar caracteres no permitidos (solo números)
    var newValue = valor.replace(/\D/g, '');
  
    // Limitar la longitud a 3 caracteres
    newValue = newValue.slice(0, 3);
  
    // Actualizar el valor del campo de entrada
    input.value = newValue;
  }
  