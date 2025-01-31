from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AnimeDetails(db.Model):
    __tablename__ = "anime_details"

    id = db.Column(db.Integer, primary_key=True)
    japanese_name = db.Column(db.String, unique=True, nullable=False)
    romaji_name = db.Column(db.String, nullable=False)
    english_name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    anime_type = db.Column(db.String, nullable=False)
    number_of_episodes = db.Column(db.Integer, nullable=False)
    year_of_release = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)

    locations = db.relationship("AnimeLocation", backref="anime_details")


class AnimeLocation(db.Model):
    __tablename__ = "anime_location"

    id = db.Column(db.Integer, primary_key=True)
    anime_name = db.Column(db.String, db.ForeignKey("anime_details.japanese_name"), nullable=False)
    location_name = db.Column(db.String, nullable=False)
    coordinates = db.Column(db.String, nullable=False)
    real_photos = db.Column(db.String, nullable=False)
    anime_photos = db.Column(db.String, nullable=False)
