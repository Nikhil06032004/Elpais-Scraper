from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def accept_cookies(driver):
    wait = WebDriverWait(driver, 5)

    try:
        accept_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Aceptar') or contains(., 'Accept')]")
            )
        )
        accept_button.click()
        print("Cookies accepted")
    except:
        pass  # If no popup appears, continue normally
