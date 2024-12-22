from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


service = Service('/Users/phuonganhpham/chromedriver/chromedriver')


class Scraper:
    BASE_URL = "https://www.bbc.com"

    # Map subcategories to URLs
    CATEGORY_MAP = {
        "News": {
            "War in Ukraine": "news/war-in-ukraine",
            "US & Canada": "news/us-canada",
            "UK": "news/uk",
            "Africa": "news/world/africa",
            "Asia": "news/world/asia",
            "Australia": "news/world/australia",
            "Europe": "news/world/europe",
            "Latin America": "news/world/latin_america",
            "Middle East": "news/world/middle_east",
            "BBC InDepth": "news/bbcindepth",
        },
        "Sport": {
            "Football": "sport/football",
            "Cricket": "sport/cricket",
            "Formula 1": "sport/formula1",
            "Rugby Union": "sport/tennis",
            "Golf": "sport/golf",
            "Athletics": "sport/athletics",
            "Cycling": "sport/cycling",
        },
        "Business": {
            "Executive Lounge": "business/executive-lounge",
            "Technology of Business": "business/technology-of-business",
            "Future of Business": "business/future-of-business",
        },
        "Innovation": {
            "Technology": "innovation/technology",
            "Science": "innovation/science",
            "Artificial Intelligence": "innovation/artificial-intelligence",
            "AI v the Mind": "innovation/ai-v-the-mind",
        },
        "Culture": {
            "Film & TV": "culture/film-tv",
            "Music": "culture/music",
            "Art": "culture/art",
            "Style": "culture/style",
            "Books": "culture/books",
            "Entertainment News": "culture/entertainment-news",
        },
        "Travel": {
            "Destinations": "travel/destinations",
            "Worlds Table": "travel/worlds-table",
            "Cultural Experiences": "travel/cultural-experiences",
            "Adventures": "travel/adventures",
            "Specialist": "travel/specialist",
        },
    }

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def scrape_bbc_subcategory(self, main_category, subcategory):
        try:
            # Get subcategory URL
            subcategory_path = self.CATEGORY_MAP.get(main_category, {}).get(subcategory)
            if not subcategory_path:
                raise ValueError("Invalid category or subcategory")

            url = f"{self.BASE_URL}/{subcategory_path}"
            self.driver.get(url)
            
            # Scrape articles
            articles = []
            headlines = self.driver.find_elements(By.CLASS_NAME, "sc-8ea7699c-3")
            descriptions = self.driver.find_elements(By.CLASS_NAME, "sc-b8778340-4")

            for i, headline in enumerate(headlines):
                description_text = descriptions[i].text if i < len(descriptions) else "No description available."
                articles.append({
                    "headline": headline.text,
                    "description": description_text
                })
            return articles
        except Exception as e:
            print(f"Error scraping BBC subcategory: {e}")
            return []
        finally:
            self.driver.quit()
