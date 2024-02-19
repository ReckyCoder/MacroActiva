document.addEventListener('DOMContentLoaded', function() {
    const mainMenu = document.querySelector('.main-menu');

    // Añadir evento cuando el mouse entra al sidebar
    mainMenu.addEventListener('mouseenter', function() {
        expandSidebar();
    });

    // Añadir evento cuando el mouse sale del sidebar
    mainMenu.addEventListener('mouseleave', function() {
        collapseSidebar();
    });

    // Función para expandir el sidebar
    function expandSidebar() {
        mainMenu.classList.add('expanded');
        // Ajustar el margen izquierdo del contenido cuando el sidebar se expande
        document.querySelector('.content').style.marginLeft = '250px'; // Ancho del sidebar expandido
    }

    // Función para contraer el sidebar
    function collapseSidebar() {
        mainMenu.classList.remove('expanded');
        // Ajustar el margen izquierdo del contenido cuando el sidebar se contrae
        document.querySelector('.content').style.marginLeft = '60px'; // Ancho del sidebar contraído
    }
})