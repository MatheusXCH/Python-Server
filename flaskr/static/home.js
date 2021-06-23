const sio = io();

sio.on('connect', () => {
    console.log("Connected to the server")
});

sio.on("disconnect", () => {
    console.log("Disconnect from the server")
});

sio.on("create_product", (data, cb) => {
    console.log(data);

    var product_id = Math.floor(Math.random() * 100);
    var product_name = prompt("Product Name: ");
    var product_brand = prompt("Product Brand: ");
    var product_price = prompt("Product Price: ");
    var product_stock = prompt("Product Stock: ");

    const result = {id: product_id, name: product_name, brand: product_brand, price: product_price, stock: product_stock};
    cb(result);
});

sio.on("client_count", (count) => {
    console.log("Current connected clients: " + count);
});

sio.on("get_product", (data, cb) => {
    console.log(data);
    const request_success = {"success": true}
    cb(request_success)
})