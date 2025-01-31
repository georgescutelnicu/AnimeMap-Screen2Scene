//  Carousel section
const gap = 16;

const carousel = document.getElementById("carousel"),
  content = document.getElementById("content"),
  next = document.getElementById("next"),
  prev = document.getElementById("prev");

let width;
let itemWidth;
let numVisibleItems;
let currentScrollIndex = 0;

function updateCarousel() {
  width = carousel.offsetWidth;

  const items = document.querySelectorAll(".item");

  numVisibleItems = Math.floor((width + gap) / (200 + gap));
  if (numVisibleItems < 1) numVisibleItems = 1;

  itemWidth = Math.floor((width - (numVisibleItems - 1) * gap) / numVisibleItems);

  items.forEach((item) => {
    item.style.width = `${itemWidth}px`;
  });

  carousel.scrollLeft = currentScrollIndex * (itemWidth + gap);

  prev.style.display = currentScrollIndex > 0 ? "flex" : "none";
  next.style.display = currentScrollIndex + numVisibleItems < items.length ? "flex" : "none";
}

next.addEventListener("click", () => {
  const items = document.querySelectorAll(".item");
  const maxIndex = items.length - numVisibleItems;

  currentScrollIndex = Math.min(currentScrollIndex + numVisibleItems, maxIndex);
  carousel.scrollTo({ left: currentScrollIndex * (itemWidth + gap), behavior: "smooth" });

  prev.style.display = "flex";
  if (currentScrollIndex >= maxIndex) {
    next.style.display = "none";
  }
});

prev.addEventListener("click", () => {
  currentScrollIndex = Math.max(currentScrollIndex - numVisibleItems, 0);
  carousel.scrollTo({ left: currentScrollIndex * (itemWidth + gap), behavior: "smooth" });

  next.style.display = "flex";
  if (currentScrollIndex <= 0) {
    prev.style.display = "none";
  }
});

window.addEventListener("resize", updateCarousel);
updateCarousel();


// Map section
document.addEventListener("DOMContentLoaded", function () {
  var map = L.map('map').setView([35.6895, 139.6917], 5); // Tokyo center

  L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    attribution: '&copy; Google Maps',
  }).addTo(map);

  var customIcon = L.icon({
    iconUrl: "/static/images/logo.png",
    iconSize: [30, 40],
    iconAnchor: [20, 40],
    popupAnchor: [0, -40]
  });

  var locations = [
    { coords: [35.7101, 139.8107], name: "Tokyo Skytree" },
    { coords: [35.6895, 139.6917], name: "Shinjuku" },
    { coords: [35.6586, 139.7454], name: "Tokyo Tower" },
    { coords: [35.7118, 139.7967], name: "Asakusa" }
  ];

  locations.forEach(function (location, index) {
    L.marker(location.coords, { icon: customIcon })
      .addTo(map)
      .bindPopup(`
        <b><button class="mapButton" onclick="flipMap(${index})">${location.name}</button></b>
      `);
  });
});

function flipMap(index) {
  alert(`Flip map function triggered for location: ${index}`);
}
