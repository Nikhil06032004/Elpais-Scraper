from src.cookie_handler import accept_cookies


def navigate_to_opinion(driver):
    opinion_url = "https://elpais.com/opinion/"
    driver.get(opinion_url)

    accept_cookies(driver)

    print("Navigated directly to Opinion section")
