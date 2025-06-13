let cart = [];
let wishlist = [];
let products = [];

document.addEventListener('DOMContentLoaded', function () {
    fetch('http://localhost:3000/products')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch products');
            return response.json();
        })
        .then(data => {
            products = data;
            displayProducts(products);
        })
        .catch(error => {
            console.error("Error loading products:", error);
            document.getElementById("productList").innerHTML = "<p>Failed to load products.</p>";
        });

    document.getElementById('addtocart').addEventListener('click', showCartPopup);
    document.getElementById('addtofav').addEventListener('click', showWishlistPopup);
});

function displayProducts(products) {
    const productList = document.getElementById("productList");
    productList.innerHTML = "";
    products.forEach((product) => {
        const productDiv = document.createElement("div");
        productDiv.className = "product";
        productDiv.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>$${product.price}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
            <button onclick="addToWishlist(${product.id})">❤️ Add to Wishlist</button>
        `;
        productList.appendChild(productDiv);
    });
}

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        cart.push(product);
        alert(`${product.name} added to the cart!`);
    }
}


function addToWishlist(productId) {
    const product = products.find(p => p.id === productId);
    if (product && !wishlist.includes(product)) {
        wishlist.push(product);
        alert(`${product.name} added to your Wishlist!`);
    }
}

// Show Cart Popup
function showCartPopup() {
    let total = 0;
    let cartHtml = `
        <div id="cartPopup">
            <h2>Your Cart</h2>
            <input type="text" id="custName" placeholder="Enter your name" required><br>
            <input type="tel" id="custMobile" placeholder="Enter mobile number" required><br>
            <ul>
    `;
    cart.forEach(item => {
        total += item.price;
        cartHtml += `<li>${item.name} - $${item.price}</li>`;
    });

    cartHtml += `
            </ul>
            <p><strong>Total: $${total.toFixed(2)}</strong></p>
            <button onclick="downloadInvoice()">Download Invoice</button>
            <button onclick="clearCart()">Clear Cart</button>
            <button onclick="closePopup()">Close</button>
        </div>
    `;

    const popupContainer = document.createElement("div");
    popupContainer.innerHTML = cartHtml;
    document.body.appendChild(popupContainer);
}

function clearCart() {
    cart = [];
    closePopup();
    alert("Cart has been cleared!");
}

// Show Wishlist Popup
function showWishlistPopup() {
    if (wishlist.length === 0) {
        alert("Your wishlist is empty!");
        return;
    }

    let wishHtml = `
        <div id="cartPopup">
            <h2>Your Wishlist</h2>
            <ul>
    `;
    wishlist.forEach(item => {
        wishHtml += `<li>${item.name} - $${item.price}</li>`;
    });

    wishHtml += `
            </ul>
            <button onclick="clearWishlist()">Clear Wishlist</button>
            <button onclick="closePopup()">Close</button>
        </div>
    `;

    const popup = document.createElement("div");
    popup.innerHTML = wishHtml;
    document.body.appendChild(popup);
}

function clearWishlist() {
    wishlist = [];
    closePopup();
    alert("Wishlist has been cleared!");
}

// Close any popup
function closePopup() {
    const popup = document.getElementById("cartPopup");
    if (popup) popup.remove();
}

// Download Invoice (Simulated as .txt)
function downloadInvoice() {
    const name = document.getElementById("custName").value;
    const mobile = document.getElementById("custMobile").value;

    if (!name || !mobile) {
        alert("Please enter your name and mobile number.");
        return;
    }

    let invoice = `Customer: ${name}\nMobile: ${mobile}\n\nItems:\n`;
    let total = 0;
    cart.forEach(item => {
        invoice += `${item.name} - $${item.price}\n`;
        total += item.price;
    });
    invoice += `\nTotal: $${total.toFixed(2)}`;

    const blob = new Blob([invoice], { type: "application/pdf" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "invoice.txt"; // You can change this to .pdf if using PDF generation lib
    link.click();
}
