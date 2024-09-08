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
    try:
        with open(file_path, "r") as file:
            json_data = json.load(file)
        return json_data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")


class WebDriverFactory:
    def __init__(self, json_data):
        self.driver_type = json_data.get("driver_type", "").lower()
        self.screen_width = json_data.get("width")
        self.screen_height = json_data.get("height")


    def driver(self, url):

        if self.driver_type == "chrome":
            chrome_options = ChromeOptions()
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            if self.screen_width and self.screen_height:
                driver.set_window_size(self.screen_width, self.screen_height)
            else:
                driver.maximize_window()

            driver.get(url)
            return driver

        elif self.driver_type == "firefox":
            firefox_options = FirefoxOptions()
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)

            if self.screen_width and self.screen_height:
                driver.set_window_size(self.screen_width, self.screen_height)
            else:
                driver.maximize_window()

            driver.get(url)
            return driver


file_path = "/home/vanya/PycharmProjects/selenium_framework/global_vars1.json"
json_data = read_json(file_path)

if json_data:
    webdriver_factory = WebDriverFactory(json_data)
    url = "https://www.facebook.com"
    driver = webdriver_factory.driver(url)
    time.sleep(5)
    driver.quit()
else:
    print("Fayl ne nayden")
