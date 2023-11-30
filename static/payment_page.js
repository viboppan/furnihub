let cartDetails = localStorage.getItem('cart');
let cData = JSON.parse(localStorage.getItem('cData'));
let payload = {
    "customer_id": "",
    "products": [],
    "total_cost": 0
};
let cardPayload = {
    "payment_date": "",
    "payment_method": "",
    "amount": 0,
    "order_id":"",
};

if (cData && cData !== 'undefined') {
    payload.customer_id = cData.id;
}

if (cartDetails && cartDetails !== 'undefined') {
    cartDetails = JSON.parse(cartDetails);

    payload.products = cartDetails.map(product => {
        let info = {};
        info.product_id = product.product_id;
        info.quantity = 1;
        return info;
    });

   const cartCost = cartDetails.reduce((sum, product) => sum + product.cost, 0);
   payload.total_cost = cartCost;

    console.log(payload);

} else {
    console.error("Cart details not found or invalid.");
}

document.getElementById("total-cost").innerText = parseFloat(payload.total_cost.toFixed(2));


let payButton = document.getElementById('payment-button');

// Attach the onclick event handler function to the button
payButton.onclick = proceedPayment;

function proceedPayment(e) {
    e.preventDefault();
    const cardNumber = document.getElementById('card-number').value;
    if (!isValidCardNumber(cardNumber)) {
        return;
    }

    const cardHolder = document.getElementById('card-holder').value;
    if (!isValidCardHolder(cardHolder)) {
        return;
    }

    const expiryDate = document.getElementById('expiry').value;
    if (!isValidExpiryDate(expiryDate)) {
        return;
    }

    const cvv = document.getElementById('cvv').value;
    if (!isValidCVV(cvv)) {
        return;
    }
    const url = 'http://localhost:5000/add_order';
    postData(url, payload)
        .then(responseData => {
            console.log('Success:', responseData);
            if(responseData.order_id !=undefined) {
                // window.location.href = `order_summary`;
                const url1 = 'http://localhost:5000/add_payment';
                cardPayload.payment_date = new Date().toLocaleString();
                cardPayload.payment_method = "card";
                cardPayload.amount = cartDetails.reduce((sum, product) => sum + product.cost, 0);;
                cardPayload.order_id = responseData.order_id;

                console.log("CardPayload",cardPayload);
                postData(url1, cardPayload)
                    .then(responseData => {
                            console.log('Success:', responseData);
                            window.location.href = `order_summary`;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                    });
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });


}

// Validation functions
function isValidCardNumber(cardNumber) {
    const cardNumberRegex = /^\d{16}$/;
    return cardNumberRegex.test(cardNumber);
}

function isValidCardHolder(cardHolder) {
    const cardHolderRegex = /^[A-Za-z\s]+$/;
    return cardHolderRegex.test(cardHolder);
}

function isValidExpiryDate(expiryDate) {
    const expiryDateRegex = /^(0[1-9]|1[0-2])\/\d{2}$/;
    return expiryDateRegex.test(expiryDate);
}

function isValidCVV(cvv) {
    const cvvRegex = /^\d{3}$/;
    return cvvRegex.test(cvv);
}


function postData(url = '', data = {}) {
    // Default options are marked with *
    return fetch(url, {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data), // body data type must match "Content-Type" header
        })
        .then(response => response.json());
}