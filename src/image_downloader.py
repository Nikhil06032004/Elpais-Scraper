import os
import re
import unicodedata
import requests
from selenium.webdriver.common.by import By


def sanitize_filename(title: str) -> str:
    """
    Convert title to ASCII-safe filename.
    Removes accents and special characters.
    """

    # Normalize accents (á → a, ñ → n, etc.)
    normalized = unicodedata.normalize("NFKD", title)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")

    # Replace non-alphanumeric characters with underscore
    ascii_text = re.sub(r"[^a-zA-Z0-9]+", "_", ascii_text)

    # Remove leading/trailing underscores
    ascii_text = ascii_text.strip("_")

    return ascii_text


def download_cover_image(driver, title):
    """
    Downloads the main article image.
    Returns a JSON-safe relative path (forward slashes).
    """

    try:
        # More specific selector (safer than generic img)
        image_element = driver.find_element(By.CSS_SELECTOR, "article img")
        image_url = image_element.get_attribute("src")

        if not image_url:
            return None

        # Request image
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        # Prepare directory
        save_dir = os.path.join("assets", "images")
        os.makedirs(save_dir, exist_ok=True)

        # Sanitize filename
        clean_name = sanitize_filename(title)
        filename = f"{clean_name}.jpg"

        full_path = os.path.join(save_dir, filename)

        # Save file
        with open(full_path, "wb") as f:
            f.write(response.content)

        print(f"Image saved: {filename}")

        # Convert Windows backslashes → forward slashes for JSON
        json_path = full_path.replace("\\", "/")

        return json_path

    except Exception as e:
        print(f"[WARNING] Image download failed: {e}")
        return None
