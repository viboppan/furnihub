     function deleteProduct(name){
        // cartProducts = cartProducts.filter(item => item.name !== name);
        console.log(name);
    }

function getQueryParam(variable) {
      const query = window.location.search.substring(1);
      const vars = query.split("&");
      for (let i = 0; i < vars.length; i++) {
        const pair = vars[i].split("=");
        if (pair[0] === variable) {
          return decodeURIComponent(pair[1]);
        }
      }
      return null;
    }

    // Get the data from the URL and parse it as JSON
    const receivedData = JSON.parse(getQueryParam('cd'));
    let cartProducts = JSON.parse(JSON.stringify(receivedData));

    // Use the received data
    console.log("Data received in receiver.html:", cartProducts);
    document.getElementById('total-items').innerText = cartProducts.length;

    const productData = document.getElementById("cart-products");
    let totalCartPrice = 0;
    for (let i = 0; i<cartProducts.length; i++) {
        totalCartPrice = totalCartPrice+Number(cartProducts[i].cost);
         const div = document.createElement('div');
            div.innerHTML = "<div class='d-flex flex-row justify-content-between align-items-center pt-lg-4 pt-2 pb-3 border-bottom mobile'>\n" +
            "                <div class='d-flex flex-row align-items-center'>\n" +
            "                    <div><img id='image' width='150' height='150' alt = '' src="+cartProducts[i].image_url+" /></div>\n" +
            "                    <div class='d-flex flex-column pl-md-3 pl-1'>\n" +
            "                        <div><h6>"+cartProducts[i].name+"</h6></div>\n" +
            "                        <div >Brand: <span class='pl-2'>"+cartProducts[i].brand+"</span></div>\n" +
            "                        <div>Color:<span class='pl-3'>"+cartProducts[i].color+"</span></div>\n" +
            "                    </div>\n" +
            "                </div>\n" +
            "                <div class='pl-md-0 pl-1'><b>"+cartProducts[i].cost+"</b></div>\n" +
            "                <div class='pl-md-0 pl-2'>\n" +
            "                    <span class='fa fa-minus-square text-secondary'></span><span class='px-md-3 px-1'>1</span><span class='fa fa-plus-square text-secondary'></span>\n" +
            "                </div>\n" +
            "                <div class='pl-md-0 pl-1'><b>"+cartProducts[i].cost+"</b></div>\n" +
            "                <div class='close' id = 'close-product' onclick='deleteProduct(\"" + cartProducts[i].name + "\")'>&times;</div>\n" +
            "            </div>"
        productData.appendChild(div);
    }
    document.getElementById('total-cart').innerText = "$"+totalCartPrice+"";
    document.getElementById('close-product').addEventListener('click',deleteProduct);


    document.getElementById('payment-button').addEventListener('click', function() {
            window.location.href = `payment_page`;
        });