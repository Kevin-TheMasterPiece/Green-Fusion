const verdurasSelect = document.getElementById('verduras');
const frutasSelect = document.getElementById('frutas');
const tamanoSelect = document.getElementById('tamano');
const listaIngredientes = document.getElementById('lista-ingredientes');
const contenedorIngredientes = document.getElementById('contenedor-ingredientes-seleccionados');
const finalizarPedidoBtn = document.getElementById('finalizar-pedido');
const precioSpan = document.getElementById('precio');

verdurasSelect.addEventListener('change', agregarIngrediente);
frutasSelect.addEventListener('change', agregarIngrediente);
tamanoSelect.addEventListener('change', actualizarPrecio);
finalizarPedidoBtn.addEventListener('click', finalizarPedido);

function agregarIngrediente() {
  const ingredienteSeleccionado = this.value;
  if (ingredienteSeleccionado !== '') {
    const nuevoIngrediente = document.createElement('li');
    nuevoIngrediente.textContent = ingredienteSeleccionado;
    listaIngredientes.appendChild(nuevoIngrediente);

    this.selectedIndex = 0;
  }
}
