from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.cookie_handler import accept_cookies
import time
import re


CONTENT_SELECTORS = (
    "article p, "
    "div[data-dtm-region='articulo_cuerpo'] p, "
    "article div > p, "
    "article div[class*='body'] p"
)


EXCLUDED_KEYWORDS = [
    "compartir",
    "whatsapp",
    "facebook",
    "twitter",
    "linkedin",
    "copiar enlace",
    "comentarios",
    "suscríbete",
    "newsletter",
    "ir a los comentarios"
]


def _is_valid_paragraph(text: str) -> bool:
    """
    Applies content filtering rules to remove UI noise,
    metadata, captions, and non-article elements.
    """

    if not text:
        return False

    if len(text) < 60:
        return False

    lower_text = text.lower()

    if any(keyword in lower_text for keyword in EXCLUDED_KEYWORDS):
        return False

    if re.search(r"\d+\s*fotos?", lower_text):
        return False

    if text.isupper():
        return False

    if re.match(r"^[A-ZÁÉÍÓÚÑ\s]+$", text) and len(text.split()) <= 4:
        return False

    if re.search(r"\d{1,2}\s+[A-Z]{3}\s+\d{4}", text):
        return False

    return True


def _normalize_text(text: str) -> str:
    """
    Normalizes whitespace and formatting.
    """
    return re.sub(r"\s+", " ", text).strip()


def extract_article_content(driver, url: str) -> str:
    """
    Extracts structured textual content from El País opinion articles.
    Supports standard and photo-essay layouts.
    """

    driver.get(url)
    accept_cookies(driver)

    wait = WebDriverWait(driver, 20)

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight / 2);"
    )
    time.sleep(2)

    try:
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
    except TimeoutException:
        return ""

    clean_paragraphs = []

    # Primary extraction strategy
    elements = driver.find_elements(By.CSS_SELECTOR, CONTENT_SELECTORS)

    for element in elements:
        text = _normalize_text(element.text)

        if _is_valid_paragraph(text):
            clean_paragraphs.append(text)

    # Controlled fallback for layout variations
    if not clean_paragraphs:
        div_blocks = driver.find_elements(By.CSS_SELECTOR, "article div")

        for block in div_blocks:
            text = _normalize_text(block.text)

            if len(text) > 80 and _is_valid_paragraph(text):
                clean_paragraphs.append(text)

    return "\n\n".join(clean_paragraphs)
