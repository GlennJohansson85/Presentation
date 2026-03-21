// NAVBAR-SCROLL.JS
document.addEventListener("DOMContentLoaded", function () {

    const navbar   = document.querySelector(".navbar");
    const collapse = document.getElementById("navbarSupportedContent");

    if (!navbar || !collapse) return;

    /* Scroll: mörk navbar när man scrollar */
    function updateScrolled() {
        if (window.scrollY > 0) {
            navbar.classList.add("scrolled");
            return;
        }
        if (!navbar.classList.contains("navbar--open")) {
            navbar.classList.remove("scrolled");
        }
    }

    window.addEventListener("scroll", updateScrolled);
    updateScrolled();

    /* Toggler öppnas */
    collapse.addEventListener("show.bs.collapse", function () {
        navbar.classList.add("navbar--open");
        navbar.classList.add("scrolled");
    });

    /* Toggler stängs */
    collapse.addEventListener("hidden.bs.collapse", function () {
        navbar.classList.remove("navbar--open");
        updateScrolled();
    });

    /* Resize: om vi går till desktop, resetta "open"-state */
    function handleResize() {
        if (window.innerWidth > 992) {
            navbar.classList.remove("navbar--open");
            updateScrolled();
        }
    }

    window.addEventListener("resize", handleResize);
    handleResize();

});
