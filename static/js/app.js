document.addEventListener("DOMContentLoaded", function () {
    const banner = document.getElementById("banner");
    const images = banner.getElementsByTagName("img");
    const interval = parseInt(banner.dataset.interval); // Convert to number

    let currentImageIndex = 0;

    function showImage(index) {
        for (let i = 0; i < images.length; i++) {
            images[i].style.display = "none";
        }
        images[index].style.display = "block";
        currentImageIndex = index;
    }

    function nextImage() {
        currentImageIndex = (currentImageIndex + 1) % images.length;
        showImage(currentImageIndex);
    }

    showImage(currentImageIndex);
    setInterval(nextImage, interval);
});