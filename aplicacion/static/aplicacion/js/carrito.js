  // JavaScript para controlar la apertura y cierre del carrito
  document.getElementById('cart-toggle').addEventListener('click', function() {
    this.classList.toggle('active');  // Toggle class 'active' en el botón
    var cart = document.querySelector('.cart');
    if (cart.style.right === '0px') {
      cart.style.right = '-350px';  // Cierra el carrito si está abierto
    } else {
      cart.style.right = '0px';  // Abre el carrito si está cerrado
    }
  });
  
  // JavaScript para cerrar el carrito
  function cerrarCarrito() {
    var cart = document.querySelector('.cart');
    cart.style.right = '-350px';  // Ajusta la posición inicial del carrito fuera de la pantalla
    document.getElementById('cart-toggle').classList.remove('active');  // Remueve la clase 'active' del botón
  }
  