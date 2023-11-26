// Initialize cart only once when the page loads
let cart = JSON.parse(localStorage.getItem('cart')) || [];

function getATCButtons() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    let totalCost = 0;
    document.getElementById('cart-count').innerText = cart.length;

    addToCartButtons.forEach(button => {
        // Check if the event listener has been attached before attaching it
        if (!button.hasEventListener) {
            button.hasEventListener = true; // Mark the button to avoid attaching multiple event listeners
            button.addEventListener('click', function(e) {
                var product = button.getAttribute('data-product-id');
                product = JSON.parse(product.replace(/'/g, '"'));
                if (product) {
                    cart.push(product);
                    totalCost += product.cost;
                    document.getElementById('cart-count').innerText = cart.length;
                }
            });
        }
    });

    return cart;
}

function getProductsByCategory(category) {
    return products.filter(product => product.category === category);
}

function loadProducts(category) {
    const productListElement = document.getElementById('product-type');
    productListElement.innerHTML = '';

    const filteredProducts = getProductsByCategory(category);

    filteredProducts.forEach(product => {
        const productElement = document.createElement('div');
        productElement.className = 'product';
        productElement.innerHTML = `
            <img src="${product.image_url}" alt="${product.name}" class="product-image">
            <p>Name: ${product.name}</p>
            <p>${product.color}</p>
            <p>Price: $${product.cost}</p>
            <p>ID: ${product.product_id}</p>
            <button class="add-to-cart" data-product-id='${JSON.stringify(product)}' id="add-cart">
                Add to Cart
            </button>
        `;
        productListElement.appendChild(productElement);
    });

    // Reattach event listeners for the "Add to Cart" buttons
    getATCButtons();

    return filteredProducts; // Return the filtered products
}

document.addEventListener('DOMContentLoaded', function() {
    var products = JSON.parse(JSON.stringify(productsData)); // Copy the data to a new array

    const coffeeTableLink = document.getElementById('coffee-table-link');
    const diningChairLink = document.getElementById('dining_chair-link');
    const diningSetLink = document.getElementById('dining_set_link');
    const officeChairLink = document.getElementById('office-chair-link');
    const reclinerLink = document.getElementById('recliners-link');
    const shoeCabinetLink = document.getElementById('shoe-cabinet-link');
    const sofaLink = document.getElementById('sofa-link');


    // Initial loading of products and attaching event listeners
    const initialFilteredProducts = loadProducts('coffee_table');
    getATCButtons(); // Attach event listeners

    coffeeTableLink.addEventListener('click', function(event) {
        event.preventDefault();
        const filteredProducts = loadProducts('coffee_table');
        console.log("Load cart", cart);
    });

    diningChairLink.addEventListener('click', function(event) {
        event.preventDefault();
        const filteredProducts = loadProducts('dining_chair');
        console.log("Load cart", cart);
    });

    diningSetLink.addEventListener('click', function(event) {
        event.preventDefault();
        const filteredProducts = loadProducts('dining_set');
        console.log("Load cart", cart);
    });

    officeChairLink.addEventListener('click', function(event) {
        event.preventDefault();
        const filteredProducts = loadProducts('office_chair');
        console.log("Load cart", cart);
    });

    reclinerLink.addEventListener('click', function(event) {
        event.preventDefault();
        const filteredProducts = loadProducts('reclyner');
        console.log("Load cart", cart);
    });

    shoeCabinetLink.addEventListener('click', function(event) {
        event.preventDefault();
        const filteredProducts = loadProducts('shoe_cabinet');
        console.log("Load cart", cart);
    });

    sofaLink.addEventListener('click', function(event) {
        event.preventDefault();
        const filteredProducts = loadProducts('sofa');
        console.log("Load cart", cart);
    });

    // Go To Cart
    document.getElementById('go-to-cart-button').addEventListener('click', function() {
        let cartString = JSON.stringify(cart);
        localStorage.setItem('cart', cartString);
        window.location.href = `cart_page`;
    });
});