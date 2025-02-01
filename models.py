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

    def to_dict(self):
        anime_dict = {
            "japanese_name": self.japanese_name,
            "romaji_name": self.romaji_name,
            "english_name": self.english_name,
            "image_url": self.image_url,
            "anime_type": self.anime_type,
            "number_of_episodes": self.number_of_episodes,
            "year_of_release": self.year_of_release,
            "description": self.description,
            "locations": {location.location_name: location.to_dict() for location in self.locations}
        }
        return anime_dict


class AnimeLocation(db.Model):
    __tablename__ = "anime_location"

    id = db.Column(db.Integer, primary_key=True)
    anime_name = db.Column(db.String, db.ForeignKey("anime_details.japanese_name"), nullable=False)
    location_name = db.Column(db.String, nullable=False)
    coordinates = db.Column(db.String, nullable=False)
    real_photos = db.Column(db.String, nullable=False)
    anime_photos = db.Column(db.String, nullable=False)

    def to_dict(self):
        location_dict = {
            "location_name": self.location_name,
            "coordinates": self.coordinates,
            "real_photos": self.real_photos,
            "anime_photos": self.anime_photos,
            "anime_details": {
                "japanese_name": self.anime_details.japanese_name,
                "english_name": self.anime_details.english_name,
                "romaji_name": self.anime_details.romaji_name,
                "anime_type": self.anime_details.anime_type,
                "year_of_release": self.anime_details.year_of_release,
                "number_of_episodes": self.anime_details.number_of_episodes,
                "description": self.anime_details.description
            }
        }
        return location_dict
