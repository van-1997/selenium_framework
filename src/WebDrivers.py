import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def read_json(file_path):
        with open(file_path, "r") as file:
            json_data = json.load(file)
        return json_data


class WebDriverFactory:
    def __init__(self, json_data):
        self.json_data = json_data

    def driver(self, url):
        driver_type = self.json_data.get("driver_type", "").lower()
        screen_width = self.json_data.get("weight")
        screen_height = self.json_data.get("height")

        if driver_type == "chrome":
            chrome_options = ChromeOptions()
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.set_window_size(screen_width, screen_height)
            driver.get(url)
            return driver

        elif driver_type == "firefox":
            firefox_options = FirefoxOptions()
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
            driver.set_window_size(screen_width, screen_height)
            driver.get(url)
            return driver

file_path = "/home/vanya/PycharmProjects/selenium_framework/global_vars.json"
json_data = read_json(file_path)
webdriver_factory = WebDriverFactory(json_data)

url = "https://www.facebook.com"

driver = webdriver_factory.driver(url)
time.sleep(5)
driver.quit()

