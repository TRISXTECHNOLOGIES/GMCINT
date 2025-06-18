document.addEventListener('DOMContentLoaded', function () {
    const menuItems = document.querySelectorAll('.sidebar nav ul li a');

    menuItems.forEach(item => {
        item.addEventListener('click', function () {
            menuItems.forEach(i => i.parentElement.classList.remove('active'));
            this.parentElement.classList.add('active');
        });
    });
});
