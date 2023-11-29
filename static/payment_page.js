// Getting cart details from local storage and setting up payload.

let cartDetails = localStorage.getItem('cart');
let payload = {
  "customer_id": "655a4e300d5cfaf04a8daca5",
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
        const cardNumber = document.getElementById('card-number').value;
    // if (!isValidCardNumber(cardNumber)) {
    //     // alert('Invalid card number');
    //     return;
    // }
    //
    // // Validate card holder
    // const cardHolder = document.getElementById('card-holder').value;
    // if (!isValidCardHolder(cardHolder)) {
    //     // alert('Invalid card holder name');
    //     return;
    // }
    //
    // // Validate expiry date
    // const expiryDate = document.getElementById('expiry').value;
    // if (!isValidExpiryDate(expiryDate)) {
    //     // alert('Invalid expiry date');
    //     return;
    // }
    //
    // // Validate CVV
    // const cvv = document.getElementById('cvv').value;
    // if (!isValidCVV(cvv)) {
    //     // alert('Invalid CVV');
    //     return;
    // }
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

// // Validation functions
// function isValidCardNumber(cardNumber) {
//     // Check if the card number is a 16-digit numeric value
//     const cardNumberRegex = /^\d{16}$/;
//     return cardNumberRegex.test(cardNumber);
// }
//
// function isValidCardHolder(cardHolder) {
//     // Check if the card holder name contains only letters and spaces
//     const cardHolderRegex = /^[A-Za-z\s]+$/;
//     return cardHolderRegex.test(cardHolder);
// }
//
// function isValidExpiryDate(expiryDate) {
//     // Check if the expiry date is in MM/YY format
//     const expiryDateRegex = /^(0[1-9]|1[0-2])\/\d{2}$/;
//     return expiryDateRegex.test(expiryDate);
// }
//
// function isValidCVV(cvv) {
//     // Check if the CVV is a 3-digit numeric value
//     const cvvRegex = /^\d{3}$/;
//     return cvvRegex.test(cvv);
// }


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
