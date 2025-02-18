# AnimeMap-Screen2Scene

## Overview
AnimeMap-Screen2Scene is a web application that maps real-world locations featured in anime. Users can explore a map with anime-related locations and view details about the anime and their corresponding scenes.

## Tech Stack
- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript, Leaflet.js
- **Database:** PostgreSQL (via SQLAlchemy ORM)

## Data
A data folder is included in the project, containing data used to populate the map. The only modification from the original scraped data was adding a coordinates column to the location table.
Additionally, some location names were missing, so i had to manually updated them.

## Demo
Hosted on [Render](https://render.com/).
<br>
Please note that it may take up to 1 minute to start when first accessed, as I am using a free instance on Render. <br>
This is due to the instance spinning down after a period of inactivity. Once it's warmed up, the loading times will be faster.
<br><br>
<a href="https://animemap-screen2scene.onrender.com/">
    <img src="https://img.shields.io/badge/AnimeMap Screen2Scene-0088e7?logo=render&logoColor=fff&style=for-the-badge"></img>
</a>

## Acknowledgments
Special thanks to [フラバーのふらふらアニメ聖地巡礼](https://furaba-animeseichi.blog.jp/) for their amazing work in mapping anime pilgrimage locations.

