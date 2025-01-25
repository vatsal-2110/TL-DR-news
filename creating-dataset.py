from mira_sdk import MiraClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("my_API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

# Create dataset
client.dataset.create("vatsal2110/news-data-2", "dataset for the news")

# Add URL to your data set (URL must be added to an existing dataset)
# url = input("url: ")
client.dataset.add_source("vatsal2110/news-data-2", url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtUmxHZ0pFUlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en")
client.dataset.add_source("vatsal2110/news-data-2", url="https://www.news18.com/")
client.dataset.add_source("vatsal2110/news-data-2", url="https://www.ndtv.com")

client.dataset.add_source("vatsal2110/news-data-2", url="https://www.indiatoday.in/latest-news")


