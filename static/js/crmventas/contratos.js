// trasladando ordenes para generar contrato
function moveToOtherCard(element) {
    var otherCard = document.querySelector('.ordenes2 .card');
    otherCard.appendChild(element);
    element.onclick = function() {
        moveToOtherCardBack(this);
    };
}

function moveToOtherCardBack(element) {
    var originalCard = document.querySelector('.ordenes1 .card');
    originalCard.appendChild(element);
    element.onclick = function() {
        moveToOtherCard(this);
    };
}

// Obtener la fecha de hoy
var today = new Date();
    
// Obtener el elemento de entrada de fecha
var fechacontratoInput = document.getElementById('fechacontrato');

// Formatear la fecha en el formato ISO (YYYY-MM-DD)
var formattedDate = today.toISOString().split('T')[0];

// Establecer la fecha de hoy como valor inicial del campo de entrada de fecha
fechacontratoInput.value = formattedDate;

// funcion actualizar estado
function cambiarEstado() {
    var selectElement = document.getElementById("estadoContrato");
    var selectedValue = selectElement.options[selectElement.selectedIndex].value;
    document.getElementById("estadoContratoButton").innerText = selectedValue;
}


// Función para manejar el clic en el ícono y generar el PDF
function generarPDF() {
    // Crear una instancia de jsPDF
    var doc = new jsPDF();
    
    // Agregar contenido al PDF
    doc.text('¡Hola, este es tu PDF!', 10, 10);
    
    // Obtener los datos del PDF como una cadena de datos
    var pdfData = doc.output('datauristring');
    
    // Abrir el PDF en una nueva pestaña del navegador
    window.open(pdfData);
    window.jsPDF = window.jspdf.jsPDF;
}

