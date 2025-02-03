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

  L.tileLayer('https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}&hl=en', {
  attribution: '&copy; Google Maps',
  }).addTo(map);

  var customIcon = L.icon({
    iconUrl: "/static/images/logo.png",
    iconSize: [30, 40],
    iconAnchor: [20, 40],
    popupAnchor: [0, -40]
  });

var locations = [];
mapPins.forEach(function(location) {
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
        <b><button class="mapButton" onclick="showLocation('${location.name}')">${location.name}</button></b>
      `);
  });
});

function showAnime(animeName) {
    const anime = animeDetails[animeName];
    let html = `<div class="location-container">`;

    html += `<div class="title">${anime.english_name}
    ${anime.romaji_name.toLowerCase() != anime.english_name.toLowerCase() ? ' - ' + anime.romaji_name : ''}</div>`;

    html += `
        <p class="info">
            <span class="anime-type">${anime.anime_type}</span> |
            <span class="year">${anime.year_of_release}</span> |
            <span class="episodes">${anime.number_of_episodes} episodes</span>
        </p>
    `;

    html += `<p class="description">${anime.description.replace(/\s*\[Written by MAL Rewrite\]$/, '')}</p>`;

    html += `<div class="locations">`;
    for (let locationKey in anime.locations) {
        const location = anime.locations[locationKey];

        html += `<div class="location">`;
        html += `<h4 class="location-name">${location.location_name}</h4>`;

        let animePhotos = JSON.parse(location.anime_photos.replace(/'/g, '"'));
        let realPhotos = JSON.parse(location.real_photos.replace(/'/g, '"'));

        html += `<div class="photos">`;
        for (let i = 0; i < animePhotos.length; i++) {
            html += `
                <div class="flip-container">
                    <div class="flipper">
                        <div class="front">
                            <img class="photo" src="${animePhotos[i]}" alt="Anime Photo ${i+1}" />
                        </div>
                        <div class="back">
                            <img class="photo" src="${realPhotos[i]}" alt="Real Photo ${i+1}" />
                        </div>
                    </div>
                </div>
            `;
        }
        html += `</div>`;
        html += `</div>`;
    }
    html += `</div>`;

    html += `</div>`;

    document.getElementById('infoContent').innerHTML = html;
}

function showLocation(locationName) {
    const locations = animeLocations[locationName];

    let html = `<div class="location-container">`;
    html += `<div class="title">${locations[0].location_name}</div>`;

    locations.forEach(loc => {
        const details = loc.anime_details;

        html += `<h3 class="subtitle">${details.english_name}${
            details.english_name.toLowerCase() !== details.romaji_name.toLowerCase()
                ? ` <span class="subtitle">- ${details.romaji_name}</span>`
                : ""
        }</h3>`;

        let animePhotos = [];
        let realPhotos = [];

        animePhotos = JSON.parse(loc.anime_photos.replace(/'/g, '"'));
        realPhotos = JSON.parse(loc.real_photos.replace(/'/g, '"'));

        html += `<div class="photos">`;
        for (let i = 0; i < animePhotos.length; i++) {
            html += `
                <div class="flip-container">
                    <div class="flipper">
                        <div class="front">
                            <img class="photo" src="${animePhotos[i]}" alt="Anime Photo ${i+1}" />
                        </div>
                        <div class="back">
                            <img class="photo" src="${realPhotos[i]}" alt="Real Photo ${i+1}" />
                        </div>
                    </div>
                </div>
            `;
        }
        html += `</div>`;

    });

    html += `</div>`;

    document.getElementById('infoContent').innerHTML = html;
}
