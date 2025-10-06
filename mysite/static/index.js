document.addEventListener("DOMContentLoaded", () => {
  const carousel = document.querySelector(".carousel-container");
  const slide = document.querySelector(".carousel-slide");
  const style = getComputedStyle(carousel);
  const gap = parseInt(style.gap) || 8;

  function carouselMove(positive = true) {
    const slideWidth = slide.clientWidth + gap;

    if (positive) {
      if (
        carousel.scrollLeft + carousel.clientWidth >=
        carousel.scrollWidth - slideWidth
      ) {
        carousel.scrollLeft = 0;
      } else {
        carousel.scrollLeft += slideWidth;
      }
    } else {
      if (carousel.scrollLeft <= 0) {
        carousel.scrollLeft = carousel.scrollWidth - carousel.clientWidth;
      } else {
        carousel.scrollLeft -= slideWidth;
      }
    }
  }

  setInterval(() => carouselMove(true), 4000);
  window.carouselMove = carouselMove; // чтобы кнопки могли вызывать функцию
});

setInterval(() => {
  carouselMove(true);
}, 4000);
