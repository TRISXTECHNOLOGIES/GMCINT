// Handle the click event for status boxes
const statusBoxes = document.querySelectorAll('.status-box');
statusBoxes.forEach(box => {
    box.addEventListener('click', function() {
        const status = this.getAttribute('data-status');
        filterTableByStatus(status);
    });
});

function filterTableByStatus(status) {
    const tableRows = document.querySelectorAll('#contact-table-body tr');
    tableRows.forEach(row => {
        const rowStatus = row.querySelector('td:last-child').textContent;
        if (rowStatus === status || (status === 'Open' && rowStatus === 'Contacted')) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// Initialize flatpickr on the date input field
flatpickr("#filter-date", {
    dateFormat: "d M Y",
});

// Apply the selected filters
document.getElementById('reset-filter-button').addEventListener('click', function() {
    document.getElementById('filter-date').value = "Date";
    document.getElementById('filter-type').value = "Contact Type";
    document.getElementById('filter-status').value = "Contact Status";
    filterTableByStatus('Open');
});

// Pagination controls (for demonstration, actual implementation will need more work)
document.querySelector('.prev-page').addEventListener('click', function() {
    alert('Previous page clicked');
});

document.querySelector('.next-page').addEventListener('click', function() {
    alert('Next page clicked');
});
