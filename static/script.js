
document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let totalCost = 0;
    document.getElementById('cart-count').innerText = cart.length;
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
                totalCost += product.cost;
                document.getElementById('cart-count').innerText = cart.length;

                // updateCart();
            }
        });
    });

    // function updateCart() {
    //     cartItems.innerHTML = '';
    //
    //     cart.forEach(item => {
    //         console.log("from updateCart : "+item)
    //         var product = JSON.stringify(item);
    //         console.log(product.cost);
    //         const listItem = document.createElement('li');
    //         listItem.innerText = `${item.name} - ${item.cost}`;
    //         cartItems.appendChild(listItem);
    //     });
    //     cartTotal.textContent = totalCost.toFixed(2);
    // }

    document.getElementById('go-to-cart-button').addEventListener('click', function() {
            // Redirect to the cart_page.html
            let cartString = JSON.stringify(cart);
            localStorage.setItem('cart', cartString);
            window.location.href = `cart_page`;
        });
});
