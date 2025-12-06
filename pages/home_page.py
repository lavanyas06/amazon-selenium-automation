from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_btn = (By.ID, "nav-search-submit-button")

    def open_home_page(self):
        print("Opening Amazon home page...")
        self.driver.get("https://www.amazon.com")
        time.sleep(3)
        print("✅ Amazon home page opened.")

    def search_product(self, product_name):
        print(f"Searching for: {product_name}")
        
        try:
            # Wait for search box to be visible and clickable
            search_input = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.search_box)
            )
            search_input.clear()
            search_input.send_keys(product_name)
            print(f"✅ Entered search term: {product_name}")
            
            time.sleep(1)
            
            # Click search button
            search_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(self.search_btn)
            )
            search_button.click()
            print("✅ Clicked search bar.")
            
            # Wait for results to load
            time.sleep(3)
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@data-component-type='s-search-result']")
                )
            )
            print("✅ Search results loaded.")
            
        except Exception as e:
            print(f"❌ Search failed: {e}")
            print(f"Current URL: {self.driver.current_url}")
            raise