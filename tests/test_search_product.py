from utils.driver_setup import get_driver
from pages.home_page import HomePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_search():
    driver = get_driver()
    home_page = HomePage(driver)

    home_page.open_home_page()

    # ✅ Step 1: Handle "Continue Shopping" if it appears
    try:
        continue_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button"))
        )
        continue_btn.click()
        print("Clicked 'Continue Shopping' button.")
    except TimeoutException:
        print("'Continue Shopping' not found. Moving ahead...")

    # ✅ Step 2: Search for product
    home_page.search_product("latest macbook pro")

    time.sleep(10)
    driver.quit()
