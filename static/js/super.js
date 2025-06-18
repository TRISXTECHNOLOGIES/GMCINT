document.addEventListener('DOMContentLoaded', function () {
    const resetButton = document.querySelector('.reset-filter');
    const filterSelects = document.querySelectorAll('.filter-group select');

    resetButton.addEventListener('click', function () {
        filterSelects.forEach(select => {
            select.selectedIndex = 0;
        });
    });

    const menuToggle = document.querySelector('.menu-toggle img');
    const sidebar = document.querySelector('.sidebar');

    menuToggle.addEventListener('click', function () {
        sidebar.classList.toggle('open');
    });
});
