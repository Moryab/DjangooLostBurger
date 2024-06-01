//Ingreso Admin
document.addEventListener('DOMContentLoaded', function () {
  var loginForm = document.querySelector('.login__form');

  loginForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Previene el envío tradicional del formulario

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    // Establece las credenciales correctas aquí
    var correctEmail = 'lostburger@gmail.com';
    var correctPassword = 'Burger123';

    // Comprueba si las credenciales son correctas
    if (email === correctEmail && password === correctPassword) {
      window.location.href = 'admin.html#panel'; // Redirecciona a admin.html#panel
    } else {
      alert('Credenciales incorrectas, intente de nuevo.'); // Muestra un mensaje de error
    }
  });
});
//Recuperar contraseña
function recuperarPass(event) {
  event.preventDefault(); // Evitar que el formulario se envíe realmente
  alert("Se ha enviado una verificación a su correo.");
  window.location.href = 'login.html'; // Redirigir a la página login.html después de aceptar el alerta
}

document.addEventListener("DOMContentLoaded", function () {
  var recuperarButton = document.getElementById("recuperar");
  recuperarButton.addEventListener("click", recuperarPass);
});
