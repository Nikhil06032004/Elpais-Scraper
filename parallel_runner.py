import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

from main import run_automation
from src.driver_factory import create_driver


browser_combinations = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "buildName": "ElPais Parallel Build",
        "sessionName": "Chrome Win11"
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "10",
        "buildName": "ElPais Parallel Build",
        "sessionName": "Firefox Win10"
    },
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "buildName": "ElPais Parallel Build",
        "sessionName": "Edge Win11"
    },
    {
        "deviceName": "iPhone 14",
        "realMobile": "true",
        "osVersion": "16",
        "buildName": "ElPais Parallel Build",
        "sessionName": "iPhone 14"
    },
    {
        "deviceName": "Samsung Galaxy S23",
        "realMobile": "true",
        "osVersion": "13.0",
        "buildName": "ElPais Parallel Build",
        "sessionName": "Galaxy S23"
    },
]


def run_parallel_test(caps):
    session_name = caps.get("sessionName", "unknown")
    print(f"Starting session: {session_name}")
    driver = create_driver(caps)
    run_automation(driver, session_name=session_name)


if __name__ == "__main__":
    load_dotenv()
    os.environ["USE_BROWSERSTACK"] = "true"

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(run_parallel_test, caps) for caps in browser_combinations]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print("Thread failed with error:", e)