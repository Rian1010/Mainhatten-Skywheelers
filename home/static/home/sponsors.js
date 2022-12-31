const sponsors = document.querySelector('.sponsor-sec');

let rect = sponsors.getBoundingClientRect(),
    sponsorsTop = rect.top,
    oldScrollY = window.scrollY;

document.addEventListener('scroll', () => {
    if (oldScrollY < window.scrollY && window.pageYOffset > sponsorsTop / 3) {
        sponsors.scrollLeft += 11;
    } else if (window.scrollY < oldScrollY) {
        sponsors.scrollLeft -= 11;
    }
    oldScrollY = window.scrollY;
});