import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://elpais.com/?lang=es")
MAX_ARTICLES = int(os.getenv("MAX_ARTICLES", 5))
PAGE_LOAD_TIMEOUT = 60
