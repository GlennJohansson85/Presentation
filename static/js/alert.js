// alert.js
document.addEventListener("DOMContentLoaded", function() {
    const alerts = document.querySelectorAll('.custom-alert');

    // Ta bort efter 3 sekunder
    setTimeout(() => {
        alerts.forEach(alert => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500); // tar bort elementet helt
        });
    }, 3000);
});