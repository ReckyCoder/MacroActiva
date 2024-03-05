const tbody = document.querySelector('.items');

const agregar = document.querySelector('#Agregar');
const eliminar = document.querySelector('#Eliminar');

const ingreso = document.querySelectorAll('.descripcion');

const totalSinImpuesto = document.querySelector('.total-sin-impuesto');
const totalImpuesto = document.querySelector('.total-impuesto');
const totalOrden = document.querySelector('#totalOrden');

document.addEventListener('DOMContentLoaded', () => {
  
  botonesDeAccion();

  agregar.addEventListener('click', e => {

    if (tbody.children.length > 0){
      ReplicarFila();
    } else {
      CrearFila(); 
    }
  });

  eliminar.addEventListener('click', e => {
    eliminarFila();
  });

  inputDetectar();

  totales();
});

function ReplicarFila(){
  const tr = document.createElement('tr');

  const td = tbody.children[0].children;

  for (let i = 0; i < td.length; i++){

      const cloneTd = td[i].cloneNode(true);

      const clonedInputs = cloneTd.querySelectorAll('input');
      clonedInputs.forEach(input => {
        input.value = '';  // Establecer el valor como una cadena vacía
      });

      const clonedSpan = cloneTd.querySelectorAll('.total');
      clonedSpan.forEach(span => {
        span.textContent = '';  // Establecer el valor como una cadena vacía
      });

      tr.appendChild(cloneTd);   

  };

  tbody.appendChild(tr);

  // Vuelve a inicializar los tooltips después de clonar
  const tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  tooltips.forEach(tooltip => {
    // Hacer una excepción para el elemento de clic
    if (tooltip !== agregar && tooltip !== eliminar) {
      new bootstrap.Tooltip(tooltip);
    }
  });
}

function eliminarFila(){
  const fila = tbody.children;
  if(fila.length > 0){
    const ultimaFila = fila[fila.length - 1];

    tbody.removeChild(ultimaFila);

    const tr = tbody.querySelectorAll('tr');

    totales(tr)
  } 
}

function CrearFila(){
// Crear el table row del tbody
      const tr = document.createElement('tr');


      // Crear los table data del tr
      const td1 = document.createElement('td');
      td1.classList.add('ps-1');

      const td2 = document.createElement('td');
      td2.classList.add('ps-1');

      const td3 = document.createElement('td');
      td3.classList.add('ps-1');

      const td4 = document.createElement('td');
      td4.classList.add('ps-1');

      const td5 = document.createElement('td');
      td5.classList.add('ps-1', 'text-center');

      const td6 = document.createElement('td');
      td6.classList.add('ps-1', 'text-center');

      const td7 = document.createElement('td');
      td7.classList.add('ps-1', 'text-center');
      // ---------------------------------------

      // Crear los inputs de los table data 1, 2, 3 y 4

      const input1 = document.createElement('input');
      input1.classList.add('form-control');
      input1.setAttribute('type', 'text');
      input1.setAttribute('placeholder', '123 ...');

      const input2 = document.createElement('input');
      input2.classList.add('form-control');
      input2.setAttribute('type', 'text');
      input2.setAttribute('placeholder', 'Item ...');

      const input3 = document.createElement('input');
      input3.classList.add('form-control', 'cantidad');
      input3.setAttribute('type', 'text');
      input3.setAttribute('placeholder', '2 ...');

      const input4 = document.createElement('input');
      input4.classList.add('form-control', 'neto');
      input4.setAttribute('type', 'text');
      input4.setAttribute('placeholder', '00.000.000');

      // ------------------------------------------

      // Crear los span de los table data 5 y 6

      const span1 = document.createElement('span');
      span1.classList.add('text-sm', 'font-weight-normal');
      span1.textContent = '0.19';

      const span2 = document.createElement('span');
      span2.classList.add('text-sm', 'font-weight-normal', 'total');

      // -------------------------------------------

      // Creacion del icono tooltip 

      const button = document.createElement('button');
      button.classList.add('eliminar', 'btn', 'm-0');
      button.setAttribute('type', 'button');
      button.setAttribute('data-bs-toggle', 'tooltip');
      button.setAttribute('data-bs-title', 'Eliminar Item');

      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.setAttribute('width', '24');
      svg.setAttribute('height', '24');
      svg.setAttribute('viewBox', '0 0 448 512');

      const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
      path.setAttribute('fill', '#1e293b');
      path.setAttribute('d', 'M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z');

      // -------------------------------------------

      td1.appendChild(input1);
      td2.appendChild(input2);
      td3.appendChild(input3);
      td4.appendChild(input4);
      td5.appendChild(span1);
      td6.appendChild(span2);

      svg.appendChild(path);
      button.appendChild(svg);
      td7.appendChild(button);

      tr.appendChild(td1);
      tr.appendChild(td2);
      tr.appendChild(td3);
      tr.appendChild(td4);
      tr.appendChild(td5);
      tr.appendChild(td6);
      tr.appendChild(td7);

      tbody.appendChild(tr);
    
}

