
document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');

    let cart = [];
    let total = 0;

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {

            var product = button.getAttribute('data-product-id');
            product = JSON.parse(product.replace(/'/g, '"'));
            console.log("from add to cart"+product);
            console.log(typeof product); // To check the type of the variable
            console.log(Object.keys(product));
            console.log(product.cost)
            console.log(product['cost'])
            if (product) {
                cart.push(product);
                total += product.cost;
                updateCart();
            }
        });
    });

    function updateCart() {
        cartItems.innerHTML = '';

        cart.forEach(item => {
            console.log("from updateCart : "+item)
            var product = JSON.stringify(item);
            console.log(product.cost);
            const listItem = document.createElement('li');
            listItem.innerText = `${item.name} - ${item.cost}`;
            cartItems.appendChild(listItem);
        });

        cartTotal.textContent = total.toFixed(2);
    }
});
