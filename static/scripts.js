document.addEventListener('DOMContentLoaded', (event) => {
    fetchAdminData();
});

function fetchAdminData() {
    fetch('http://10.162.39.206:5000/admin')  // Cambiar la dirección IP a la compartida
        .then(response => response.json())
        .then(data => {
            const adminDataDiv = document.getElementById('admin-data');
            adminDataDiv.innerHTML = `
                <p><strong>ID:</strong> ${data.id}</p>
                <p><strong>Name:</strong> ${data.name}</p>
                <p><strong>Email:</strong> ${data.email}</p>
            `;
        })
        .catch(error => console.error('Error fetching admin data:', error));
}

function fetchProducts(vendorType) {
    fetch(`http://10.162.39.206:5000/products/${vendorType}`)  // Cambiar la dirección IP a la compartida
        .then(response => response.json())
        .then(data => {
            const productsDataDiv = document.getElementById('products-data');
            productsDataDiv.innerHTML = data.map(product => `
                <div class="product-item">
                    <p><strong>ID:</strong> ${product.id}</p>
                    <p><strong>Name:</strong> ${product.name}</p>
                    <p><strong>Category:</strong> ${product.category}</p>
                    <p><strong>Type:</strong> ${product.type}</p>
                </div>
            `).join('');
        })
        .catch(error => console.error('Error fetching products:', error));
}