function botonesDeAccion(){
  tbody.addEventListener('click', e => {
    const botonEliminar = e.target.closest('.eliminar');
 
    if (botonEliminar) {
      const filaEliminar = botonEliminar.parentNode.parentNode;

      if (filaEliminar && tbody.contains(filaEliminar)) {
        
        // Eliminar tooltips antes de quitar la fila del DOM
        const tooltips = filaEliminar.querySelectorAll('[data-bs-toggle="tooltip"]');
        tooltips.forEach(tooltip => {
          const tooltipInstance = bootstrap.Tooltip.getInstance(tooltip);
          if (tooltipInstance) {
            tooltipInstance.dispose(); // Destruir el tooltip
          }
        });

        tbody.removeChild(filaEliminar);

        const tr = tbody.querySelectorAll('tr');

        totales(tr)
      }
    }
  });

};

function inputDetectar(){
  
  tbody.addEventListener('change', e => {
    const tr = e.target.closest('tr');


    if(tr){
      const neto = tr.querySelector('.neto');
      const cantidad = tr.querySelector('.cantidad');
      const total = tr.querySelector('.total');

      const numeros = neto.value;
      const formato = numeros.replace(/\./g, '');
      const parsear = parseInt(formato);

      if(cantidad.value !== '' && neto.value !== ''){

        // Verificar si la conversión fue exitosa y realizar acciones adicionales si es necesario
          if (!isNaN(parsear)) {
            const division = parsear / 100;
            const comision = Math.round(division * 19);

            const resultado = Math.round((parseInt(cantidad.value) * parsear) + parseInt(cantidad.value) * comision);

            // Formatear el resultado en formato de pesos
            const formatoPesos = new Intl.NumberFormat('es-ES').format(resultado);
            total.textContent = formatoPesos;
          } else {
            total.textContent = '';
          }
        
      }
    

    }
  });
  
};

function totales(tr){

  if(tr){
    const listaSinImpuesto = [];
    const listaImpuesto = [];

    tr.forEach(e => {
      const netos = e.querySelector('.neto');
      const cantidad = e.querySelector('.cantidad');

      const numeros = netos.value;
      const formato = numeros.replace(/\./g, '');
      const parsear = parseInt(formato);

      const division = parsear / 100;
      const comision = Math.round(division * 19);

      const resultado = parseInt(cantidad.value) * parsear;
      const impuesto = parseInt(cantidad.value) * comision;

      if(!isNaN(resultado)){
        listaSinImpuesto.push(parseInt(resultado)); 
      } 

      if(!isNaN(impuesto)){
        listaImpuesto.push(parseInt(impuesto));
      }
      
    });

    let neto = 0;
    listaSinImpuesto.map(e => neto += e);

    let impuesto = 0;
    listaImpuesto.map(e => impuesto += e);

    const formatoPesos = new Intl.NumberFormat('es-ES').format(neto);
    const formatoPesos2 = new Intl.NumberFormat('es-ES').format(impuesto);

    if(neto !== 0){
      totalSinImpuesto.textContent = formatoPesos;
    } else {
      totalSinImpuesto.textContent = '00.000.000';
    }

    if(impuesto !== 0){
      totalImpuesto.textContent = formatoPesos2;
    } else {
      totalImpuesto.textContent = '00.000.000';
    }

    if(neto !== 0 && impuesto !== 0){
      let sum = neto + impuesto;
      const formatoPesos = new Intl.NumberFormat('es-ES').format(sum);
      totalOrden.textContent = formatoPesos;
    } else {
      totalOrden.textContent = "00.000.000";
    }
  }

  tbody.addEventListener('change', () => {
    const tr = tbody.querySelectorAll('tr');

    const listaSinImpuesto = [];
    const listaImpuesto = [];

    tr.forEach(e => {
      const netos = e.querySelector('.neto');
      const cantidad = e.querySelector('.cantidad');

      const numeros = netos.value;
      const formato = numeros.replace(/\./g, '');
      const parsear = parseInt(formato);

      const division = parsear / 100;
      const comision = Math.round(division * 19);

      const resultado = parseInt(cantidad.value) * parsear;
      const impuesto = parseInt(cantidad.value) * comision;

      if(!isNaN(resultado)){
        listaSinImpuesto.push(parseInt(resultado)); 
      } 

      if(!isNaN(impuesto)){
        listaImpuesto.push(parseInt(impuesto));
      }
      
    });

    let neto = 0;
    listaSinImpuesto.map(e => neto += e);

    let impuesto = 0;
    listaImpuesto.map(e => impuesto += e);

    const formatoPesos = new Intl.NumberFormat('es-ES').format(neto);
    const formatoPesos2 = new Intl.NumberFormat('es-ES').format(impuesto);

    if(neto !== 0){
      totalSinImpuesto.textContent = formatoPesos;
    } else {
      totalSinImpuesto.textContent = '00.000.000';
    }

    if(impuesto !== 0){
      totalImpuesto.textContent = formatoPesos2;
    } else {
      totalImpuesto.textContent = '00.000.000';
    }

    if(neto !== 0 && impuesto !== 0){
      let sum = neto + impuesto;
      const formatoPesos = new Intl.NumberFormat('es-ES').format(sum);
      totalOrden.textContent = formatoPesos;
    } else {
      totalOrden.textContent = "00.000.000";
    }
  })
}