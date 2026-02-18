import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver(custom_caps=None):

    use_browserstack = os.getenv("USE_BROWSERSTACK", "false").lower() == "true"

    if use_browserstack:
        username = os.getenv("BROWSERSTACK_USERNAME")
        access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")

        if not username or not access_key:
            raise Exception("BROWSERSTACK_USERNAME or BROWSERSTACK_ACCESS_KEY not set in .env!")

        if not custom_caps:
            raise Exception("BrowserStack capabilities not provided!")

        options = webdriver.ChromeOptions()

        for key, value in custom_caps.items():
            options.set_capability(key, value)

        driver = webdriver.Remote(
            command_executor=f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub",
            options=options
        )

        return driver

    else:
        options = Options()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(options=options)