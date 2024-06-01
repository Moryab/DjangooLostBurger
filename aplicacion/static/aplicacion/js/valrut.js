function validarRut(rut) {
    // Eliminar puntos y guiones del RUT y convertir a mayúsculas si hay letras
    rut = rut.replace(/[.-]/g, '').toUpperCase();

    // Verificar que el RUT tenga el formato correcto
    if (!/^\d{1,3}(\.\d{3})*-\d$/.test(rut)) {
        return false;
    }

    // Verificar la longitud del RUT
    if (rut.length !== 9) {
        return false;
    }

    // Separar el cuerpo del RUT y el dígito verificador
    var cuerpo = rut.slice(0, -2);
    var dv = rut.slice(-1);

    // Verificar que el cuerpo del RUT sea un número válido
    if (isNaN(cuerpo)) {
        return false;
    }

    // Calcular el dígito verificador esperado
    var suma = 0;
    var multiplicador = 2;
    for (var i = cuerpo.length - 1; i >= 0; i--) {
        suma += parseInt(cuerpo.charAt(i)) * multiplicador;
        multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
    }
    var resto = suma % 11;
    var dvEsperado = resto === 0 ? 0 : resto === 1 ? 'K' : 11 - resto;

    // Verificar que el dígito verificador ingresado coincida con el dígito verificador esperado
    if (dvEsperado.toString() !== dv) {
        return false;
    }

    // Si pasa todas las verificaciones, el RUT es válido
    return true;
}
