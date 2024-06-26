// validacion Nombre en adddprouc y edit validarCardname
function validarNombre() {
  var input = document.getElementById('nombre');
  var valor = input.value;
  
  // Verificar si el campo está vacío
  if (valor.trim() === '') {
      var errorMessage = document.getElementById('error-nombre');
      errorMessage.textContent = 'El campo no puede estar vacío.';
      return;
  }
  
  // Remover caracteres no alfabéticos y no espacios en blanco
  var newValue = valor.replace(/[^A-Za-z\s]/g, '');
  
  // Verificar si el valor ingresado contiene caracteres no alfabéticos
  if (valor !== newValue) {
      input.value = newValue;
      var errorMessage = document.getElementById('error-nombre');
      errorMessage.textContent = 'Ingrese solo letras.';
  } else {
      var errorMessage = document.getElementById('error-nombre');
      errorMessage.textContent = ''; // Limpiar el mensaje de error si el nombre es válido
  }
}
//Validacion apellido en editUser
function validarApellido() {
  var input = document.getElementById('apellido');
  var valor = input.value;
  
  // Verificar si el campo está vacío
  if (valor.trim() === '') {
      var errorMessage = document.getElementById('error-apellido');
      errorMessage.textContent = 'El campo no puede estar vacío.';
      return;
  }
  
  // Remover caracteres no alfabéticos y no espacios en blanco
  var newValue = valor.replace(/[^A-Za-z\s]/g, '');
  
  // Verificar si el valor ingresado contiene caracteres no alfabéticos
  if (valor !== newValue) {
      input.value = newValue;
      var errorMessage = document.getElementById('error-apellido');
      errorMessage.textContent = 'Ingrese solo letras.';
  } else {
      var errorMessage = document.getElementById('error-apellido');
      errorMessage.textContent = ''; // Limpiar el mensaje de error si el nombre es válido
  }
}

//validacion Descripcion en adddprouc y edit
function validarDescripcion() {
  var input = document.getElementById('descripcion');
  var valor = input.value;
  
  // Verificar si el campo está vacío
  if (valor.trim() === '') {
      var errorMessage = document.getElementById('error-descripcion');
      errorMessage.textContent = 'El campo no puede estar vacío.';
      return;
  }
  
  // Verificar si el valor ingresado contiene caracteres no alfabéticos
  if (valor !== newValue) {
      input.value = newValue;
      var errorMessage = document.getElementById('error-descripcion');
      errorMessage.textContent = 'Ingrese solo letras.';
  } else {
      var errorMessage = document.getElementById('error-descripcion');
      errorMessage.textContent = ''; // Limpiar el mensaje de error si el nombre es válido
  }
}

//validacion Precio en adddprouc y edit
function validarPrecio() {
  var input = document.getElementById('precio');
  var valor = input.value;
  
  // Verificar si se ha ingresado un valor en el campo de entrada (ignorando el símbolo "$")
  if (valor.trim() === '' || valor === '$') {
      var errorMessage = document.getElementById('error-precio');
      errorMessage.textContent = 'Ingrese un precio.';
      return; // Salir de la función si el campo está vacío
  }
  // Remover caracteres no permitidos (solo números)
  var newValue = valor.replace(/\D/g, ''); // \D coincide con cualquier carácter que no sea un dígito

  // Convertir el valor a un número
  var numero = parseFloat(newValue);

  // Verificar si el precio es mayor que cero
  if (numero > 0) {
      // Agregar el símbolo "$" al principio del valor
      newValue = '$' + newValue;

      input.value = newValue;

      // Si es válido, vaciar el mensaje de error
      var errorMessage = document.getElementById('error-precio');
      errorMessage.textContent = '';
  } else {
      // Si el precio no es válido, limpiar el campo de entrada y mostrar mensaje de error
      input.value = '';
      var errorMessage = document.getElementById('error-precio');
      errorMessage.textContent = 'El precio debe ser mayor que cero.';
  }
}


//Validar Categoria
function validarCategoria() {
  var categoria = document.getElementById('categoria');

  // Verificar si se ha seleccionado una categoría válida
  if (categoria.value === 'Sin Seleccionar') {
      var errorMessage = document.getElementById('error-categoria');
      errorMessage.textContent = 'Seleccione una categoría.';
  } else {
      var errorMessage = document.getElementById('error-categoria');
      errorMessage.textContent = ''; // Limpiar el mensaje de error si la categoría es válida
  }
}



//validacion Imagenes en adddprouc y edit
function validarImagen() {
  var input = document.getElementById('imagen');
  var file = input.files[0];
  var allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];

  if (file && allowedTypes.includes(file.type)) {
      // La selección de archivo es una imagen permitida
      input.setCustomValidity('');
  } else {
      // La selección de archivo no es una imagen permitida
      input.setCustomValidity('Seleccione una imagen válida (JPEG, PNG, GIF, WEBP).');
  }
}

//validacion correo en editUser
function validarEmail() {
  var input = document.getElementById('email');
  var valor = input.value;

  if (!valor.includes('@')) {
      input.setCustomValidity('El correo electrónico debe contener "@".');
  } else {
      input.setCustomValidity('');
  }
}

// Confirmacion de registro de usuario
function mostrarAlerta() {
  var nombre = document.getElementById('nombre').value;
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;

  if (nombre === '' || email === '' || password === '') {
      alert('Por favor, llene todos los campos antes de enviar el formulario.');
      return; // No continuar si hay campos vacíos
  }

  alert("Se ha registrado con éxito.");
  window.location.href = 'admin.html#usuarios'; // Redirigir a la página index.html después de aceptar la alerta
}

document.getElementById("registrarbtn").addEventListener("click", mostrarAlerta);


//Validacion de contraseña
function validarContrasena() {
  var contrasena = document.getElementById('password').value;
  var errorpass = document.getElementById('errorpass');

  if (!/[A-Z]/.test(contrasena)) {
      errorpass.textContent = 'La contraseña debe contener al menos una letra mayúscula.';
      return false; // Devuelve falso si la validación falla
  } else {
      errorpass.textContent = ''; // Limpiar el mensaje de error si la validación es exitosa
  }

  return true; // Devuelve verdadero si la validación es exitosa
}

