document.addEventListener('DOMContentLoaded', function () {
    const backButton = document.querySelector('.back-button a');

    backButton.addEventListener('click', function (event) {
        event.preventDefault();
        window.history.back();
    });
});
