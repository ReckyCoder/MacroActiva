 // Función para actualizar el estado seleccionado
 function actualizarEstado(estado, icono) {
    // Actualizar el texto del botón
    document.querySelector('.dropdown-toggle').textContent = estado;
    
    // Actualizar el icono seleccionado
    var iconoSeleccionado = document.getElementById('icono-seleccionado');
    iconoSeleccionado.innerHTML = icono;
}

function editarNumeroOrden() {
    var numeroOrdenInput = document.getElementById('numeroOrden');
    numeroOrdenInput.readOnly = false; // Permite editar el número de orden
    numeroOrdenInput.focus(); // Coloca el cursor en el input para facilitar la edición
}

// Obtener la fecha de hoy
var today = new Date();
    
// Obtener el elemento de entrada de fecha
var fechaCotizacionInput = document.getElementById('fechacotizacion');

// Formatear la fecha en el formato ISO (YYYY-MM-DD)
var formattedDate = today.toISOString().split('T')[0];

// Establecer la fecha de hoy como valor inicial del campo de entrada de fecha
fechaCotizacionInput.value = formattedDate;


