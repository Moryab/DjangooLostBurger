document.addEventListener("DOMContentLoaded", function() {
    var deleteButtons = document.querySelectorAll(".btn-confirmar");

    deleteButtons.forEach(function(button) {
        button.addEventListener("click", function(e) {
            e.preventDefault();
            showConfirmationModal(e);
        });
    });
});

function showConfirmationModal(event) {
    var form = event.currentTarget.closest("form");
    Swal.fire({
        title: "¿Está seguro que desea eliminar este producto?",
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
            form.submit();
        }
    });
}
