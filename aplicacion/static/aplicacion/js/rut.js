// Contenido de rutFormatter.js
function formatearRutInput() {
  document.getElementById('rutInput').addEventListener('input', function() {
      var rutInput = this.value.replace(/[^\dkK0-9]/g, ''); // Eliminar caracteres no válidos, incluyendo puntos
      rutInput = rutInput.slice(0, 9); // Limitar a 9 caracteres incluyendo el dígito verificador

      // Formatear el RUT solo si se ha ingresado completamente
      if (rutInput.length >= 2) {
          var rutFormateado = '';

          // Agregar puntos al RUT
          for (var i = 0; i < rutInput.length - 1; i++) {
              rutFormateado += rutInput[i];
              if ((rutInput.length - i - 2) % 3 === 0 && i !== rutInput.length - 2) {
                  rutFormateado += '.';
              }
          }

          // Agregar el guion y el dígito verificador
          rutFormateado += '-' + rutInput.charAt(rutInput.length - 1).toUpperCase();

          // Actualizar el valor del input con el RUT formateado
          this.value = rutFormateado;
      } else {
          this.value = rutInput; // Si el RUT es corto, dejarlo sin formato
      }
  });
}

// Llamada a la función para formatear el RUT al cargar la página
document.addEventListener('DOMContentLoaded', formatearRutInput);
