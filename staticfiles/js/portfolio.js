document.addEventListener("DOMContentLoaded", function () {
    const lightbox = document.getElementById("imgLightbox");
    const lightboxStage = document.getElementById("imgLightboxStage");
    const lightboxImg = document.getElementById("lightboxImg");
    const lightboxVideo = document.getElementById("lightboxVideo");
    const closeBtn = document.getElementById("imgLightboxClose");

    if (!lightbox || !lightboxStage || !lightboxImg) {
        return;
    }

    let zoomLevel = 1;
    let activeType = "image";

    function resetStage() {
        zoomLevel = 1;
        lightbox.classList.remove("zoomed");
        lightboxStage.scrollLeft = 0;
        lightboxStage.scrollTop = 0;

        lightboxImg.style.width = "";
        lightboxImg.style.height = "";
        lightboxImg.style.maxWidth = "92vw";
        lightboxImg.style.maxHeight = "92vh";
    }

    function stopVideo() {
        if (!lightboxVideo) {
            return;
        }

        lightboxVideo.pause();
        lightboxVideo.currentTime = 0;
        lightboxVideo.removeAttribute("src");
        lightboxVideo.removeAttribute("poster");
        lightboxVideo.style.display = "none";
        lightboxVideo.load();
    }

    function applyZoom() {
        if (activeType !== "image") {
            return;
        }

        if (zoomLevel <= 1) {
            lightbox.classList.remove("zoomed");
            lightboxImg.style.width = "";
            lightboxImg.style.maxWidth = "92vw";
            lightboxImg.style.maxHeight = "92vh";
            lightboxStage.scrollLeft = 0;
            lightboxStage.scrollTop = 0;
            return;
        }

        lightbox.classList.add("zoomed");
        lightboxImg.style.maxWidth = "none";
        lightboxImg.style.maxHeight = "none";
        lightboxImg.style.width = lightboxImg.naturalWidth * zoomLevel + "px";
        lightboxImg.style.height = "auto";
    }

    function openImage(src, alt) {
        if (!src) {
            return;
        }

        activeType = "image";
        resetStage();
        stopVideo();

        lightboxImg.style.display = "block";
        lightboxImg.onload = function () {
            applyZoom();
        };
        lightboxImg.src = src;
        lightboxImg.alt = alt || "";

        lightbox.classList.add("open");
        lightbox.setAttribute("aria-hidden", "false");
    }

    function openVideo(src, poster, label) {
        if (!lightboxVideo || !src) {
            return;
        }

        activeType = "video";
        resetStage();

        lightboxImg.onload = null;
        lightboxImg.src = "";
        lightboxImg.alt = "";
        lightboxImg.style.display = "none";

        lightboxVideo.style.display = "block";
        lightboxVideo.src = src;

        if (poster) {
            lightboxVideo.poster = poster;
        } else {
            lightboxVideo.removeAttribute("poster");
        }

        lightboxVideo.setAttribute("aria-label", label || "Portfolio video");
        lightboxVideo.load();

        lightbox.classList.add("open");
        lightbox.setAttribute("aria-hidden", "false");

        lightboxVideo.play().catch(function () {
            // autoplay may be blocked until user presses play
        });
    }

    function closeLightbox() {
        resetStage();
        activeType = "image";

        lightbox.classList.remove("open", "zoomed");
        lightbox.setAttribute("aria-hidden", "true");

        lightboxImg.onload = null;
        lightboxImg.src = "";
        lightboxImg.alt = "";
        lightboxImg.style.display = "block";
        lightboxImg.style.width = "";
        lightboxImg.style.height = "";
        lightboxImg.style.maxWidth = "";
        lightboxImg.style.maxHeight = "";

        stopVideo();
    }

    document.querySelectorAll(".port-img, .port-thumb").forEach(function (item) {
        item.addEventListener("click", function (e) {
            e.stopPropagation();

            const type = item.dataset.type || "image";
            const label = item.dataset.alt || item.getAttribute("aria-label") || item.alt || "";

            if (type === "video") {
                openVideo(item.dataset.src, item.dataset.poster, label);
                return;
            }

            const fullImage = item.dataset.full || item.getAttribute("src");
            openImage(fullImage, label);
        });
    });

    lightboxImg.addEventListener("click", function (e) {
        if (activeType !== "image") {
            return;
        }

        e.stopPropagation();
        zoomLevel = zoomLevel === 1 ? 2 : 1;
        applyZoom();
    });

    lightbox.addEventListener("wheel", function (e) {
        if (!lightbox.classList.contains("open") || activeType !== "image") {
            return;
        }

        e.preventDefault();

        if (e.deltaY < 0) {
            zoomLevel = Math.min(4, zoomLevel + 0.25);
        } else {
            zoomLevel = Math.max(1, zoomLevel - 0.25);
        }

        applyZoom();
    }, { passive: false });

    if (closeBtn) {
        closeBtn.addEventListener("click", closeLightbox);
    }

    lightbox.addEventListener("click", function (e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });

    document.addEventListener("keydown", function (e) {
        if (e.key === "Escape") {
            closeLightbox();
        }
    });
});
