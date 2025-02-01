from flask import Flask, render_template, request
from models import db, AnimeDetails, AnimeLocation
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

db.init_app(app)

@app.route("/")
def home():
    map_pins = []
    anime_details_dict = {}
    anime_locations_dict = {}

    anime_details = db.session.query(AnimeDetails).all()
    anime_locations = db.session.query(AnimeLocation).all()

    for anime in anime_details:
        anime_details_dict[anime.japanese_name] = anime.to_dict()

    for location in anime_locations:
        map_pins.append({
            "location_name": location.location_name,
            "coordinates": location.coordinates,
        })
        anime_locations_dict[location.location_name] = location.to_dict()

    return render_template("index.html", anime_details = anime_details_dict, anime_locations = anime_details_dict,
                           map_pins = map_pins)


if __name__ == '__main__':
    app.run(debug=True)
