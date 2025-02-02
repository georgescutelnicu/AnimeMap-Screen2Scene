import requests
import pandas as pd
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import argparse
import time
import sys

# Anime data
japanese_name = []
romaji_name = []
english_name = []
image_url = []
anime_type = []
number_of_episodes = []
year_of_release = []
description = []

# Location data
_japanese_name = []
location_name = []
real_photos = []
anime_photos = []


class WebScraper:
    """
    A web scraper class to scrape anime and location details from a given URL.
    """

    def __init__(self, url):
        """
        Initializes the WebScraper with a URL.

        Args:
            url (str): The URL to scrape data from.
        """
        self.url = url
        self.name = ""
        self.temp_location_name = []
        self.temp_real_photos = []
        self.temp_anime_photos = []

    def get_details(self):
        """
        Scrapes anime and location details from the webpage.

        Returns:
            str: The name of the anime in Japanese, if found, in order to use it with JikanAPI.
        """
        response = requests.get(self.url)
        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            sys.exit(1)

        soup = BeautifulSoup(response.content, "html.parser")

        anime_name = soup.find("h2", class_="category-name")
        if anime_name:
            name = anime_name.get_text(strip=True)
            japanese_name.append(name)
        else:
            print("No <h2> tag with class 'category-name' found.")
            sys.exit(1)

        article_body = soup.find("div", class_="article-body-inner")

        for element in article_body.find_all():
            if element.name == "span" and "《" in element.text:
                location = element.text[1:-2]

                if location not in self.temp_location_name:
                    self.temp_location_name.append(location)
                    location_name.append(self.to_english(location))
                    _japanese_name.append(name)

                    if len(self.temp_real_photos) > 0:
                        real_photos.append(self.temp_real_photos)
                        anime_photos.append(self.temp_anime_photos)
                        self.temp_real_photos = []
                        self.temp_anime_photos = []

            elif element.name == "img" and element.get("src"):
                image_url = element["src"]

                if image_url not in self.temp_real_photos and image_url not in self.temp_anime_photos:
                    if len(self.temp_real_photos) <= len(self.temp_anime_photos):
                        self.temp_real_photos.append(image_url)
                    else:
                        self.temp_anime_photos.append(image_url)

        real_photos.append(self.temp_real_photos)
        anime_photos.append(self.temp_anime_photos)

        return anime_name

    def to_english(self, text):
        """
        Translates Japanese text to English.

        Args:
            text (str): The text to translate.

        Returns:
            str: The translated text.
        """
        translator = GoogleTranslator(source="ja", target="en")
        translated_text = translator.translate(text)

        return translated_text

    def save_to_csv(self, name):
        """
        Saves scraped data to CSV files.

        Args:
            name (str): The base name for the output CSV files.
        """
        anime_data = {
            "Japanese_Name": japanese_name,
            "Romaji_Name": romaji_name,
            "English_Name": english_name,
            "Image_URL": image_url,
            "Anime_Type": anime_type,
            "Number_of_Episodes": number_of_episodes,
            "Year_of_Release": year_of_release,
            "Description": description,
        }

        location_data = {
            "Anime_Name": _japanese_name,
            "Location_Name": location_name,
            "Real_Photos": real_photos,
            "Anime_Photos": anime_photos,
        }

        anime_df = pd.DataFrame(anime_data)
        location_df = pd.DataFrame(location_data)

        anime_df.to_csv(f"{name}-anime.csv", index=False)
        print(f"Anime data saved to {name}-anime.csv")

        location_df.to_csv(f"{name}-location.csv", index=False)
        print(f"Location data saved to {name}-location.csv")


class JikanAPI:
    """
    A class to interact with the Jikan API to fetch anime details.
    """

    def __init__(self, base_url="https://api.jikan.moe/v4/anime"):
        """
        Initializes the JikanAPI with the base URL.

        Args:
            base_url (str): The base URL for the Jikan API. Default is "https://api.jikan.moe/v4/anime".
        """
        self.base_url = base_url

    def get_anime_details(self, anime_name):
        """
        Fetches anime details from the Jikan API.

        Args:
            anime_name (str): The name of the anime to fetch details for.
        """
        params = {"q": anime_name, "limit": 1}
        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch data from Jikan API. Status code: {response.status_code}")
            sys.exit(1)

        data = response.json()
        if data["data"]:
            anime_data = data["data"][0]
            romaji_name.append(anime_data["titles"][0]["title"])
            english_name.append(anime_data["titles"][-1]["title"])
            image_url.append(anime_data["images"]["jpg"]["large_image_url"])
            anime_type.append(anime_data["type"])
            number_of_episodes.append(anime_data["episodes"])
            year_of_release.append(anime_data["year"])
            description.append(anime_data["synopsis"])
        else:
            print("No anime data found for the given name.")


# Argument parsing and script execution logic
parser = argparse.ArgumentParser(description="Scrape pictures from anime that can be found in real places in Japan"
                                             " and location details and fetch additional data using Jikan API.")
parser.add_argument("--ids", "-i", nargs="+", required=True, type=int, help="List of anime IDs to scrape.")
parser.add_argument("--csv_name", "-n", required=True, type=str, help="Base name for the output CSV files.")
args = parser.parse_args()

anime_ids = args.ids
csv_name = args.csv_name

for anime_id in anime_ids:
    url = f"https://furaba-animeseichi.blog.jp/archives/cat_{anime_id}.html"

    scraper = WebScraper(url)
    jikan_api = JikanAPI()

    jp_anime_name = scraper.get_details()
    jikan_api.get_anime_details(jp_anime_name)

    time.sleep(5)

scraper.save_to_csv(csv_name)
