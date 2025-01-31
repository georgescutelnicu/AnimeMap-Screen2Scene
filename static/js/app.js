const carousel = document.getElementById("carousel");
const content = document.getElementById("content");

let width;
let itemWidth;
let numVisibleItems;
let currentScrollIndex = 0;
const gap = 16;

function updateCarousel() {
  width = carousel.offsetWidth;

  const items = document.querySelectorAll(".item");

  numVisibleItems = Math.floor((width + gap) / (200 + gap));
  if (numVisibleItems < 1) numVisibleItems = 1;

  itemWidth = Math.floor((width - (numVisibleItems - 1) * gap) / numVisibleItems);

  items.forEach((item) => {
    item.style.width = `${itemWidth}px`;
  });
}

carousel.addEventListener("wheel", (e) => {
  e.preventDefault();
  const scrollAmount = numVisibleItems * (itemWidth + gap);
  carousel.scrollBy({ left: e.deltaY > 0 ? scrollAmount : -scrollAmount, behavior: "smooth" });
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

var locations = [];
animeLocations.forEach(function(location) {
    var coords = location.coordinates.split(', ').map(Number);

    locations.push({
        coords: coords,
        name: location.location_name
    });
});

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
