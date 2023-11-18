// Getting cart details from local storage and setting up payload.

let cartDetails = localStorage.getItem('cart');
let payload = {
  "customer_id": "653f4f2bc4568a5bbc0d0ceb",
  "products": [],
  "total_cost": 0
};

if (cartDetails && cartDetails !== 'undefined') {
  cartDetails = JSON.parse(cartDetails);

  payload.products  = cartDetails.map(product => {
    let info = {};
    info.product_id = product.product_id;
    info.quantity = 1;
    return info;
  });

  payload.total_cost = cartDetails.reduce((sum, product) => sum + product.cost, 0);

  console.log(payload);

} else {
  console.error("Cart details not found or invalid.");
}

document.getElementById("total-cost").innerText = parseFloat(payload.total_cost.toFixed(2));

// Click event on payment button.

var payButton = document.getElementById('payment-button');

// Attach the onclick event handler function to the button
payButton.onclick = proceedPayment;

    function proceedPayment() {
          const url = 'http://localhost:5000/add_order';
          postData(url, payload)
            .then(responseData => {
              console.log('Success:', responseData);
              window.location.href = `order_summary`;
            })
            .catch(error => {
              console.error('Error:', error);
            });
    }

// Post call to db -- These calls should be moved to service.js
function postData(url = '', data = {}) {
  // Default options are marked with *
  return fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Content-Type': 'application/json',
      // Add any other headers if needed
    },
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  })
    .then(response => response.json()); // parses JSON response into native JavaScript objects
}
