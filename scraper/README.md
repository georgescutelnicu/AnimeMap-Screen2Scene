# Anime Scraper


This Python script scrapes pictures from anime that can be found in real places in Japan, location details from [Furaba Anime Seichi](https://furaba-animeseichi.blog.jp/) and fetches additional anime information using the Jikan API. The scraped data is saved into CSV files for further analysis.

## Prerequisites

- Python 3.x
- Install the required Python packages listed in requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Arguments

- **-i, --ids**: A list of anime IDs to scrape (**required**). Make sure the ID exists on the website. For example, the URL https://furaba-animeseichi.blog.jp/archives/**35846680**.html has the ID **35846680**.
- **-n, --csv_name**: The name for the output CSV files (**required**).

```bash
python scraper.py -p 1 -k "java" -n "java_jobs"
```

### Example Command

```bash
python scraper.py --ids 35846680 --csv_name output
```

### Output Files

**output-anime.csv**: Contains anime details (e.g., Japanese name, English name, synopsis).

**output-location.csv**: Contains location details (e.g., location name, real photos, anime photos).

## Example Output

| Japanese Name | Romaji Name     | English Name | Image URL                  | Type | Number of Episodes | Year of Release | Description       |
|---------------|-----------------|--------------|----------------------------|------|--------------------|-----------------|-------------------|
| 鬼滅の刃       | Kimetsu no Yaiba | Demon Slayer | https://example.com/image.jpg | TV   | 26                 | 2019            | A story about...  |

| Anime Name | Location Name |Coordinates | Real Photos               | Anime Photos               |
|------------|---------------|------------|---------------------------|----------------------------|
| 鬼滅の刃    | Ashikaga Flower Park      | 44.39315051849718, 26.042991665924724 |[photo1.jpg, photo2.jpg]  | [anime1.jpg, anime2.jpg]   |

## Notes

**Respect robots.txt**: Always check the website's robots.txt file before scraping to ensure compliance with their rules.

**Rate Limiting**: The script includes a 5-second delay between requests to avoid overwhelming the server.

**Error Handling**: The script stops execution if a non-200 status code is encountered during scraping.

## Acknowledgments
[Furaba Anime Seichi](https://furaba-animeseichi.blog.jp/) for providing the locations and images used in this project.

[Jikan API](https://jikan.moe/) for providing anime data.

[Deep Translator](https://github.com/nidhaloff/deep-translator) for Japanese-to-English translation.