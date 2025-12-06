from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

def get_driver():
    # Use Chrome (or Firefox)
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--headless")  # uncomment to hide browser
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver