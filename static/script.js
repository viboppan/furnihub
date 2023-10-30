
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

    document.getElementById('go-to-cart-button').addEventListener('click', function() {
            // Redirect to the cart_page.html
            window.location.href = "cart_page";
        });
});

document.addEventListener('DOMContentLoaded', function() {
    // Retrieve cart data from local storage (assuming you're using local storage)
    const cartData = JSON.parse(localStorage.getItem('cart'));

    const cartItems = document.getElementById('cart-items');

    if (cartData && cartData.length > 0) {
        cartData.forEach(item => {
            const cartItemDiv = document.createElement('div');
            cartItemDiv.classList.add('d-flex', 'flex-row', 'justify-content-between', 'align-items-center', 'pt-4', 'pb-3', 'mobile');

            // Create elements for product details
            const productImage = document.createElement('img');
            productImage.src = item.image_url;
            productImage.width = 150;
            productImage.height = 150;
            productImage.alt = 'Product Image';

            const productDetailsDiv = document.createElement('div');
            const productName = document.createElement('h6');
            productName.innerText = item.name;

            // Add other product details as needed (Art.No, Color, Size)

            const productPrice = document.createElement('b');
            productPrice.innerText = `$${item.cost.toFixed(2)}`;

            // Create an element for the quantity controls (e.g., plus/minus buttons)

            // Add a close button for removing items

            // Append all elements to cartItemDiv

            cartItemDiv.appendChild(productImage);
            cartItemDiv.appendChild(productDetailsDiv);
            cartItemDiv.appendChild(productPrice);
            // Append other elements to cartItemDiv

            cartItems.appendChild(cartItemDiv);
        });
    }
});
