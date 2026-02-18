from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_first_five_articles(driver):
    wait = WebDriverWait(driver, 20)

    # Wait for real article headline links to appear
    wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "article h2 a[href*='/202']")
        )
    )

    links = driver.find_elements(By.CSS_SELECTOR, "article h2 a[href*='/202']")

    article_data = []

    for link in links:
        title = link.text.strip()
        url = link.get_attribute("href")

        if title and url and "/202" in url:
            article_data.append({
                "title": title,
                "link": url
            })

        if len(article_data) == 5:
            break

    return article_data
