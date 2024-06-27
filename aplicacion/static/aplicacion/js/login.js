//Ingreso Admin
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
