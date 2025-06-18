
        document.getElementById('adminForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Get the input values
    const adminName = document.getElementById('adminName').value;
    const adminEmail = document.getElementById('adminEmail').value;
    const adminRole = document.getElementById('adminRole').value;

    // Add the new admin to the table
    addAdminToTable(adminName, adminEmail, adminRole);

    // Clear the form
    document.getElementById('adminForm').reset();
});

function addAdminToTable(name, email, role) {
    const tableBody = document.querySelector('#adminTable tbody');
    const newRow = document.createElement('tr');

    newRow.innerHTML = `
        <td>${name}</td>
        <td>${email}</td>
        <td>${role}</td>
    `;

    tableBody.appendChild(newRow);
}

