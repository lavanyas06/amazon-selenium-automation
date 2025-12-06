from utils.driver_setup import get_driver
from pages.home_page import HomePage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_to_cart():
    driver = get_driver()
    home = HomePage(driver)
    cart = CartPage(driver)

    # ⭐ Clear cart first so Add to Cart button always appears
    cart.clear_cart()

    home.open_home_page()

    # optional popup
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]"))
        ).click()
    except:
        pass

    home.search_product("mouse")

    cart.select_first_product()

    cart.add_to_cart()

    cart.open_cart()

    title = cart.verify_product_in_cart()
    assert len(title) > 3

    driver.quit()
