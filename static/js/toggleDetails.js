document.addEventListener('DOMContentLoaded', function() {
    // Select all buttons with the class 'view-details-btn'
    var viewDetailButtons = document.querySelectorAll('.view-details-btn');

    // Loop through each button and attach the event listener
    viewDetailButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Get the flight ID from the data attribute
            var flightId = button.getAttribute('data-flight-id');
            toggleDetails(flightId);
        });
    });
});

function toggleDetails(flightId) {
    var detailsRow = document.getElementById('details-' + flightId);
    if (detailsRow.style.display === 'none' || detailsRow.style.display === '') {
        detailsRow.style.display = 'table-row';
    } else {
        detailsRow.style.display = 'none';
    }
}
