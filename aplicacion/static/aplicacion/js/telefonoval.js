function validarTelefono() {
    var input = document.getElementById('telefono');
    var valor = input.value;
    var errorMessage = document.getElementById('error-telefono');

    // Remover caracteres no permitidos (solo números)
    var newValue = valor.replace(/\D/g, ''); // \D coincide con cualquier carácter que no sea un dígito

    // Limitar la longitud del valor a 9 caracteres
    if (newValue.length > 9) {
        newValue = newValue.slice(0, 9);
    }

    // Actualizar el valor del campo
    input.value = newValue;

    // Verificar si el campo está vacío
    if (newValue === '') {
        errorMessage.textContent = 'Ingrese un número de teléfono.';
        input.classList.add('is-invalid');
        errorMessage.style.display = 'block';
        return;
    }

    // Verificar si el número tiene exactamente 9 dígitos
    if (newValue.length !== 9) {
        errorMessage.textContent = 'El número de teléfono debe tener 9 dígitos.';
        input.classList.add('is-invalid');
        errorMessage.style.display = 'block';
    } else {
        // Si es válido, vaciar el mensaje de error
        errorMessage.textContent = '';
    }
}

function validarPrefijo() {
    var categoria = document.getElementById('prefijo');
  
    // Verificar si se ha seleccionado una categoría válida
    if (categoria.value === 'Sin Seleccionar') {
        var errorMessage = document.getElementById('error-prefijo');
        errorMessage.textContent = 'Seleccione una opcion.';
    } else {
        var errorMessage = document.getElementById('error-prefijo');
        errorMessage.textContent = ''; // Limpiar el mensaje de error si la categoría es válida
    }
  }
  