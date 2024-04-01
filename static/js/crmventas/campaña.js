document.addEventListener('DOMContentLoaded', function() {
    var inputField = document.getElementById('inputcanalesmark');
    var canalesMarketing = document.getElementById('canalesMarketing');
    var contador = 1; // Inicializar el contador

    inputField.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            var inputText = inputField.value.trim();
            if (inputText !== "") {
                var newSpan = document.createElement('span');
                newSpan.classList.add('font-weight-normal');
                newSpan.textContent = contador + ". " + inputText;
                contador++; // Incrementar el contador

                // Añadir el nuevo span al contenedor
                canalesMarketing.appendChild(newSpan);

                // Agregar un espacio después del span
                var space = document.createTextNode(" ");
                canalesMarketing.appendChild(space);

                // Agregar otro espacio después del primero
                var space2 = document.createTextNode(" ");
                canalesMarketing.appendChild(space2);

                // Limpiar el campo de entrada
                inputField.value = "";

                // Agregar el controlador de eventos para eliminar el span
                newSpan.addEventListener('click', function() {
                    var confirmDelete = confirm("¿Estás seguro de que deseas eliminar este elemento?");
                    if (confirmDelete) {
                        canalesMarketing.removeChild(newSpan);
                        canalesMarketing.removeChild(space); // Eliminar el primer espacio
                        canalesMarketing.removeChild(space2); // Eliminar el segundo espacio
                        reorganizarNumeracion(); // Reorganizar numeración
                    }
                });
            }
            event.preventDefault();
        }
    });

    // Función para reorganizar la numeración después de eliminar un elemento
    function reorganizarNumeracion() {
        var spans = canalesMarketing.querySelectorAll('span');
        contador = 1; // Reiniciar el contador
        spans.forEach(function(span, index) {
            span.textContent = (index + 1) + ". " + span.textContent.trim().split('.').slice(1).join('.'); // Eliminar la numeración anterior
        });
    }
});


// mostrar campaña
document.addEventListener('DOMContentLoaded', function() {
    var mostrarDetalleBtn = document.getElementById('mostrarDetalle');
    var detalleCampania = document.querySelector('.detalle-campania');

    mostrarDetalleBtn.addEventListener('click', function(event) {
        event.preventDefault();
        detalleCampania.classList.toggle('oculto');
    });
});

// modificar objetivo
 // Obtener el botón "Guardar"
 const guardarBtn = document.getElementById('guardar');
    
 // Agregar un event listener para guardar el texto en localStorage cuando se haga clic en el botón "Guardar"
 guardarBtn.addEventListener('click', function() {
     // Obtener el contenido del párrafo
     const texto = document.getElementById('texto').textContent;
     // Guardar el contenido del párrafo en el localStorage
     localStorage.setItem('textoGuardado', texto);
     // Cerrar el modal
     const modal = bootstrap.Modal.getInstance(document.getElementById('objetivo'));
     modal.hide();
 });

 // Obtener el elemento del párrafo
 const textoElemento = document.getElementById('texto');

 // Obtener el texto del localStorage si existe
 const textoGuardado = localStorage.getItem('textoGuardado');

 // Si hay texto guardado en localStorage, establecerlo como texto del párrafo
 if (textoGuardado) {
     textoElemento.textContent = textoGuardado;
 }