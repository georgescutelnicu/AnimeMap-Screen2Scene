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
    anime_details = db.session.query(AnimeDetails).all()
    anime_locations = db.session.query(AnimeLocation).all()

    locations_data = [{
        "location_name": location.location_name,
        "coordinates": location.coordinates,
        "real_photos": location.real_photos,
        "anime_photos": location.anime_photos
    } for location in anime_locations]

    return render_template("index.html", anime_details = anime_details, anime_locations = locations_data)


if __name__ == '__main__':
    app.run(debug=True)
