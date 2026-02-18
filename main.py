import os

from dotenv import load_dotenv

from src.driver_factory import create_driver
from src.navigator import navigate_to_opinion
from src.scraper import scrape_first_five_articles
from src.article_extractor import extract_article_content
from src.image_downloader import download_cover_image
from src.translator import translate_to_english
from src.text_analyzer import analyze_repeated_words


def process_article(driver, index, article):
    print("\n==============================")
    print(f"Article {index}")
    print("Spanish Title:", article["title"])
    print("URL:", article["link"])

    content = extract_article_content(driver, article["link"])
    print("\nContent (Spanish):\n")
    print(content[:1000])

    download_cover_image(driver, article["title"])

    translated_title = translate_to_english(article["title"])
    print("\nTranslated Title (English):", translated_title)

    return translated_title


def run_automation(driver=None, session_name=None):
    """
    Main automation workflow.
    Accepts optional driver (for BrowserStack parallel runs).
    Accepts optional session_name for BrowserStack session status marking.
    """

    print(f"Starting El País automation{f' [{session_name}]' if session_name else ''}...\n")

    driver_created_here = False
    if driver is None:
        driver = create_driver()
        driver_created_here = True

    translated_titles = []
    status = "failed"
    reason = ""

    try:
        navigate_to_opinion(driver)

        articles = scrape_first_five_articles(driver)

        for index, article in enumerate(articles, start=1):
            translated_title = process_article(driver, index, article)
            translated_titles.append(translated_title)

        analyze_repeated_words(translated_titles)

        status = "passed"
        reason = "All 5 articles scraped, translated, and analyzed successfully."

    except Exception as e:
        reason = str(e)
        print(f"\n[ERROR] {e}")

    finally:
        # Mark BrowserStack session as passed/failed
        try:
            driver.execute_script(
                f'browserstack_executor: {{"action": "setSessionStatus", '
                f'"arguments": {{"status": "{status}", "reason": "{reason}"}}}}'
            )
        except Exception:
            pass  # Not a BrowserStack session (local run), skip silently

        if driver_created_here:
            driver.quit()
            print("\nBrowser closed successfully.")


def main():
    load_dotenv()
    run_automation()


if __name__ == "__main__":
    main()