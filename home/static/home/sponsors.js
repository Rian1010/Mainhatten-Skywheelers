const sponsors = document.querySelector('.sponsor-sec');

let rect = sponsors.getBoundingClientRect(),
    sponsorsTop = rect.top,
    oldScrollY = window.scrollY;

document.addEventListener('scroll', () => {
    if (oldScrollY < window.scrollY && window.pageYOffset > sponsorsTop / 2) {
        sponsors.scrollLeft += 9;
    } else if (window.scrollY < oldScrollY) {
        sponsors.scrollLeft -= 9;
    }
    oldScrollY = window.scrollY;
});