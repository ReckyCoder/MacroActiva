// Variable para mantener el contador de cotización
var contadorCotizacion = 1;

// Función para agregar una nueva fila
function agregarFila() {
    // Obtener la tabla
    var tabla = document.querySelector('table');

    // Crear una nueva fila
    var nuevaFila = document.createElement('tr');

    // Agregar HTML a la nueva fila con el número de cotización actualizado
    nuevaFila.innerHTML = `
        <td>${contadorCotizacion++}</td>
        <td>
            <select class="form-control categoria" onchange="actualizarTotal()">
                <option value="Categoria">Categoria</option>
                <option value="muebles">Muebles</option>
                <option value="electrodomesticos">Electrodomésticos</option>
                <option value="electronicos">Electrónicos</option>
                <option value="ropa">Ropa</option>
                <!-- Agrega más opciones de categoría si es necesario -->
            </select>
        </td>
        <td>
            <select class="form-control producto" onchange="actualizarTotal()">
                <option value="Producto">Producto</option>
                <option value="sillas">Sillas</option>
                <option value="mesas">Mesas</option>
                <option value="puertas">Puertas</option>
                <option value="ropero">Ropero</option>
                <!-- Agrega más opciones de productos si es necesario -->
            </select>
        </td>
        <td><input type="number" class="form-control cantidad" min="1" onchange="actualizarTotal()"></td>
        <td><input type="number" class="form-control precioUnitario" min="0" onchange="actualizarTotal()"></td>
        <td class="subtotal">$0</td>
        <td><input type="number" class="form-control descuento" min="0" max="100" onchange="actualizarTotal()"></td>
        <td class="valorDescuento">$0</td>
        <td class="total">$0</td>
        <td>
            <button type="button" class="btn btn-danger eliminar" onclick="eliminarFila(this)"> <!-- Añade la clase "eliminar" aquí -->
                <svg width="20px" height="20px" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                    <path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"/>
                </svg>
            </button>
        </td>
    `;

    // Agregar la nueva fila a la tabla
    tabla.querySelector('tbody').appendChild(nuevaFila);
    // Actualizar el total automáticamente al agregar una fila
    actualizarTotal();
    // Renumerar las filas
    renumerarFilas();
}

// Asignar el evento clic al botón de agregar fila
document.querySelector('.agregar button').addEventListener('click', agregarFila);

// Función para calcular el total de la fila y actualizar el subtotal y el total
function actualizarTotal() {
    var filas = document.querySelectorAll('tbody tr');
    var subtotal = 0;

    filas.forEach(function(fila) {
        var cantidad = parseInt(fila.querySelector(".cantidad").value) || 0;
        var precioUnitario = parseFloat(fila.querySelector(".precioUnitario").value) || 0;
        var descuentoPorcentaje = parseFloat(fila.querySelector(".descuento").value) || 0;

        var subtotalFila = cantidad * precioUnitario;
        var descuento = subtotalFila * (descuentoPorcentaje / 100);
        subtotal += subtotalFila - descuento;

        fila.querySelector(".subtotal").innerText = "$" + subtotalFila.toFixed(2);
        fila.querySelector(".valorDescuento").innerText = "$" + descuento.toFixed(2);
        fila.querySelector(".total").innerText = "$" + (subtotalFila - descuento).toFixed(2);
    });

    // Actualizar el subtotal en el div
    document.getElementById('valor-neto').innerText = "Valor neto: $" + subtotal.toFixed(2);

    // Calcular el valor del IVA
    var iva = subtotal * 0.19;

    // Actualizar el valor del IVA en el div
    document.getElementById('iva').innerText = "IVA (19%): $" + iva.toFixed(2);

    // Calcular el total con IVA
    var totalConIVA = subtotal + iva;

    // Actualizar el total con IVA en el div
    document.getElementById('total-final').innerText = "Total: $" + totalConIVA.toFixed(2);
}

// Función para eliminar la fila y actualizar el subtotal y el total
function eliminarFila(btnEliminar) {
    var fila = btnEliminar.closest('tr');
    fila.remove();
    // Actualizar el total automáticamente al eliminar una fila
    actualizarTotal();
    // Renumerar las filas
    renumerarFilas();
}

// Función para reenumerar las filas
function renumerarFilas() {
    var contador = 1;
    document.querySelectorAll('tbody tr').forEach(function(fila) {
        fila.querySelector('td:first-child').innerText = contador++;
    });
}


// Obtener la fecha de hoy
var today = new Date();
    
// Obtener el elemento de entrada de fecha
var fechaCotizacionInput = document.getElementById('fechacotizacion');

// Formatear la fecha en el formato ISO (YYYY-MM-DD)
var formattedDate = today.toISOString().split('T')[0];

// Establecer la fecha de hoy como valor inicial del campo de entrada de fecha
fechaCotizacionInput.value = formattedDate;


// formato numeros
// Función para formatear un número según el formato deseado
function formatearNumero(numero) {
    // Convertir el número a string y eliminar los puntos de separación
    var numeroSinPuntos = numero.toString().replace(/\./g, "");
    // Agregar los puntos de separación cada 3 dígitos desde la derecha
    var numeroFormateado = numeroSinPuntos.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    // Devolver el número formateado
    return "$ " + numeroFormateado;
}

// Función para actualizar el contenido de los elementos con números formateados
function actualizarNumeros() {
    // Ejemplo de números (puedes obtenerlos de donde sea necesario)
    var valorNeto = 1000000000;
    var iva = 50000000;
    var totalFinal = valorNeto + iva;

    // Formatear los números
    var valorNetoFormateado = formatearNumero(valorNeto);
    var ivaFormateado = formatearNumero(iva);
    var totalFinalFormateado = formatearNumero(totalFinal);

    // Actualizar el contenido de los elementos con los números formateados
    document.getElementById('valor-neto').textContent = "Valor neto: " + valorNetoFormateado;
    document.getElementById('iva').textContent = "IVA (19%): " + ivaFormateado;
    document.getElementById('total-final').textContent = "Total: " + totalFinalFormateado;
}

