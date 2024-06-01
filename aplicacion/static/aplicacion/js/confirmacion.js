document.addEventListener("DOMContentLoaded", function() {
    // Selecciona todos los botones con la clase 'btn-confirmar'
    var deleteButtons = document.querySelectorAll(".btn-confirmar");

    // Añade un manejador de eventos a cada botón
    deleteButtons.forEach(function(button) {
        button.addEventListener("click", function(e) {
            e.preventDefault();
            showConfirmationModal(e);
        });
    });
});

function showConfirmationModal(event) {
    var url = event.currentTarget.getAttribute("href");
    Swal.fire({
        title: "¿Está seguro que desea eliminar este registro?",
        text: "Esta operación es irreversible",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar",
        buttonsStyling: false,
        customClass: {
            confirmButton: 'btn-confirm',
            cancelButton: 'btn-cancel'
        }
    }).then((result) => {
        if (result.isConfirmed) {
            // Aquí puedes realizar la acción de eliminación
            // Por ejemplo, redirigir a la página de eliminación
            window.location.href = "eliminarprod.html";
        }
    });
}
