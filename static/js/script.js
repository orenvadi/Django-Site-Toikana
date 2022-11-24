import './swiper.js'
// src = "https://cdn.jsdelivr.net/npm/swiper@8/swiper-bundle.min.js"

const swiper = new Swiper('.swiper', {
  direction: 'horizontal',
  loop: true,
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
