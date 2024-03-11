
document.addEventListener('DOMContentLoaded', function() {
// Obtén una referencia al enlace por su id
var iconNavbarSidenav = document.getElementById('iconNavbarSidenav');

// Obtén una referencia al elemento del sidebar por su id
var sidenavMain = document.getElementById('sidenav-main');

// Agrega un evento de clic al enlace
iconNavbarSidenav.addEventListener('click', function() {
    // Verifica si el sidebar está visible o no
    var isSidenavVisible = sidenavMain.classList.contains('show');

    // Abre o cierra el sidebar según su estado actual
    if (isSidenavVisible) {
    sidenavMain.classList.remove('show');
    } else {
    sidenavMain.classList.add('show');
    }
});
});


