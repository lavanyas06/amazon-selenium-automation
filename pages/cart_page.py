from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    # ⭐ NEW - CLEAR CART FUNCTION
    def clear_cart(self):
        print("🗑 Clearing cart...")

        # Go to cart page directly
        self.driver.get("https://www.amazon.in/gp/cart/view.html")

        try:
            delete_buttons = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//input[@value='Delete'] | //input[contains(@aria-label, 'Delete')]")
                )
            )

            print(f"Found {len(delete_buttons)} items to remove")

            for btn in delete_buttons:
                try:
                    self.driver.execute_script("arguments[0].click();", btn)
                    time.sleep(1)
                except:
                    pass

            print("🗑 Cart cleared successfully.")

        except:
            print("Cart already empty.")

    def select_first_product(self):
        print("Selecting first product...")

        try:
            # Wait for search results to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@data-component-type='s-search-result']")
                )
            )
            time.sleep(2)

            # Try multiple XPath strategies
            xpaths = [
                "(//div[@data-component-type='s-search-result'])[1]//h2//a",
                "(//span[@class='a-size-base-plus s-color-base s-spacing-none s-color-state-visited']//a)[1]",
                "(//a[@class='a-link-normal s-underline-text-link s-link'])[1]",
                "(//div[@data-component-type='s-search-result'][1])//a[contains(@href, '/dp/')]",
            ]

            product_link = None
            for xpath in xpaths:
                try:
                    product_link = WebDriverWait(self.driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, xpath))
                    )
                    print("✅ Found product with XPath")
                    break
                except:
                    continue

            if not product_link:
                raise Exception("Could not find product link")

            self.driver.execute_script("arguments[0].scrollIntoView(true);", product_link)
            time.sleep(1)
            product_link.click()
            print("✅ Clicked first product.")
            time.sleep(3)

            # Switch to new tab if opened
            if len(self.driver.window_handles) > 1:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                print("🔄 Switched to product tab.")

        except Exception as e:
            print(f"❌ Failed to select product: {e}")
            raise

    def add_to_cart(self):
        print("Adding to cart...")

        try:
            add_btn = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
            )
            add_btn.click()
            print("✅ Added to cart.")
            time.sleep(2)

            # Dismiss optional protection plan popup
            try:
                no_thanks = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@id='attachSiNoCoverage']"))
                )
                no_thanks.click()
                print("Dismissed optional popup.")
            except:
                pass

        except Exception as e:
            print(f"❌ Failed to add to cart: {e}")
            raise

    def open_cart(self):
        print("Opening cart...")

        try:
            cart_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.ID, "nav-cart"))
            )
            cart_link.click()
            print("✅ Cart opened.")
            time.sleep(2)

        except Exception as e:
            print(f"❌ Failed to open cart: {e}")
            raise

    def verify_product_in_cart(self):
        print("Verifying product in cart...")

        try:
            product_title = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='a-truncate-cut']"))
            )
            title = product_title.text
            print(f"✅ Product in cart: {title}")
            return title

        except Exception as e:
            print(f"❌ Failed to verify product: {e}")
            raise
