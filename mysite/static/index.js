let currentIndex = 0;

function carouselMove(forward = true) {
  const container = document.querySelector(".carousel-container");
  const slides = document.querySelectorAll(".carousel-slide");

  if (!slides.length) return;


  const gap = 8; 
  const slideWidth = slides[0].offsetWidth + gap;

  
  if (forward) {
    currentIndex = (currentIndex + 1) % slides.length;
  } else {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
  }


  container.scrollTo({
    left: slideWidth * currentIndex,
    behavior: "smooth",
  });
}
